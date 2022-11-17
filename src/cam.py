import cv2
import time

cam = cv2.VideoCapture(0)
# cam.set(3,1080)
cv2.namedWindow("Webcam")
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# img_counter = 0

while True:
    ret,frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("Webcam", frame)

    k = cv2.waitKey(1)


    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = "Face.jpg"
        # img = cv2.resize(frame, (256,256), interpolation=cv2.INTER_AREA)
        # cv2.imwrite(img_name, img)
        img = frame[0:480,80:560]
        cv2.imwrite(img_name, img)
        print("{} written!".format(img_name))

    # capture image every 10 seconds
    # if time.time() % 10 < 0.1:
    #     img_name = "Face.jpg"
    #     cv2.imwrite(img_name, frame)
    #     print("{} written!".format(img_name))

cam.release()

cam.destroyAllWindows()