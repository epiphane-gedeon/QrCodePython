import qrcode
from PIL import Image
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)
qr.add_data("https://www.google.com")
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')
logo = Image.open('google.png')
logo_size_height = 60 
logo_size_width = 60
logo = logo.resize((logo_size_width, logo_size_height))
pos = ((img_qr.size[0] - logo_size_width) // 2, (img_qr.size[1] - logo_size_height) // 2)
img_qr.paste(logo, pos)
img_qr.save('QrCodeWithLogo.png')
