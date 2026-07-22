import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=xVU2UDaFOfE")
img.save("song_yt.png")