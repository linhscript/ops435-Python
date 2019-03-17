import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'havanlinh304@gmail.com'
password = 'H@v@nl1nh'
send_to_email = ['vlha@myseneca.ca','havanlinh304@gmail.com','havanlinh3494@gmail.com']
subject = 'TEST MAIL multiple users'
message = 'Here is a message from python.'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = ",".join(send_to_email)
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()

try:
	server.sendmail(email, send_to_email, text)
	print("Sent")
except:
	print("Failed")

server.quit()