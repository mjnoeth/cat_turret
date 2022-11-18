#!/usr/bin/python

try:
  import cv2
except Exception as e:
  print("Warning: OpenCV not installed. To use motion detection, make sure you've properly configured OpenCV.")

import argparse


def video_loop(args):
  """
  Uses the camera to move the turret. OpenCV ust be configured to use this.
  :return:
  """
  camera = cv2.VideoCapture(args["port"])
  detector = cv2.CascadeClassifier(args["cascade"])

  while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find kitty!
    rects = detector.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=3)
    for (i, (x, y, w, h)) in enumerate(rects):
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
      cv2.putText(frame, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Cat Faces', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # When everything is done, release the capture
  camera.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  ap = argparse.ArgumentParser()
  ap.add_argument("-p", "--port", default=0, help="camera port")
  ap.add_argument("-c", "--cascade", default="haarcascade_frontalcatface.xml", help="path to cat detector haar cascade")

  args = vars(ap.parse_args())

  video_loop(args)
