import func_homographyMatrix
import func_affineConversion
import numpy

#1.2 test

#case 1. lamda1 > lamda2
print 'case 1. lamda1 > lamda2\n'

tx = 200
ty = 100
theta = 35
phi = 32
lamda1 = 1
lamda2 = 0.5

print '<input parameters>'
print 'tx = ', tx
print 'ty = ', ty
print 'theta = ', theta
print 'phi = ', phi
print 'lamda1 = ', lamda1
print 'lamda2 = ', lamda2

param = func_affineConversion.convert_affine_to_general(tx, ty, theta, phi, lamda1, lamda2)

a1 = param[0]
a2 = param[1]
a3 = param[2]
a4 = param[3]
a5 = param[4]
a6 = param[5]

H = numpy.matrix(((a1, a2, a3),
                  (a4, a5, a6),
                  (0, 0, 1)))

print '\naffine H = \n', H

param = func_affineConversion.convert_affine_from_general(a1, a2, a3, a4, a5, a6)

tx = param[0]
ty = param[1]
theta = param[2]
phi = param[3]
lamda1 = param[4]
lamda2 = param[5]

#same with input parameters
print '\n<result of conversion from general parameterization>'
print 'tx = ', tx
print 'ty = ', ty
print 'theta = ', theta
print 'phi = ', phi
print 'lamda1 = ', lamda1
print 'lamda2 = ', lamda2

#same homography matrix
H_2 = func_homographyMatrix.make_homography(tx, ty, theta, phi, lamda1, lamda2)
print '\nnew affine H = \n', H_2



print '--------------------------------------------------------------'

#case 2. lamda1 < lamda2
print 'case 2. lamda1 < lamda2\n'

lamda1 = 0.5
lamda2 = 1

print '<input parameters>'
print 'tx = ', tx
print 'ty = ', ty
print 'theta = ', theta
print 'phi = ', phi
print 'lamda1 = ', lamda1
print 'lamda2 = ', lamda2

param = func_affineConversion.convert_affine_to_general(tx, ty, theta, phi, lamda1, lamda2)

a1 = param[0]
a2 = param[1]
a3 = param[2]
a4 = param[3]
a5 = param[4]
a6 = param[5]

H = numpy.matrix(((a1, a2, a3),
                  (a4, a5, a6),
                  (0, 0, 1)))

print '\naffine H = \n', H

param = func_affineConversion.convert_affine_from_general(a1, a2, a3, a4, a5, a6)

tx = param[0]
ty = param[1]
theta = param[2]
phi = param[3]
lamda1 = param[4]
lamda2 = param[5]

#different phi, lamda1, lamda2
print '\n<result of conversion from general parameterization>'
print 'tx = ', tx
print 'ty = ', ty
print 'theta = ', theta
print 'phi = ', phi
print 'lamda1 = ', lamda1
print 'lamda2 = ', lamda2

#same homography matrix
H_2 = func_homographyMatrix.make_homography(tx, ty, theta, phi, lamda1, lamda2)
print '\nnew affine H = \n', H_2
