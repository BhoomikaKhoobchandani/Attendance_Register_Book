import cv2
import numpy
import pickle
import os

def FP():
    l=[]
    face_cascade = cv2.CascadeClassifier(os.getcwd()+'\\'+'haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")

    labels={"person_name": 1}
    with open("labels.pickle","rb") as f:
        og_labels=pickle.load(f)
        labels={v:k for k,v in og_labels.items()}


    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        global gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # try:
        faces =face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x, y, w, h) in faces:
            print(x,y,w,h)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            id_, conf = recognizer.predict(roi_gray)
            if conf>=45: #and conf <=85:
                print(id_)
                l.append(labels[id_])
                print(labels[id_]) 
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color=(255,255,255)
                stroke=2
                cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)


            # img_item = "my-img.png"
            # cv2.imwrite(img_item, roi_gray) 
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), (255,0,0), 2)



        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print(l)
    f=max(l,key=l.count)
    print(f)
    cap.release()
    cv2.destroyAllWindows()
