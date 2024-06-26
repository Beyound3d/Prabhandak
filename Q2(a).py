import cv2
import numpy as np

# Define image paths
image_path1 = "hero5.webp"
image_path2 = "hero6.webp"

# Read images
image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

# Add the images
added_image = cv2.add(image1, image2)

# Show the images
cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Added Image", added_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
