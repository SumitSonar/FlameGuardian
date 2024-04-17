from google.colab.patches import cv2_imshow
import cv2
import sys

VIDEO_URL = "Pollution.mp4"

cap = cv2.VideoCapture(VIDEO_URL)
if (cap.isOpened() == False):
  print('!!! Unable to open URL')
  sys.exit(-1)

fps = cap.get(cv2.CAP_PROP_FPS)
wait_ms = int(1000 / fps)
print('FPS:', fps)

success = False
frame = 0
while not success:
  success, frame = cap.read()
height, width, channels = frame.shape
print('Original Video Resolution:', height, ';', width)

while True:
  ret, frame = cap.read()
  if not ret:
    break
  cv2_imshow(frame)
  if cv2.waitKey(wait_ms) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()