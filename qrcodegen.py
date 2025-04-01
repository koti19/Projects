import qrcode

qr = qrcode.QRCode(
    version = 10.0,
    box_size = 20,
    border = 5
)
 
data = "https://gemini.google.com/app"

try:
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black",back_color = "white")
    img.save("test.png")
    print("QR code generated and saved as test.png")


except qrcode.exceptions.DataOverflowError:
    print("Data too long for specified QR code version.")
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
