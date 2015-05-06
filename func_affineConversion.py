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
    theta_rad = numpy.arcsin(R_theta[1,0])
    theta_deg = numpy.degrees(theta_rad)
    
    #Get phi
    phi_rad = numpy.arcsin(R_phi[1,0])
    phi_deg = numpy.degrees(phi_rad)

    tx = a3
    ty = a6

    lamda1 = D[0,0]
    lamda2 = D[1,1]

    print '\nconvert_affine_from_general\n'
    print 'tx = ', tx
    print 'ty = ', ty
    print 'theta_degree = ', theta_deg
    print 'phi_degree = ', phi_deg
    print 'lamda1 = ',lamda1
    print 'lamda2 = ',lamda2
    
    return tx, ty, theta_deg, phi_deg, lamda1, lamda2


def convert_affine_to_general(tx, ty, theta, phi, lamda1, lamda2):    
    
    theta_rad = math.radians(theta)
    phi_rad = math.radians(phi)
    
    R_theta = numpy.matrix(((math.cos(theta_rad), -math.sin(theta_rad)),
                            (math.sin(theta_rad), math.cos(theta_rad))))

    R_phi = numpy.matrix(((math.cos(phi_rad), -math.sin(phi_rad)),
                          (math.sin(phi_rad), math.cos(phi_rad))))

          
    D = numpy.matrix(((lamda1, 0),
                      (0, lamda2)))

    A = R_theta * R_phi.T * D * R_phi
    
    a1=A[0,0]
    a2=A[0,1]
    a3=tx
    a4=A[1,0]
    a5=A[1,1]
    a6=ty

    H_A = numpy.matrix(((a1, a2, a3),
                        (a4, a5, a6),
                        (0, 0, 1)))
    
    print '\nconvert_affine_to_general\n'
    print 'tx = ', tx
    print 'ty = ', ty
    print 'theta_degree = ', theta
    print 'phi_degree = ', phi
    print 'lamda1 = ',lamda1
    print 'lamda2 = ',lamda2
    
    print '\nH_A =\n', H_A
    
    return a1, a2, a3, a4, a5, a6




