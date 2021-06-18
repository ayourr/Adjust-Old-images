import cv2
import canny  as ced



#Image edge detection

"""
img  = cv2.imread("C:/Users/HP/Desktop/Projet py/test/capcv.png")

print(img[0][0])
gray = ced.rgb2gray(img)

print("Start processing ....")
print("**********************************")
detector = ced.cannyEdgeDetector([gray], sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
img_final = detector.detect()

cv2.imshow("orig",img_final[0])
def extract(orig,s,a,b):
    orig[s][0:a]=[0,0,0]
    orig[s][b:len(orig[s])]=[0,0,0]
def colorize(im):
    for l in im:
        a=0
        A = []
        z=len(im[0])-1
        Z = []
        while l[a] == 0 and a < z:
            a=a+1
            if l[a]==255 :
                A.append(a)
                break
        while l[z]==0 and z> 0:
            z = z-1
            if l[z]==255 :
                Z.append(z)
                break
        if len(A)!=0 and len(Z)!=0 :
            for k in range(A[0],Z[0]):
                l[k]=255

    return im

image=colorize(img_final[0],img)
cv2.imshow("Edge detection ",image)
cv2.waitKey(0)

#Video Edge detection
"""
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = ced.rgb2gray(frame)
    detector = ced.cannyEdgeDetector([gray], sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
    img_final = detector.detect()

    # Display the resulting frame
    cv2.imshow('frame',img_final[0])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
