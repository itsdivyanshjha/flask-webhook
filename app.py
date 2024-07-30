from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask webhook listener is running."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        send_email(data)
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'No data received'}), 400

def send_email(commit_data):
    sender_email = os.getenv("SENDER_EMAIL", "jhadivyansh29@gmail.com")
    receiver_email = os.getenv("RECEIVER_EMAIL", "jhadivyansh29@gmail.com")
    password = os.getenv("EMAIL_PASSWORD", "ooqx kxug dggr wqyn")

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Commit to Main Branch"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Assuming 'pusher' and 'name' keys exist in the commit data
    text = f"New commit by {commit_data.get('pusher', {}).get('name', 'Unknown')} to the repository {commit_data.get('repository', {}).get('name', 'Unknown')}"
    part = MIMEText(text, "plain")
    message.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
