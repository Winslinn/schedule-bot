from PIL import Image
import easyocr

reader = easyocr.Reader(['uk'])
text = reader.readtext('schedule/25.jpg', detail=0)

print(text)