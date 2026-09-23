import qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = "https://qunghia.github.io/Driver-Feedback/"

MATCHA_DARK = "#3F5F3A"
CREAM = "#FFFDF5"

OUTPUT_FILE = "driver_feedback_qr_matcha.png"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=14,
    border=4,
)

qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(
    fill_color=MATCHA_DARK,
    back_color=CREAM
).convert("RGB")

img.save(OUTPUT_FILE)

print(f"QR code created: {OUTPUT_FILE}")
print(f"URL: {URL}")
