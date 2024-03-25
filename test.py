from PIL import Image
from io import BytesIO
import easyocr

image = Image.open('schedule/25.jpg')
width, height = image.size
image = image.crop((135, 0, width/2, height))

img_bytes = BytesIO()
image.save(img_bytes, format='JPEG')
img_bytes = img_bytes.getvalue()

reader = easyocr.Reader(['uk'])
text = reader.readtext(img_bytes, detail=0)

print(text)