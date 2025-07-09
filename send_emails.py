import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

import os
import json
import configparser
from datetime import datetime

def send_email(sender_email, sender_password, recipient_emails, subject, body, smtp_server, smtp_port=587, attachment=None):
    """
    Function to send an email using SMTP, with support for multiple recipients and optional attachment.

    Parameters:
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password or app-specific password.
        recipient_emails (list): List of recipient email addresses.
        subject (str): Subject of the email.
        body (str): Body content of the email.
        smtp_server (str): SMTP server address.
        smtp_port (int): Port number for the SMTP server.
        attachment (str): File path of the attachment (optional).
    """
    try:
        # Create the email object
        message = MIMEMultipart()
        # message['From'] = Header(sender_email, 'utf-8')
        message['From'] = "Daily ArXiv <jackyfl@daily_arxiv.com>"
        # message['To'] = Header(", ".join(recipient_emails), 'utf-8')  # Join recipient emails with commas
        message['To'] = "Undisclosed Recipients"  # hideen the recipient emails
        message['Subject'] = Header(subject, 'utf-8')

        # Attach the email body
        message.attach(MIMEText(body, 'html', 'utf-8'))

        # If there is an attachment, add it
        if attachment:
            try:
                with open(attachment, 'rb') as file:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file.read())
                print("encode attachment")
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{attachment.split("/")[-1]}"'
                )
                message.attach(part)
                
            except FileNotFoundError:
                print(f"Attachment not found: {attachment}")
                return

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable secure connection
        print("log in")
        server.login(sender_email, sender_password)
        
        # Send the email
        print("send email")
        server.sendmail(sender_email, recipient_emails, message.as_string())
        print(f"Email sent successfully to: {', '.join(recipient_emails)}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("configs/config.ini")

    today_str = datetime.today().strftime("%Y_%m%d")
    attachment_path = f"out/output_{today_str}.md"
    
    if os.path.exists(attachment_path):
        selected_papers = json.load(open("out/output.json"))
        # push to target emails
        if config["EMAIL"].getboolean("push_to_email"):
            email = config["EMAIL"]
            sender_email = email['send_email']        # sender email
            sender_password = os.environ.get("EMAIL_KEY") # sender passwd
            
            recipient_email_list = email['receive_emails'].split(', ')
            
            subject = f"Daily ArXiv: {datetime.today().strftime('%m/%d/%Y')}"
            paper_len = len(selected_papers)
    
            title_authors = ''
            for i, paper_id in enumerate(selected_papers):
                paper_entry = selected_papers[paper_id]
                title = paper_entry["title"]
                authors = paper_entry["authors"]
                authors = ", ".join(authors)
                title_authors += f"<p>{i}: <b>{title}</b>. {authors}. </p>"
                
            body = f"""
            <html>
                <body>
                    <p>Hi,</p>
                    <p><b>This is <a href="https://jackyfl.github.io/gpt_paper_assistant/"> Daily ArXiv</a>  😊😊😊 </b></p>
                    <p>There are <b>{paper_len}</b> relevant papers on <b>{datetime.today().strftime('%m/%d/%Y')}</b> 👇👇👇:</p>
                    <p> {title_authors} \n </p>
                    <p>Reading papers everyday, keep innocence away 🙌 </p>
                    <p> </p>
                    <p>Best, </p>
                    <p>Daily ArXiv </p>
                <body>
            </html>            
            """
            
            smtp_server = "smtp.gmail.com"                # SMTP server address, e.g., Gmail: smtp.gmail.com
            smtp_port = 587                                 # SMTP port, e.g., Gmail: 587

            # send emails
            send_email(sender_email, sender_password, recipient_email_list, subject, body, smtp_server, smtp_port, attachment=attachment_path)
