import cv2
import cv2.data

capt = cv2.VideoCapture(0)

face_dector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

while True:
    ret, frame = capt.read()

    xyz = face_dector.detectMultiScale(frame, 1.1, 2)

    for x, y, w, h in xyz:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (10, 245, 34), 3)

    cv2.putText(frame, "opencv video", (50, 50), 2, 2, (12, 255, 34), 3)

    cv2.imshow("eeeee", frame)

    if cv2.waitKey(20) & 0xff == ord("e"):
        break