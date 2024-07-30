# Flask Webhook Email Notifier

## Overview

### What are Webhooks?

Webhooks are automated messages sent from apps when something happens. They have a message—or payload—and are sent to a unique URL, essentially an app’s phone number or address. Webhooks are used to connect two different applications and allow them to communicate with each other in real-time.

For example, when a new commit is made to a GitHub repository, GitHub can automatically send a notification (via a webhook) to another system to inform it of the new commit.

## Project Description

This project is a Flask application designed to listen to webhook notifications from GitHub. When a new commit is pushed to a specific branch of a GitHub repository, GitHub sends a webhook to this Flask application, which then processes the data and sends an email notification with details about the commit.

### How It Works

1. **Receiving Webhooks:**
   - The application exposes an endpoint (`/webhook`) that GitHub calls when a commit is made.
   - This endpoint accepts POST requests containing JSON data about the commit.

2. **Processing Data:**
   - Upon receiving a webhook notification, the application extracts relevant data from the payload, such as the commit message, author, and URL to the commit.

3. **Sending Email Notifications:**
   - Using the extracted data, the application constructs an email and sends it to a specified email address, providing a summary of the new commit.

### Usage

This project can be used in various scenarios where it's crucial to be notified of changes to a codebase, such as:
- Continuous Integration/Continuous Deployment (CI/CD) pipelines.
- Project management tools that need to track changes in real-time.
- Automated backup systems that trigger backups in response to code changes.

## Deployment

This application is designed to be deployed on platforms like Vercel, which can handle Flask applications and expose them to the internet so that GitHub can send webhooks to it.

### Environment Variables

To run this project, you need to set the following environment variables:
- `SENDER_EMAIL`: The email address from which notifications are sent.
- `RECEIVER_EMAIL`: The email address to which notifications are sent.
- `EMAIL_PASSWORD`: The password for the sender's email account.

These variables can be set in the deployment environment configuration section on Vercel or any other hosting platform being used.

## Local Testing

To test this application locally:
1. Set up your environment variables in your local development environment.
2. Run the application:
   ```bash
   flask run --host=0.0.0.0 --port=8080
