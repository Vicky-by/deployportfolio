import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', '587'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv(
    'MAIL_DEFAULT_SENDER',
    app.config['MAIL_USERNAME'],
)
app.config['CONTACT_RECIPIENT'] = os.getenv(
    'CONTACT_RECIPIENT',
    'vikkikumar9694@gmail.com',
)

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('index.html')

    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    message = request.form.get('message')

    if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
        return render_template('thank_you.html', success=False), 500

    msg = Message(
        subject="New Contact Form Submission",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[app.config['CONTACT_RECIPIENT']],
    )
    msg.body = f"""
New Contact Form Submission:

Name: {name}
Email: {email}
Service: {service}
Message: {message}
""".strip()
    msg.reply_to = email

    mail.send(msg)

    return render_template('thank_you.html', success=True)


if __name__ == '__main__':
    app.run(debug=True)
