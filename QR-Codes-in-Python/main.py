import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


def encode_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('QR-Codes-in-Python/qrcode.png')


def decode_qr(image):
    img = Image.open(image)
    result = decode(img)
    print(result)


if __name__ == "__main__":
    encode_qr(data=f"Please share this post if you liked this blog.")
    decode_qr('QR-Codes-in-Python/qrcode.png')