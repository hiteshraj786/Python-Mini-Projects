import qrcode as Qr
from PIL import Image

qr = Qr.QRCode(version=1,error_correction=Qr.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.youtube.com/watch?v=xVU2UDaFOfE")
qr.make(fit=True)

img = qr.make_image(fill_color = "red",back_color = "white")

img.save("Radha_gori_gori.png")