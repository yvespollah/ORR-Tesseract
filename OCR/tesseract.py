import cv2
import pytesseract

# Set the path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


# Read the image using OpenCV
image = cv2.imread('img5.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to preprocess the image
threshold_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)



# Use Tesseract to do OCR on the thresholded image
text = pytesseract.image_to_string(threshold_image)

# Print the detected text
print("Detected Text:\n", text)

# Display the original image and the thresholded image
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
