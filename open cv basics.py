import cv2 as cv

def imreader():
    loc=input("enter the location of your file or the name if this program is in the same folder ")
    pic=cv.imread(loc)
    cv.imshow("output",pic)
    cv.waitKey(0)
    print("image is displayed , if you do not find out on your screen see the taskbar")
def vidreader():
    y=input("enter the location of your video")
    cap=cv.VideoCapture(y)
    while True:
        success , img=cap.read()
        cv.imshow("image",img)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
print("opencv module imported successfully ") #importing module

while True:
    print("Enter your choice \n")
    print("1.reading an image \n")
    print("2.reading a video \n")
    x=int(input("enter your desicion : \t "))
    if x==1:
        imreader()
    if x==2:
        vidreader()
        



        
