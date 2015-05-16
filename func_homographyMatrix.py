import math
import numpy


#1.1 Make a homography matrix H from various transformation parameterization
def make_homography(a, *arg):

    arg_size = len(arg)+1

    #Translation
    if arg_size == 2:
        tx = a
        ty = arg[0]
        
        H = numpy.matrix(((1, 0, tx),
                         (0, 1, ty),
                         (0, 0, 1)))
        
        return H

    #Euclidean
    elif arg_size == 3:
        tx = a
        ty = arg[0]
        theta_rad = math.radians(arg[1])
        
        H = numpy.matrix(((math.cos(theta_rad), -math.sin(theta_rad), tx),
                         (math.sin(theta_rad), math.cos(theta_rad), ty),
                         (0, 0, 1)))

        return H

    #Similarity
    elif arg_size == 4:
        tx = a
        ty = arg[0]
        theta_rad = math.radians(arg[1])
        s = arg[2]

        H = numpy.matrix(((s*math.cos(theta_rad), -math.sin(theta_rad), tx),
                         (math.sin(theta_rad), s*math.cos(theta_rad), ty),
                         (0, 0, 1)))

        return H

    #Affine
    elif arg_size == 6:
        tx = a
        ty = arg[0]
        theta_rad = math.radians(arg[1])
        phi_rad = math.radians(arg[2])
        lamda1 = arg[3]
        lamda2 = arg[4]

        R_theta = numpy.matrix(((math.cos(theta_rad), -math.sin(theta_rad)),
                                (math.sin(theta_rad), math.cos(theta_rad))))
                                
        R_phi = numpy.matrix(((math.cos(phi_rad), -math.sin(phi_rad)),
                              (math.sin(phi_rad), math.cos(phi_rad))))
        
        D = numpy.matrix(((lamda1, 0),
                         (0, lamda2)))
        
        A = R_theta * R_phi.T * D * R_phi

        H = numpy.matrix(((A[0,0], A[0,1], tx),
                         (A[1,0], A[1,1], ty),
                         (0, 0, 1)))

        return H                     
    
    else:
        print '\n<usage>'
        print 'translation: make_homography(tx, ty)'
        print 'Euclidean: make_homography(tx, ty, theta)'
        print 'similarity: make_homography(tx, ty, theta, s)'
        print 'afine: make_homography(tx, ty, theta, phi, lamda1, lamda2)'
        print '---------------------------------------------------'
        return 0

    
