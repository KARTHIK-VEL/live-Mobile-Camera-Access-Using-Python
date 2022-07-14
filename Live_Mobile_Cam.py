import cv2
capture = cv2.VideoCapture("http://username/video")
while(True):
   ret, frame = capture.read()
   cv2.imshow('livestream', frame)
   if cv2.waitKey(1) == ord("q"):
      break
capture.release()
cv2.destroyAllWindows()
