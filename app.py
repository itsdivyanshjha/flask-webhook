from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    send_email(data)
    return jsonify({'status': 'success'}), 200

def send_email(commit_data):
    sender_email = "jhadivyansh29@gmail.com"
    receiver_email = "jhadivyansh29@gmail.com"
    password = "ooqx kxug dggr wqyn"

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Commit to Main Branch"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"New commit by {commit_data['pusher']['name']} to the repository {commit_data['repository']['name']}"
    part = MIMEText(text, "plain")
    message.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
