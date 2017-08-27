import cv2
import numpy as np

# Create Window
cv2.namedWindow('app')

# Dummy function to pass into the createTrackbar parameters
def dummy(val):
  pass

# Create Track bars within window to represent filters
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

# Loop to keep window open until 'q' key is pressed
while True:
  k = cv2.waitKey(1) & 0xFF
  if (k == ord('q')):
    break

# Destroy Window
cv2.destroyAllWindows()