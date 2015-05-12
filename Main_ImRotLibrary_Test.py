#--------------------------------------------------------------------------------
# Image transformation and filtering functions of Computer Vision class (2015-1)
#
# Minchul Lee: Initial code generation (2015.05.07)
# Minchul Lee: Debug (2015.05.12)
#--------------------------------------------------------------------------------

# Import libraries
import numpy as np
import ImRotLibrary as IMRot

#------------------------------------------------------------------------
# Axis, angle to Rotation matrix representation example
print '\n1) Axis, angle to Rotation matrix representation example'
angle = 90.0 # degree
axis = np.float64(np.array([1,0,0])) # axis
RotMat = np.zeros((3,3)) # zero matrix initializaition
print 'Angle: ', angle, ' [deg], Axis: ', axis


# functino run
IMRot.Fn_AxisAngle2RotMat(RotMat, axis, angle)

print 'Rotation matrix:\n', RotMat
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# Rotation matrix to Axis, angle representation example
print '\n2) Rotation matrix to Axis, angle representation example'
print '[Info] Upeer rotation matrix is used for this exmaple\n'
#function run
axis_RotMat, angle_RotMat = IMRot.Fn_RotMat2AxisAngle(RotMat)

print 'Axis:', axis_RotMat, ', Angle: ', angle_RotMat, '[deg]'
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# quaternian to Rotation matrix representation example
print '\n3) quaternian to Rotation matrix representation example'
Quat = np.float64(np.array([np.sqrt(2)/2, 0, 0, -np.sqrt(2)/2]))
print 'Quaternion: ', Quat
RotMat_Quat = np.zeros((3,3))

IMRot.Fn_Quat2RotMat(Quat,RotMat_Quat)
print 'Rotation matrix:\n', RotMat_Quat
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# Rotation matrix to quaternian representation example
print '\n4) Rotation matrix to quaternian representation example'
print '[Info] Upeer rotation matrix is used for this exmaple\n'

Quat_RotMat = IMRot.Fn_RotMat2Quat(RotMat)
print 'Quaternion: ', Quat_RotMat
#------------------------------------------------------------------------
