import matplotlib.pyplot as plt
import numpy as np

plt.subplot(221)

# equivalent but more general
ax1 = plt.subplot(2, 2, 1)
plt.show()
"""
# add a subplot with no frame
ax2 = plt.subplot(222, frameon=False)

# add a polar subplot
plt.subplot(223, projection='polar')

# add a red subplot that shares the x-axis with ax1
plt.subplot(224, sharex=ax1, facecolor='red')

# delete ax2 from the figure
plt.delaxes(ax2)

# add ax2 to the figure again
plt.subplot(ax2)

# make the first axes "current" again
plt.subplot(221)"""