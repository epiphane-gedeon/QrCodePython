import qrcode
from PIL import Image
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H, # The error correction level
)
qr.add_data("https://www.google.com") # URL to be encoded (it could be any text)
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB') # Create the QR Code
img_qr.save('QrCode.png') # Save the QR Code
