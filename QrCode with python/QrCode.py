import qrcode

data = 'My Name is Vignesh'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('C:/Users/vicky/Desktop/Py Projects/QrCode with python/Qr-codes images/img.png')