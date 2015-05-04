import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm #
from scipy import misc

import FnImConvolution


# Sample image
TestImage1 = misc.lena()

# Kernel: Sobel
Kernel = 0.125 * np.array([ [-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]] )

# 2D Convolution
print "Started!"
Result = FnImConvolution.FnImConvol( TestImage1, Kernel, 'mirror' )
print "Finished!"

# Plot result
plt.imshow(Result, cmap=cm.Greys_r)
plt.show()