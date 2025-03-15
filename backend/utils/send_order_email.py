import smtplib
from email.message import EmailMessage
from config import settings


async def submit(
    customer:str,
    phone: str,
    email: str,
):
    email_address = settings.EMAIL_ADDRESS
    email_password = settings.EMAIL_PASSWORD

    msg = EmailMessage()
    msg['Subject'] = 'Email subject'
    msg['From'] = email_address
    msg['To'] = email
    msg.set_content(
        f"""\
    Name: {customer},
    Phone: {phone},
    Email: {email},
    """,
    )
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    return "successfully sent"
