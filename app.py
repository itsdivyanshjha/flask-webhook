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

    # Example details extracted from commit data
    commit = commit_data['head_commit'] if 'head_commit' in commit_data else {}
    author_name = commit.get('author', {}).get('name', 'Unknown')
    commit_message = commit.get('message', 'No commit message provided.')
    commit_url = commit.get('url', 'URL not provided')

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Commit to Main Branch"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"""
    New commit by {author_name} to the repository {commit_data.get('repository', {}).get('name', 'Unknown')}
    Commit Message: {commit_message}
    View Commit: {commit_url}
    """
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
