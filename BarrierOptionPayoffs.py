import numpy as np
import matplotlib.pyplot as plt

#assign strike
K = 100

#generate s values
s = np.linspace(80,120,1000)

#assign barrier levels
call_knock_out_barrier = 110
call_knock_in_barrier = 110
put_knock_out_barrier = 90
put_knock_in_barrier = 90

#define payoff
call_knock_out_payoff = np.maximum(s-K,0)
call_knock_in_payoff = np.maximum(s-K,0)
put_knock_out_payoff = np.maximum(K-s,0)
put_knock_in_payoff = np.maximum(K-s,0)

#call knock out payoff
for i in range(len(s)):
    if s[i] > call_knock_out_barrier:
        call_knock_out_payoff[i] = 0
    else:
        call_knock_out_payoff[i] = max(s[i]-K,0)

#call knock in payoff
for i in range(len(s)):
    if s[i] < call_knock_in_barrier:
        call_knock_in_payoff[i] = 0
    else:
        call_knock_in_payoff[i] = max(s[i]-K,0)

#put knock out payoff
for i in range(len(s)):
    if s[i] < put_knock_out_barrier:
        put_knock_out_payoff[i] = 0
    else:
        put_knock_out_payoff[i] = max(K-s[i],0)

#put knock in payoff
for i in range(len(s)):
    if s[i] > put_knock_in_barrier:
        put_knock_in_payoff[i] = 0
    else:
        put_knock_in_payoff[i] = max(K-s[i],0)

#plotting
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(16,10))
ax[0,0].plot(s,call_knock_out_payoff)
ax[1,0].plot(s,call_knock_in_payoff)
ax[0,0].set_xlabel("Spot Price")
ax[1,0].set_xlabel("Spot Price")
ax[0,0].set_ylabel("Option Payoff")
ax[1,0].set_ylabel("Option Payoff")
ax[0,0].set_title('Call Knock Out Option')
ax[1,0].set_title('Call Knock In Option')
ax[0,1].plot(s,put_knock_out_payoff)
ax[1,1].plot(s,put_knock_in_payoff)
ax[0,1].set_xlabel("Spot Price")
ax[1,1].set_xlabel("Spot Price")
ax[0,1].set_ylabel("Option Payoff")
ax[1,1].set_ylabel("Option Payoff")
ax[0,1].set_title('Put Knock Out Option')
ax[1,1].set_title('Put Knock In Option')
plt.show()