import cv2
import os
# 1.creating a video object
def createFolder(directory):
       # print(Name)
        #print(directory+Name)
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                return directory
        except OSError: 
            print("false")
            print ('Error: Creating directory. ' +  directory)
            return False
def TakeImages(name):
    video = cv2.VideoCapture(0) 
    # 2. Variable
    a = 0
    count=0
    # 3. While loop
    folder_name = os.getcwd()+"\\"+name
    path=createFolder(folder_name)
    while True:
        a = a + 1
        count+=1
        # 4.Create a frame object
        check, frame = video.read()
        global gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Converting to grayscale
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 5.show the frame!
        cv2.imshow("Capturing",frame)
        cv2.imshow("Capturing_gray",gray)
        # 6.for playing 
        key = cv2.waitKey(1)
       
        #print(path)
        #print(path+"/Image"+str(count)+".jpg")
        cv2.imwrite(os.path.join(folder_name,"Image"+str(count)+".jpg"),gray)
        if key == ord('q'):
            break
    # 8. shutdown the camera
    video.release()
    cv2.destroyAllWindows