from flask_mail import Message
from app import mail
import logging
from io import BytesIO
from reportlab.pdfgen import canvas


class EmailNotifier:
    def __init__(self):
        self.event_handlers = {
            "proof_request": self._handle_proof_request,
            "student_ticket_request": self._handle_student_ticket_request,
        }

    def notify(self, event, data):
        handler = self.event_handlers.get(event)
        if handler:
            try:
                handler(data)
                logging.info(f"Event '{event}' processed successfully.")
            except Exception as e:
                logging.error(f"Error processing event '{event}': {e}")
        else:
            logging.warning(f"No handler for event '{event}'.")

    def _handle_proof_request(self, data):
        subject = "Solicitud de certificado de alumno regular"
        body = (
            f"Estimado/a {data['name']},\n\n"
            f"Adjuntamos su certificado de alumno regular.\n\n"
            f"Saludos cordiales."
        )
        
        pdf_content = self._generate_proof_pdf(data)
     
        self._send_email(
            subject=subject,
            recipients=[data["email"]],
            body=body,
            attachments=[("Certificado_Alumno_Regular.pdf", "application/pdf", pdf_content)],
        )

    def _handle_student_ticket_request(self, data):
        subject = "Solicitud de boleto estudiantil"
        body = (
            f"Estimado/a {data['name']},\n\n"
            f"Recibimos su solicitud de boleto estudiantil.\n\n"
            f"Datos de la solicitud:\n"
            f"Número de Documento: {data['identity_number']}\n\n"
            f"Iniciaremos el trámite y nos pondremos en contacto con usted a la brevedad.\n\n"
            f"Saludos cordiales."
        )
        
        self._send_email(
            subject=subject,
            recipients=[data["email"]],
            body=body,
        )


    def _send_email(self, subject, recipients, body, attachments=None):
        try:
            msg = Message(subject=subject, recipients=recipients, body=body)

            if attachments:
                for filename, mime_type, content in attachments:
                    msg.attach(filename, mime_type, content)
            mail.send(msg)
            logging.info(f"Email sent to {recipients}")
        except Exception as e:
            logging.error(f"Error sending email to {recipients}: {e}")


    def _generate_proof_pdf(self, data):
        buffer = BytesIO()
        c = canvas.Canvas(buffer)
        c.drawString(100, 750, "Certificado de Alumno Regular")
        c.drawString(100, 720, f"Nombre: {data['name']}")
        c.drawString(100, 700, f"Número de Documento: {data['identity_number']}")
        c.drawString(100, 700, f"Número de Matrícula: {data['enrollment_number']}")
        c.save()
        buffer.seek(0)
        return buffer.read()
