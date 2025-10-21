# Import the library
import qrcode

# Ask user for input text or link
data = input("Enter the text or URL to generate QR Code: ")

# Generate QR code
qr = qrcode.make(data)

# Save QR code as image file
qr.save("myqrcode.png")

print("QR Code generated and saved as myqrcode.png")
