from fbm import fbm, fgn, times
import matplotlib.pyplot as plt
import numpy as np

# Generate a fBm realization
fbm_low_H = fbm(n=1024, hurst=0.25, length=1, method='daviesharte')
fbm_mid_H = fbm(n=1024, hurst=0.5, length=1, method='daviesharte')
fbm_high_H = fbm(n=1024, hurst=0.75, length=1, method='daviesharte')


# Get the times associated with the fBm
t_values = times(n=1024, length=1)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(16,4))
ax[0].plot(t_values,fbm_low_H)
ax[1].plot(t_values,fbm_mid_H)
ax[2].plot(t_values,fbm_high_H)
ax[0].set_title('H=0.25')
ax[1].set_title('H=0.5')
ax[2].set_title('H=0.75')

plt.show()