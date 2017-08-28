import cv2
import numpy as np

# Create Window
cv2.namedWindow('app')

# Dummy function to pass into the createTrackbar parameters
def dummy(val):
  pass

# Create identity kernal
identity_kernel = np.array([
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
])

# Create sharpen kernel
sharpen_kernel = np.array([
  [0, -1, 0],
  [-1, 5, 1],
  [0, -1, 0]
])

# Create a gaussian kernel
gaussian_kernel1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel2 = cv2.getGaussianKernel(5, 0)

# Create a box kernel
box_kernel = np.array([
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]
], np.float32) / 9

# Make List to store Kernals
kernels = [identity_kernel, sharpen_kernel, gaussian_kernel1, gaussian_kernel2, box_kernel]

# Store Image in the color_original variable
color_original = cv2.imread('TomBrady.jpg')

# Make an Image copy to store color modified image into
color_modified = color_original.copy()

# Store Gray Scale Image in the gray_original variable
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)

# Make an Image copy to store the gray scale modified image into
gray_modified = gray_original.copy()

# Create Track bars within window to represent filters
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

# Loop to keep window open until 'q' key is pressed
while True:
  # Store Gray Scale Track bar value in grayscale variable
  grayscale = cv2.getTrackbarPos('grayscale', 'app')

  if grayscale == 0:
    # Display the Modified Image to the window
    cv2.imshow('app', color_modified)
  else:
    # Display the Grayscale Image to the window
    cv2.imshow('app', gray_modified)

  k = cv2.waitKey(1) & 0xFF
  if (k == ord('q')):
    break

  # Store Track bar positions in variables
  contrast = cv2.getTrackbarPos('contrast', 'app')
  brightness = cv2.getTrackbarPos('brightness', 'app')
  kernel = cv2.getTrackbarPos('filter', 'app')

  # Store Modified Image after applying filter
  color_modified = cv2.filter2D(color_original, -1, kernels[kernel])

  # Store Modified Gray Image after applying filter
  gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel])

  # Add Modifications to the Original Image
  color_modified = cv2.addWeighted(color_modified, contrast, np.zeros(color_original.shape, dtype=color_original.dtype), 0, brightness - 50)

  # Add Modifications to the Original Gray Image
  gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros(gray_original.shape, dtype=gray_original.dtype), 0, brightness - 50)

# Destroy Window
cv2.destroyAllWindows()