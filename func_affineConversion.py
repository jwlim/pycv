import func_homographyMatrix
import math
import numpy


#1.2 Write a function that converts between two affine parameterizations, (a1,a2,...,a6) and (x,y,th,s,phi,aspect)

def convert_affine_from_general(a1, a2, a3, a4, a5, a6):

    H = numpy.matrix(((a1, a2, a3),
                      (a4, a5, a6),
                      (0, 0, 1)))

    A = numpy.matrix(((a1, a2),
                      (a4, a5)))


    #SVD(A) = UDVt = (UVt)(VDVt) = (R(theta))(R(-phi)DR(phi))
    
    U, D, Vt = numpy.linalg.svd(A, full_matrices=True)
    D = numpy.diag(D)

    if Vt[0,0] * Vt[1,1] < 0:
        Vt = numpy.matrix(((-Vt[0, 0], -Vt[0, 1]),
                          (Vt[1, 0], Vt[1, 1])))
        U = numpy.matrix(((-U[0, 0], U[0, 1]),
                          (-U[1, 0], U[1, 1])))
        
    R_theta = U*Vt
    R_phi = Vt


    #Get theta
    sin_theta = R_theta[1, 0]
    cos_theta = R_theta[0, 0]

    if cos_theta == 0:
        theta_rad = numpy.arcsin(sin_theta)

    else:
        tan_theta = sin_theta / cos_theta
        theta_rad = numpy.arctan(tan_theta)

    theta_deg = numpy.degrees(theta_rad)        
    
    #Get phi
    sin_phi = R_phi[1, 0]
    cos_phi = R_phi[0, 0]

    if cos_phi == 0:
        phi_rad = numpy.arcsin(sin_phi)
                
    else:
        tan_phi = sin_phi / cos_phi
        phi_rad = numpy.arctan(tan_phi)
        

    phi_deg = numpy.degrees(phi_rad)

    tx = a3
    ty = a6

    lamda1 = D[0,0]
    lamda2 = D[1,1]
    
    return tx, ty, theta_deg, phi_deg, lamda1, lamda2


def convert_affine_to_general(tx, ty, theta, phi, lamda1, lamda2):    
    
    H = func_homographyMatrix.make_homography(tx, ty, theta, phi, lamda1, lamda2)
    
    a1=H[0,0]
    a2=H[0,1]
    a3=tx
    a4=H[1,0]
    a5=H[1,1]
    a6=ty
    
    return a1, a2, a3, a4, a5, a6




