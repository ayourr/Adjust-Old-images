import cv2
""""
from app import change
print("Starting the prod function ...")
original = cv2.imread("./test.png")
print(original[5][5])
test2 = change(original,0,original.shape[0],0,original.shape[1])
"""
def product(a, b):
    m = []
    for i in range(len(a)):
        m.append(a[i] * b[i])
    return m
def limit (m) :
    a = []
    for i in range(0,m):
        a.append(0)
    a[0]=255
    a[m-1]=255
    return a
def One(m):
    a = []
    for i in range(0,m):
        a.append(0)
    a[0]=1
    a[m-1]=1
    return a
def full(k):
    t= []
    for i in range(k):
        t.append(255)
    return t
##################################### The Naive logic #########################
def spread(T):
    M = T
    for k in range (3,int(len(T)/2)-1):
        alpha = limit(k)
        beta = One(k)
        for i in range (len(T)):
            if len(alpha) + i <= len(T):
                if product(beta, T[i:len(alpha) + i]) == alpha:
                    print(alpha)
                    print("found a match")
                    M[i:len(alpha) + i] = full(len(alpha))

    return M
#####################################The optimised way ######################################



##############################################################################################
# Test functions to extracts usful data from images and adjust it to the spread function

def extract(image, m, n):
    A = []
    B = []
    C = []
    if n == 0:
        for i in range(image.shape[1]):
            A.append(image[m][i])
        return A
    elif n == 1:
        for i in range(image.shape[1]):
            B.append(image[m][i])
        return B
    elif n==2:
        for i in range(image.shape[1]):
            C.append(image[m][i])
        return C


# test will be done for image with 2 colors , red and white

def prod(image,original):
    cnst = original[1][1]
    print("Looking for matches ...")
    for i in range(image.shape[0]):
        A = spread(extract(image, i, 0))
        B = spread(extract(image, i, 1))
        C = spread(extract(image, i, 2 ))
        for j in range(image.shape[1]):
            if A[j] > 0 or B[j] > 0 or C[j] >0 :
                print(original[i][j])
                print("Changing the pixels now")
                original[i][j] = cnst
    print("Done ...")
    return original
""""
test = prod(test2)
cv2.imshow("Test Result", test)
cv2.waitKey()
"""
# it should be done for just white and black to work (
# it's working for black inside white ,next step is to develop a way
# to make it work for white in black so we can use the laplacian function)
"""
the horizontal spread is working fine , that means we can make it work for columns too
but we have to take just the intersection

"""
