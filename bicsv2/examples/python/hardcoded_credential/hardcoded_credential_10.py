from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email():
    message = Mail(
        from_email='your-verified-email@example.com',
        to_emails='recipient@example.com',
        subject='Sending with SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>'
    )

    sg = SendGridAPIClient("SG.1234567890")
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
