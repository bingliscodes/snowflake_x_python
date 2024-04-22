from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import os
import smtplib

# Email addresses
address_list = ["benjamin.inglis@dentwizard.com"]
csv_path = r"C:\Users\BInglis\Code\Snowflake_Py_Project\VINS_to_Onestream_v3.csv"  # Use a raw string for the path

# Set up connection to the email server
smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(os.getenv('OUTLOOK_USER'), os.getenv('OUTLOOK_PASSWORD'))

# Email content
subject = "Test"
text = "Testing. . . testing. . . 1 2 3"

# Build the message
msg = MIMEMultipart()
msg['From'] = os.getenv('OUTLOOK_USER')  # Ensure the From header is set
msg['To'] = ", ".join(address_list)
msg['Subject'] = subject
msg.attach(MIMEText(text))

# Attaching the file
with open(csv_path, 'rb') as f:
    file = MIMEApplication(
        f.read(),
        Name=os.path.basename(csv_path)
    )
    file['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(csv_path))
    msg.attach(file)

# Send the email
smtp.sendmail(from_addr=os.getenv('OUTLOOK_USER'), to_addrs=address_list, msg=msg.as_string())
smtp.quit()
