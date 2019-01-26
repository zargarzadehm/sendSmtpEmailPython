import smtplib, ssl
from email.mime.text import MIMEText

print("Sending E-mail")

SUBJECT = 'SUBJECT EMAIL'
msg = 'EMAIL MESSAGE'
TO = 'receiver@email.com'
FROM = 'sender@email.com'

msg = MIMEText(msg)
msg['Subject'] = SUBJECT
msg['To'] = TO
msg['From'] = FROM

# Send the message via our own SMTP server.
context = ssl.create_default_context()
with smtplib.SMTP_SSL("SMTP.MAIL.COM", PORT_SMTP , context=context) as server:
    server.login("sender@email.com", "PASSWORD_SERVER")
    server.send_message(msg)
    print('email sent')
    server.quit()
