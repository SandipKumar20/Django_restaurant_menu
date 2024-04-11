import qrcode

image = qrcode.make("http://127.0.0.1.8002")
image.save("qr.png")