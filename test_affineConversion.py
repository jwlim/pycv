import func_affineConversion

#1.2 test

#case 1. lamda1 > lamda2

tx = 100
ty = 30
theta = 30
phi = 45
lamda1 = 2
lamda2 = 1

param = func_affineConversion.convert_affine_to_general(tx, ty, theta, phi, lamda1, lamda2)
func_affineConversion.convert_affine_from_general(param[0], param[1], param[2], param[3], param[4], param[5])

print '--------------------------------------------------------------'
#case 2. lamda1 < lamda2'

lamda1 = 1
lamda2 = 2

param = func_affineConversion.convert_affine_to_general(tx, ty, theta, phi, lamda1, lamda2)
func_affineConversion.convert_affine_from_general(param[0], param[1], param[2], param[3], param[4], param[5])
