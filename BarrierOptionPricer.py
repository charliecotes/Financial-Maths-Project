import numpy as np
from scipy.linalg import cholesky
import matplotlib.pyplot as plt


def monte_carlo_pricer(spot, K, T, r, theta, kappa, sigma, vt1, op_type, corr=0.5, barrier1=0,barrier2=0):
  
  # Monte Carlo Parameters
  N = 1000   # number of time steps
  M = 1000   # number of simulations
  dt = T/N

  # Correlation matrix between wiener processes assuming risk-neutrality
  rho = np.array([[1,corr],[corr,1]])
  # Perform cholesky decomposition
  lower_chol = cholesky(rho, lower=True)
  # Generate correlated Wiener variables
  Z = np.random.normal(0.0, 1.0, size=(N,M,2))
  W = Z @ lower_chol

  # Heston model adjustments for time steps
  kappadt = kappa*dt
  sigmasdt = sigma*np.sqrt(dt)

  # arrays for storing prices and variances
  lnSt = np.full(shape=(N+1,M), fill_value=np.log(spot))

  asset = np.full(shape=(N+1,M), fill_value=spot)

  vt = np.full(shape=(N+1,M), fill_value=vt1)

  Barrier = np.full(shape=(1,M), fill_value=1)

  for j in range(1,N+1):

    # Simulate variance processes using Heston
    vt[j] = vt[j-1] + kappadt*(theta - vt[j-1]) + sigmasdt*np.sqrt(vt[j-1])*W[j-1,:,1]

    # Simulate log asset prices using BS formula
    nu1dt = (r - 0.5*vt[j])*dt

    lnSt[j] = lnSt[j-1] + nu1dt + np.sqrt(vt[j]*dt)*W[j-1,:,0]
    
    #calculate asset price at each time step
    asset[j] = np.exp(lnSt[j])

    #store barrier status in matrix depending on number of barriers
    if barrier1 !=0:
      if barrier2 !=0:
        for i in range(0,M-1):
          if asset[j][i] > barrier2 or asset[j][i] < barrier1:
            Barrier[0][i] = 0
      else:
        for i in range(0,M-1):
          if asset[j][i] < barrier1:
              Barrier[0][i] = 0
    else:
      if barrier2 != 0:
        for i in range(0,M-1):
          if asset[j][i] > barrier2:
            Barrier[0][i] = 0        

  #final array of asset prices
  St = np.exp(lnSt)

  #calculate payoff for call/put
  for i in Barrier:
    if op_type == "call":
      CT = np.maximum(0,i * (St[-1] - K))
    elif op_type == "put":
      CT = np.maximum(0,i * (K - St[-1]))

  # Compute Expectation
  
  C0 = np.exp(-r*T)*np.sum(CT)/M

  #transpose St matrix so each row is a price process
  St_T = np.transpose(St)

  #create lists for barrier hit paths and non barrier hit paths 
  barrier_not_hit = []
  barrier_hit = []

  #filtering asset paths depending on barrier status
  for i in range(M):
    if Barrier[0][i] == 1:
      barrier_not_hit.append(list(St_T[i]))
    if Barrier[0][i] == 0:
      barrier_hit.append(list(St_T[i]))

  #create arrays
  barrier_hit_array = np.full(shape=(len(barrier_hit),N+1), fill_value=0.0)
  barrier_not_hit_array = np.full(shape=(len(barrier_not_hit),N+1), fill_value=0.0)

  #turn lists into arrays
  for i in range(len(barrier_hit)):
    barrier_hit_array[i] = barrier_hit[i]

  for i in range(len(barrier_not_hit)):
    barrier_not_hit_array[i] = barrier_not_hit[i]

  #transpose again so columns are price processes
  St_B = np.transpose(barrier_hit_array)
  St_nB = np.transpose(barrier_not_hit_array)

  #generate plots
  t = np.linspace(0,1,len(St))
  fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,8))
  ax[0].plot(t,St_nB[:,:20], 'g')
  ax[0].plot(t,St_B[:,:20], 'r')
  ax[0].set_title('Option Price')
  ax[1].plot(t,vt[:,:20])
  ax[1].set_title('Volatility')

  fig.suptitle("Option with Stochastic Volatility", fontsize=14)
  plt.show()

  return(C0)

#monte_carlo_pricer(100,100,1,0.01828,0.02,0.1,0.05,0.03,"put",0.5,barrier1=80,barrier2=120)