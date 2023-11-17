import re
import cv2
import pytesseract

img = cv2.imread('img.jpg')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    
osd = pytesseract.image_to_osd(img)
match = re.search('(?<=Script: )\d+', osd)
if match:
    script = match.group(0)
    # Faire quelque chose avec la variable 'script' ici
else:
    print("Aucune correspondance trouvée pour 'Script: \d+' dans la variable 'osd'")

angle = re.search('(?<=Rotate: )\d+', osd).group(0)
script = re.search('(?<=Script: )\d+', osd).group(0)
print("angle: ", angle)
print("script: ", script)    

cv2.imshow('img', img)
cv2.waitKey(0)