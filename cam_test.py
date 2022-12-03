import cv2

#Start video capture
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH,1280/4)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,480/2)

while(True):
    ret, frame = vid.read()

    #Display images
    cv2.imshow('image', frame)

    #Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()