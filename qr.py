import qrcode
from PIL import Image
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)
qr.add_data("https://www.google.com")
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')
img_qr.save('QrCode.png')
