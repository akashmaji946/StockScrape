import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase
from email import encoders







def sendmail():
	from_ = "akash.maji.technocrat@gmail.com"
	to_ = "akashmaji945@gmail.com"
	body="Hello from python"
	subject = "THIS IS SENT BY AKASH"

	msg = MIMEMultipart()
	msg['From'] = from_
	msg['To'] = to_
	msg['Subject'] = subject

	msg.attach(MIMEText(body, 'plain'))
	my_file= open('scrape.csv', 'rb')
	part = MIMEBase('application', "octet-stream")
	part.set_payload(my_file.read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename = '+'scrape.csv')

	msg.attach(part)

	message = msg.as_string()

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login('akash.maji.technocrat@gmail.com', 'zfevaivrlzplrvso')

	server.sendmail(from_, to_, message)
	server.quit()