import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(mail_host, mail_port, mail_from, mail_to, msg):
    # connect smtp server, set debug to see reply information
    smtp = smtplib.SMTP()
    smtp.connect(mail_host, mail_port)
    smtp.set_debuglevel(1)
    # send mail
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    # quit
    smtp.quit()


def get_massage(mail_from, mail_to):
    msg = MIMEMultipart('alternative')
    # from, to, subject
    msg["From"] = mail_from
    msg["To"] = ";".join(mail_to)
    msg['Subject'] = r"Oooooooooooooooops"
    # html
    html = """\
	<html>
		<head><meta charset="UTF-8"></head>
		<body>
			<p>Hello, World!</p>
			<p>The attach is the script to send this email.</p>
		</body>
	</html>
	"""
    content = MIMEText(html, 'html', 'UTF-8')
    msg.attach(content)
    # end
    return msg


if __name__ == "__main__":
    # host:port
    mail_host = "smtp.gmail.com"
    mail_port =
    # mail from and mail to
    mail_from = "master@example.com.cn"
    mail_to = ["ojas.dubey@gmail.com"]
    # massage
    msg = get_massage(mail_from, mail_to)
    # send
    send_mail(mail_host, mail_port, mail_from, mail_to, msg)