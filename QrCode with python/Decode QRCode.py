from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/vicky/Desktop/Py Projects/QrCode with python/Qr-codes images/img.png')

result = decode(img)

print(result)