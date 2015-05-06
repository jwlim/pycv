import func_homographyMatrix

import math
import numpy
import scipy
import matplotlib.pyplot as plt

#backward warping
def backward_warping(src, dst, H_inv):
    height = dst.shape[0]
    width = dst.shape[1]

    for y in range(0, height):
        for x in range(0, width):
            
            dst_coord = numpy.matrix((x,y,1)).T
            src_coord = H_inv*dst_coord

            src_x = src_coord[0]
            src_y = src_coord[1]

            if src_x >= 0 and src_x < width-1 and src_y >= 0 and src_y < height-1:

                #bilinear interpolation
                x1 = math.floor(src_x)
                y1 = math.floor(src_y)
                x2 = x1 + 1
                y2 = y1 + 1
                dx = src_x - x1
                dy = src_y - y1

                a = dx*src[y1,x2] + (1-dx)*src[y1,x1]
                b = dx*src[y2,x2] + (1-dx)*src[y2,x1]
                val = dy*b + (1-dy)*a;

                #dst[y,x]=src[math.floor(src_y),math.floor(src_x)]   #without bilinear interpolation
                dst[y,x]=val #with bilinear interpolation

#1.1 test
                
#Making homography matrix

tx = 10
ty = 30
theta = 60
s = 2

phi = 30
lamda1 = 2
lamda2 = 1

H_translation = func_homographyMatrix.make_homography(tx, ty)
H_euclidean = func_homographyMatrix.make_homography(tx, ty, theta)
H_similarity = func_homographyMatrix.make_homography(tx, ty, theta, s)
H_affine = func_homographyMatrix.make_homography(tx, ty, theta, phi, lamda1, lamda2)


#Image warping using homography matrix

img_src = scipy.misc.lena()
height = img_src.shape[0]
width = img_src.shape[1]

plt.figure()
plt.subplot(121)
plt.imshow(img_src, cmap=plt.cm.gray)

img_dst = numpy.zeros(img_src.shape, dtype=numpy.uint8)

tx = 200
ty = 100
theta = 45
phi = 20
lamda1 = 1
lamda2 = 0.5

H = func_homographyMatrix.make_homography(tx, ty, theta, phi, lamda1, lamda2)
H_inv = numpy.linalg.inv(H)
backward_warping(img_src, img_dst, H_inv)

plt.subplot(122)
plt.imshow(img_dst, cmap=plt.cm.gray)
plt.show()
