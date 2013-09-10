import os
import re
from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
from config import SENDER

app = Flask(__name__)
app.config.from_object('config')

mailService = Mail(app)

@app.route('/')
def main():
	return render_template('index.html');

@app.route('/mail', methods=['POST'])
def mail():
	newMail = request.form['email'];
	newName = request.form['name'];

	if (validate_email(newMail)):
		send_email("[NewCustomer] "+newMail, SENDER[0], SENDER, 
					render_template("basicEmail.txt" , email = newMail , name = newName),
        			render_template("basicEmail.html", email = newMail , name = newName))
		return redirect(url_for('email_sent'))

	return redirect(url_for('main'))
	
@app.route('/emailSent')
def email_sent():
	return render_template('emailSent.html');

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    mailService.send(msg)	

def validate_email(email):
	if len(email) > 7:
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
			return 1
	return 0 
