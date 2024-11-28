import qrcode
from io import BytesIO
from flask import url_for, send_file

class QRCodeFactory:
    @staticmethod
    def generate_event_qr(event_name, start_date, end_date):
        qr_data = (
            f"BEGIN:VCALENDAR\n"
            f"VERSION:2.0\n"
            f"BEGIN:VEVENT\n"
            f"SUMMARY:{event_name}\n"
            f"DTSTART:{start_date.strftime('%Y%m%dT%H%M%SZ')}\n"
            f"DTEND:{end_date.strftime('%Y%m%dT%H%M%SZ')}\n"
            f"END:VEVENT\n"
            f"END:VCALENDAR"
        )

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        return img_buffer
