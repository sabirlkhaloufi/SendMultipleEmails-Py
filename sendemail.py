import imaplib
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# import pandas as pd


def fetch_email_signature(email_address, password):
    # Connect to the IMAP server (for Gmail)
    imap_server = 'imap.gmail.com'
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_address, password)
    except Exception as e:
        print("Failed to connect to the IMAP server.")
        print(e)
        return ''

    # Select the inbox and search for the latest email to fetch the signature
    mail.select('inbox')
    status, response = mail.search(None, 'ALL')
    message_ids = response[0].split()

    if message_ids:
        latest_email_id = message_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        signature = ''
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if 'text/plain' in content_type:
                    signature = part.get_payload(decode=True).decode()
                    break
        else:
            signature = msg.get_payload(decode=True).decode()

        return signature.strip()

    # Close the connection
    mail.logout()
    return ''

def send_email(sender_email, sender_password, recipients, subject, body, cv_file):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate port for your SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
    except Exception as e:
        print("Failed to connect to the SMTP server.")
        print(e)
        return


    for email in recipients:

        # Prepare the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject

        # Attach the CV file
        with open(cv_file, 'rb') as file:
            cv_content = file.read()
        cv_part = MIMEApplication(cv_content)
        cv_part.add_header('Content-Disposition', 'attachment', filename=cv_file)
        msg.attach(cv_part)

        # Add the email body
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            server.sendmail(sender_email, email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print("Failed to send the email.")
            print(e)

    # Close the SMTP server
    server.quit()

if __name__ == '__main__':
    # Replace the following variables with your email and password
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'
    
    subject = ' Your Email Subject ' #example : 'Candidature Développeur Full Stack Web / Mobile'
    body ='Your Email Body'          #example : 'Cher responsable du recrutement,\n\nJe souhaite postuler en tant que Développeur Full Stack Web ou Développeur Mobile dans votre entreprise

    # Replace with the filename of your CV in the same directory or provide the full path
    cv_file = 'your_cv.pdf'          #example : C:/Users/../Desktop/SendMultipleEmails-Py/cv.pdf

    # Example usage
    file_path = "C:/Users/.../Desktop/SendMultipleEmails-Py/emails.txt"  #example : C:/Users/.../Desktop/SendMultipleEmails-Py/emails.txt

    def read_text_file(file_path):
        try:
            with open(file_path, 'r') as file:
                # Read the lines from the text file and store them in a list
                lines = file.readlines()

                # Strip any leading/trailing whitespace or newline characters from each line
                lines = [line.strip() for line in lines]

                return lines
        except Exception as e:
            print("Error: ", e)
            return None


    result_array = read_text_file(file_path)
    send_email(sender_email, sender_password, result_array, subject, body, cv_file)

    
