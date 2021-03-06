import smtplib
import mimetypes

from app import app
from werkzeug.utils import secure_filename
from flask import flash, render_template, request

from email.message import EmailMessage
from email.utils import make_msgid

@app.route('/')
def email_page():
	return render_template('home.html')

@app.route('/log')
def logi():
	return render_template('login.html')


@app.route('/about')
def abou():
	return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['password'] != request.form['password2'] :
			error = 'Pleasee Check Password'
		else:
			global email_add
			email_add = request.form['username']
			global pass_word
			pass_word = request.form['password']
			return render_template('emails.html',template1 = open('templates/template1.html').read())
	return render_template('login.html', error=error)

@app.route('/send', methods=['POST'])
def send_email():
	subject = request.form['email-subject']
	body = request.form['email-body']
	emails = request.form['emails']
	email = 'fake334912@gmail.com'
	passd = 'Fake@3342'
	if subject and body and emails:

		msg = EmailMessage()

		asparagus_cid = make_msgid()

		msg['Subject'] = subject
		msg['From'] = email_add
		msg['To'] = (emails)

		msg.add_alternative(body.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

		if 'email-attachments[]' in request.files:
			files = request.files.getlist('email-attachments[]')

			for file in files:
				filename = secure_filename(file.filename)

				ctype = mimetypes.MimeTypes().guess_type(filename)[0]

				if ctype is None:
					ctype = 'application/octet-stream'

				maintype, subtype = ctype.split('/', 1)
				f_data = file.read()

				msg.add_attachment(f_data, maintype=maintype, filename=filename, subtype=subtype)

		s = smtplib.SMTP('smtp.gmail.com', 587)

		s.starttls()
		if(email_add):
			s.login(email_add, pass_word)
		else :
			s.login(email,passd)
		s.send_message(msg)
		s.quit()

		flash('Email successfully sent to recepients')

		return render_template('emails.html', color='green',template1 = open('templates/template1.html').read())
	else:
		flash('Email subject, body and list of emails are required field')

		return render_template('emails.html', color='red',template1 = open('templates/template1.html').read())

@app.route('/fmail')
def fmail():
	return render_template('fake.html' , template1 = open('templates/template1.html').read())

@app.route('/fake', methods=['POST'])
def send_femail():
	subject = request.form['email-subject']
	body = request.form['email-body']
	emails = request.form['emails']
	email = 'fake334912@gmail.com'
	passd = 'Fake@3342'
	if subject and body and emails:

		msg = EmailMessage()

		asparagus_cid = make_msgid()

		msg['Subject'] = subject
		msg['From'] = email
		msg['To'] = (emails)

		msg.add_alternative(body.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

		if 'email-attachments[]' in request.files:
			files = request.files.getlist('email-attachments[]')

			for file in files:
				filename = secure_filename(file.filename)

				ctype = mimetypes.MimeTypes().guess_type(filename)[0]

				if ctype is None:
					ctype = 'application/octet-stream'

				maintype, subtype = ctype.split('/', 1)
				f_data = file.read()

				msg.add_attachment(f_data, maintype=maintype, filename=filename, subtype=subtype)

		s = smtplib.SMTP('smtp.gmail.com', 587)

		s.starttls()
		s.login(email,passd)
		s.send_message(msg)
		s.quit()

		flash('Email successfully sent to recepients')

		return render_template('fake.html', color='green' , template1 = open('templates/template1.html').read())
	else:
		flash('Email subject, body and list of emails are required field')

		return render_template('fake.html', color='red' , template1 = open('templates/template1.html').read() )


if __name__ == "__main__":
	app.run()
