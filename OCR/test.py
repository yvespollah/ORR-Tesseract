import cv2
import pytesseract
import matplotlib.pyplot as plt

# Définir le chemin vers l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Lire l'image avec OpenCV
image = cv2.imread('img6.png')


# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image)


# # Appliquer un seuillage pour binariser l'image
# # threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_,threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# imwrite sert a enregistrer l'image
cv2.imwrite('image_gris.jpg', gray_image)

# Use Tesseract to do OCR on the thresholded image
text = pytesseract.image_to_string(threshold_image)

# Print the detected text
print("Detected Text:\n", text)

# Afficher l'image en niveaux de gris
cv2.imshow('Image en niveaux de gris', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



