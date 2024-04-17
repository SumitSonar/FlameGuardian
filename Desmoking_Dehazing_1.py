from google.colab.patches import cv2_imshow
import cv2
import sys
import numpy as np

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

# Define the desmoking function
def desmoke(frame):
  # Convert the frame to HSV color space
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  # Apply a threshold to the V channel to get a binary mask of the smoke
  _, mask = cv2.threshold(hsv[:,:,2], 200, 255, cv2.THRESH_BINARY)
  # Bitwise-AND the frame with the inverted mask to remove the smoke
  result = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
  # Use image inpainting to fill in the missing regions
  mask = cv2.dilate(mask, np.ones((3,3),np.uint8),iterations=2)
  result = cv2.inpaint(result, mask, 3, cv2.INPAINT_TELEA)
  return result

# Define the dehazing function
def dehaze(frame):
  # Convert the frame to HSV color space
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  # Apply a threshold to the S channel to get a binary mask of the haze
  _, mask = cv2.threshold(hsv[:,:,1], 100, 255, cv2.THRESH_BINARY)
  # Bitwise-AND the frame with the inverted mask to remove the haze
  result = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
  # Use image inpainting to fill in the missing regions
  mask = cv2.dilate(mask, np.ones((3,3),np.uint8),iterations=2)
  result = cv2.inpaint(result, mask, 3, cv2.INPAINT_TELEA)
  return result

while True:
  ret, frame = cap.read()
  if not ret:
    break
  # Apply desmoking and dehazing to the frame
  frame = desmoke(frame)
  frame = dehaze(frame)
  cv2_imshow(frame)
  if cv2.waitKey(wait_ms) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()