import qrcode
yt_link = "https://youtu.be/XODUmAc5P2U?si=e6_2YRO5oGf2Pts8"
qr = qrcode.add(yt_link)
qr.make(fit=True)
qr = qrcode.QRCode(Version =1 , box_size= 10, border= 4)
img = qr.make_image(fill = "black", back_color="white")
img.save("yt.png")