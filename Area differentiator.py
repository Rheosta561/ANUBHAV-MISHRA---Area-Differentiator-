import cv2 as cv
import numpy as np
def areadifferentiator(x):
    y=str(x)
    img=cv.imread('images/'+y+'.png')

    

    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV) # creating an hsv mode of image for masking out various things .

    cv.waitKey(0) #Masking the unburnt area
    lowgreen=np.array([25,52,72])
    highgreen=np.array([102,255,255])
    unburnt=cv.inRange(hsv,lowgreen,highgreen)


    merg=cv.bitwise_and(img,img, mask=unburnt)

    merg1=cv.cvtColor(merg,cv.COLOR_BGR2HLS_FULL)
   

    # now we are going to mask out the burnt area from the main image 
    # so here we go 
    low_brown = np.array([5, 0, 0])           #NUMPY array values hsv , for brown colour
    high_brown = np.array([17,255,255])
    burnt=cv.inRange(hsv,low_brown,high_brown)


    burnt1=cv.bitwise_and(img,img,mask=burnt)

    burnt2=cv.cvtColor(burnt1,cv.COLOR_BGR2XYZ)
    
    f=cv.bitwise_or(merg1,burnt2) #MERGING THE BURNT AND THE UNBURNT AREA 

    #Masking out houses
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    low_blue = np. array([94, 80, 2]) 
    high_blue = np. array([126, 255, 255])
    house=cv.inRange(hsv,lower_red,upper_red)
    h1=cv.bitwise_and(img,img,mask=house)
    

    house2=cv.inRange(hsv,low_blue,high_blue)
    h2=cv.bitwise_and(img,img,mask=house2)
   
    fin=cv.bitwise_or(f,h1) #MERGING THE HOUSES WITH THE BURNT AND THE UNBURNT AREA 

    final=cv.bitwise_or(fin,h2)
    return final 


for i in range(1,12):
    x=str(i)
    print(x+".png , image received ")
    im=cv.imread("images/"+x+".png")
    out=areadifferentiator(i)
    ht1=np.hstack((im,out))

    cv.imshow("INPUT and OUTPUT IMAGES ARE  :",ht1)
    
    

    