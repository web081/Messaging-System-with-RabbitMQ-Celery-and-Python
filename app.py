import os
import time
from flask import Flask, request, Response
from dotenv import load_dotenv
from celery import Celery
from celery_worker import make_celery
from flask_mail import Mail, Message

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Flask-Mail configuration for Gmail using SSL
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # Gmail SMTP SSL port
app.config['MAIL_USE_SSL'] = True  # Enable SSL encryption
app.config['MAIL_USERNAME'] = os.getenv('GMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('GMAIL_PASSWORD')

# Celery configuration
app.config['CELERY_BROKER_URL'] = os.getenv('CELERY_BROKER_URL')
app.config['CELERY_RESULT_BACKEND'] = os.getenv('CELERY_RESULT_BACKEND')

# Initialize Flask-Mail and Celery
mail = Mail(app)

celery = make_celery(app)

@celery.task(name='app.send_email')  # Register the task with a specific name
def send_email(receivermail):
    msg = Message("Stage 3 Test Email", sender=os.getenv('GMAIL_USER'), recipients=[receivermail])
    msg.body = "This is a test email for Task."

    try:
        # Simulate a delay of 10 seconds before sending email
        #time.sleep(10)

        with app.app_context():
            mail.send(msg)
        print(f"Sent email to {receivermail}")
    except Exception as e:
        print(f"Error sending email: {e}")

    return True  # Optionally, return a value indicating success

@app.route("/")
def handle_request():
    sendmail_param = request.args.get('sendmail')
    talktome_param = request.args.get('talktome')

    if sendmail_param:
        send_email.delay(sendmail_param)
        return f'Sending email to {sendmail_param}...'

    elif talktome_param is not None: 
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f'Logged at {current_time}\n'
        log_file = '/var/log/messaging_system.log'
        with open(log_file, 'a') as f:
            f.write(log_message)
        return 'Logging message...'

    else:
        return 'Stage 3 Task Messaging System!'

@app.route('/logs')
def get_log():
    try:
        with open('/var/log/messaging_system.log', 'r') as f:
            log_content = f.read()
        return Response(log_content, mimetype='text/plain')
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)