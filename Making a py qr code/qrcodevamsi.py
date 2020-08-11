import qrcode

qr = qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
data = 'www.billavamsikrishna.co'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green',back_color='white')
img.save('vamsi.png')
