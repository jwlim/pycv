#--------------------------------------------------------------------------------
# Image transformation and filtering functions of Computer Vision class (2015-1)
#
# Minchul Lee: Initial code generation (2015.04.29)
#
#
#
#
#
#--------------------------------------------------------------------------------

# import the basic librarires
from math import atan2, cos, sin, sqrt, pi
from numpy import float64, hypot, zeros, flatnonzero, array

# Makes 3D rotation matrices from axis/angle
def Fn_AxisAngle2RotMat(matrix, axis, angle):
    # Trig factors.
    ca = cos(pi*angle/180)
    sa = sin(pi*angle/180)
    C = 1 - ca

    # Depack the axis.
    x, y, z = axis

    # Multiplications (to remove duplicate calculations).
    xs = x*sa
    ys = y*sa
    zs = z*sa
    xC = x*C
    yC = y*C
    zC = z*C
    xyC = x*yC
    yzC = y*zC
    zxC = z*xC

    # Update the rotation matrix.
    matrix[0, 0] = x*xC + ca
    matrix[0, 1] = xyC - zs
    matrix[0, 2] = zxC + ys
    matrix[1, 0] = xyC + zs
    matrix[1, 1] = y*yC + ca
    matrix[1, 2] = yzC - xs
    matrix[2, 0] = zxC - ys
    matrix[2, 1] = yzC + xs
    matrix[2, 2] = z*zC + ca


# Makes 3D rotation matrices from quaternion
def Fn_Quat2RotMat(quat, matrix):
    #Convert a quaternion into rotation matrix form.

    # Repetitive calculations.
    q4_2 = quat[3]**2
    q12 = quat[0] * quat[1]
    q13 = quat[0] * quat[2]
    q14 = quat[0] * quat[3]
    q23 = quat[1] * quat[2]
    q24 = quat[1] * quat[3]
    q34 = quat[2] * quat[3]

    # The diagonal.
    matrix[0, 0] = 2.0 * (quat[0]**2 + q4_2) - 1.0
    matrix[1, 1] = 2.0 * (quat[1]**2 + q4_2) - 1.0
    matrix[2, 2] = 2.0 * (quat[2]**2 + q4_2) - 1.0

    # Off-diagonal.
    matrix[0, 1] = 2.0 * (q12 - q34)
    matrix[0, 2] = 2.0 * (q13 + q24)
    matrix[1, 2] = 2.0 * (q23 - q14)

    matrix[1, 0] = 2.0 * (q12 + q34)
    matrix[2, 0] = 2.0 * (q13 - q24)
    matrix[2, 1] = 2.0 * (q23 + q14)

# Converts 3D rotation matrices to axis/angle
def Fn_RotMat2AxisAngle(matrix):
    # Axes.
    axis = zeros(3, float64)
    axis[0] = matrix[2,1] - matrix[1,2]
    axis[1] = matrix[0,2] - matrix[2,0]
    axis[2] = matrix[1,0] - matrix[0,1]

    # Angle.
    r = hypot(axis[0], hypot(axis[1], axis[2]))
    t = matrix[0,0] + matrix[1,1] + matrix[2,2]
    theta = 180*atan2(r, t-1)/pi

    # Normalise the axis.
    axis = axis / r

    # Return the data.
    return axis, theta


# Converts 3D rotation matrices to quaternion
def Fn_RotMat2Quat(matrix):
    # Estimate the denominator
      den = array([ 1.0 + matrix[0,0] - matrix[1,1] - matrix[2,2],
                       1.0 - matrix[0,0] + matrix[1,1] - matrix[2,2],
                       1.0 - matrix[0,0] - matrix[1,1] + matrix[2,2],
                       1.0 + matrix[0,0] + matrix[1,1] + matrix[2,2]])
      
      max_idx = flatnonzero(den == max(den))[0]
    
      quat = zeros(4)
      quat[max_idx] = 0.5 * sqrt(max(den))
      denom = 4.0 * quat[max_idx]
      if (max_idx == 0):
         quat[1] =  (matrix[1,0] + matrix[0,1]) / denom 
         quat[2] =  (matrix[2,0] + matrix[0,2]) / denom 
         quat[3] = -(matrix[2,1] - matrix[1,2]) / denom 
      if (max_idx == 1):
         quat[0] =  (matrix[1,0] + matrix[0,1]) / denom 
         quat[2] =  (matrix[2,1] + matrix[1,2]) / denom 
         quat[3] = -(matrix[0,2] - matrix[2,0]) / denom 
      if (max_idx == 2):
         quat[0] =  (matrix[2,0] + matrix[0,2]) / denom 
         quat[1] =  (matrix[2,1] + matrix[1,2]) / denom 
         quat[3] = -(matrix[1,0] - matrix[0,1]) / denom 
      if (max_idx == 3):
         quat[0] = -(matrix[2,1] - matrix[1,2]) / denom 
         quat[1] = -(matrix[0,2] - matrix[2,0]) / denom 
         quat[2] = -(matrix[1,0] - matrix[0,1]) / denom 
    
      return quat