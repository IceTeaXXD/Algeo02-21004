import cv2
import time

cam = cv2.VideoCapture(0)

cv2.namedWindow("Webcam")

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

    # elif k%256 == 32:
    #     # SPACE pressed
    #     img_name = "opencv_frame_{}.png".format(img_counter)
    #     cv2.imwrite(img_name, frame)
    #     print("{} written!".format(img_name))
    #     img_counter += 1

    # capture image every 10 seconds
    if time.time() % 10 < 0.1:
        img_name = "Face.jpg"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

cam.release()

cam.destroyAllWindows()