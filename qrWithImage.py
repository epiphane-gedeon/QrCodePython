import qrcode
from PIL import Image
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)
qr.add_data("https://www.google.com")
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')
logo = Image.open('google.png')# Path to the logo
logo_size_height = 60 # Height of the logo
logo_size_width = 60 # Width of the logo
logo = logo.resize((logo_size_width, logo_size_height)) # Resize the logo
pos = ((img_qr.size[0] - logo_size_width) // 2, (img_qr.size[1] - logo_size_height) // 2) # Position of the logo
img_qr.paste(logo, pos) # Paste the logo on the QR Code
img_qr.save('QrCodeWithLogo.png')
