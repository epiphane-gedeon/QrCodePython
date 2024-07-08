# QrCodePython

This project is a simple Python application that generates QR codes. You can use it to create QR codes for URLs, text.

## Features

- Generate QR codes for any text or URL.
- Save QR codes as image files.
- Optionally, add a logo to the center of the QR code.

## Requirements

- Python 3.6+
- qrcode library
- Pillow library (for image processing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/epiphane-gedeon/QrCodePython.git
   cd QrCodePython
2. Create a virtual environment (optional but recommended):
   - On Windows
      ```bash
      py -3 -m venv .venv
      .venv\Scripts\activate
      pip install -r requirements.txt

   - On Mac or Linux
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
