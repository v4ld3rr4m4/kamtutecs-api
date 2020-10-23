import cv2
import numpy as np
import base64
import pytesseract
import os

image = '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'
decoded_data = base64.b64decode(image)
np_data = np.frombuffer(decoded_data,np.uint8)
imgBGR = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
imgRGB = cv2.cvtColor(imgBGR , cv2.COLOR_BGR2RGB)
grey_img = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)

# pse = page segmentation mode
# oem = ocr engine mode (algorithm used)
tessdata_dir = [os.getcwd(), 'tessdata-fast']
tess_path = '/'.join(tessdata_dir)
config = f'--oem 3 --psm 6'
ocr_text = pytesseract.image_to_string(grey_img, config=config)
print(ocr_text)