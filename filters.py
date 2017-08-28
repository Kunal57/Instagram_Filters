import cv2
import numpy as np

# Create Window
cv2.namedWindow('app')

# Dummy function to pass into the createTrackbar parameters
def dummy(val):
  pass

# Store Image in the color_original variable
color_original = cv2.imread('TomBrady.jpg')

# Make an Image copy to store modified image into
color_modified = color_original.copy()

# Create Track bars within window to represent filters
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

# Loop to keep window open until 'q' key is pressed
while True:
  # Display the Modified Image to the window
  cv2.imshow('app', color_modified)
  k = cv2.waitKey(1) & 0xFF
  if (k == ord('q')):
    break

  # Store Track bar positions in variables
  contrast = cv2.getTrackbarPos('contrast', 'app')
  brightness = cv2.getTrackbarPos('brightness', 'app')

  # Add Color Modifications to the Original Image
  color_modified = cv2.addWeighted(color_original, contrast, np.zeros(color_original.shape, dtype=color_original.dtype), 0, brightness - 50)

# Destroy Window
cv2.destroyAllWindows()