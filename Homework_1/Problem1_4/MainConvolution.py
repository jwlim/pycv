import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm #
from scipy import misc

from FnImConvolution import FnImConvol


# Sample image
TestImage1 = misc.lena()

# Kernel
Kernel_1 = 0.125 * np.array([ [-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]] ) # 3x3
Kernel_2 = 1.0/256 * np.array( [ [1.0, 4.0, 6.0, 4.0, 1.0],
                                [4.0, 16.0, 24.0, 16.0, 4.0],
                                [6.0, 24.0, 36.0, 24.0, 6.0],
                                [4.0, 16.0, 24.0, 16.0, 4.0],
                                [1.0, 4.0, 6.0, 4.0, 1.0]])     # 5x5
Kernel_3 = np.array( [  [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0],
                        [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0],
                        [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0],
                        [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0],
                        [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0],
                        [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0],
                        [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0],
                        [-1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0] ] ) # 8x8

# 2D Convolution
Result_1 = FnImConvol( TestImage1, Kernel_1, 'zero' )
Result_2 = FnImConvol( TestImage1, Kernel_2, 'mirror' )
Result_3 = FnImConvol( TestImage1, Kernel_3, 'wrap' )

# Plot result
plt.figure('Kernel 1')
plt.imshow(Result_1, cmap=cm.Greys_r)

plt.figure('Kernel 2')
plt.imshow(Result_2, cmap=cm.Greys_r)

plt.figure('Kernel 3')
plt.imshow(Result_3, cmap=cm.Greys_r)
plt.show()