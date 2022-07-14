import cv2
capture = cv2.VideoCapture("http://25.149.199.7:8080/video")
while(True):
   ret, frame = capture.read()
   cv2.imshow('livestream', frame)
   if cv2.waitKey(1) == ord("q"):
      break
capture.release()
cv2.destroyAllWindows()
