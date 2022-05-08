import numpy as np
import matplotlib.pyplot as plt

#assign strike
K = 100

#generate s values
s = np.linspace(80,120,1000)

#payoff functions
call_payoff = np.maximum(s-K,0)
put_payoff = np.maximum(K-s,0)

#plotting
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,8))
ax[0].plot(s,call_payoff)
ax[1].plot(s,put_payoff)
ax[0].set_xlabel("Spot Price")
ax[1].set_xlabel("Spot Price")
ax[0].set_ylabel("Option Payoff")
ax[1].set_ylabel("Option Payoff")
ax[0].set_title('Call Option')
ax[1].set_title('Put Option')
plt.show()