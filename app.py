import cv2
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
from Core import prod
import canny as ced

################## The test image ############
height = 800
width = 800
blank_image = np.zeros((height, width, 3), np.uint8)
blank_image[:, 0:width] = (255, 255, 255)  # (B, G, R
img2 = cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB)
im_test = Image.fromarray(img2)


############################### image prod ############


#######################################################

def open_img():
    global img_prod
    x = filedialog.askopenfilename(title='"pen')
    img = Image.open(x)
    img = img.resize((800, 800), Image.ANTIALIAS)
    img_prod = img
    img = ImageTk.PhotoImage(img)
    return img


################## Image processing ################


def sample(a, b, c, d):
    image = cv2.cvtColor(np.asarray(img_prod), cv2.COLOR_RGB2BGR)
    if b >= 800:
        b = 799
    if d >= 800:
        d = 799
    if c < 0:
        c = 0
    if a < 0:
        a = 0
    demo =spread(image,a,b,c,d)
    for i in range(c,d):
        for j in range(a,b):
            image[j][i]=demo[j-a][i-c]
    im = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2RGB)
    immg = ImageTk.PhotoImage(Image.fromarray(im))
    return immg
###############################  For Tests  #################################
def change(image,a,b,c,d):
    blank_image = np.zeros((b-a,d-c, 3), np.uint8)
    img2 = cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB)
    im = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2RGB)
    for i in range(c,d):
        for j in range(a,b):
            img2[j-a][i-c]=im[j][i]
    #lap = cv2.Sobel(img2,cv2.CV_8U,1,0,5)
    #lap = cv2.Laplacian(img2,cv2.CV_8U)
    gray = ced.rgb2gray(img2)
    detector = ced.cannyEdgeDetector([gray], sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
    lap = detector.detect()
    print(lap[0][0][0])
    return lap[0]

################################The core function of the app version 1.0 #######################################
def spread(image,a,b,c,d):
    blank_image = np.zeros((b-a,d-c, 3), np.uint8)
    demo = cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB)
    for i in range(a,b):
        for j in range(c,d):
            demo[i-a][j-c]=image[i][j]
    lap = change(image,a,b,c,d)
    cv2.imshow("lap",lap)
    result = prod(lap,demo)
    return result



