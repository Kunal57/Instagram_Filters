import cv2
import numpy as np

# Create Window
cv2.namedWindow('app')

# Loop to keep window open until 'q' key is pressed
while True:
  k = cv2.waitKey(1) & 0xFF
  if (k == ord('q')):
    break

# Destroy Window
cv2.destroyAllWindows()