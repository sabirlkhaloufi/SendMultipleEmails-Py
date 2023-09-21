# send-multiple-emails-Python

This Python script allows you to fetch an email signature and send emails with attachments using Gmail as the email provider. It can be useful for tasks like sending job applications with a CV attached.

# Prerequisites

Before using this script, make sure you have the following:

1. Python installed on your system.
2. Gmail account credentials (email address and password).
3. A CV file (PDF, Word document, etc.) that you want to attach to your emails.
4. A list of recipient email addresses in a text file (one email address per line).

## Installation

1. Clone this repository to your local machine.

2. Install the required Python libraries using pip:

   
```bash
   pip install imaplib email smtplib
```

# Usage
## To use this script, follow these steps:

1. Open the script file (email_automation.py) in a text editor.
2. Replace the following variables with your Gmail account credentials:

```bash
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'
```
3. Customize the email subject and body to your needs:
```bash
    subject = 'Your Email Subject'
    body = 'Your Email Body'
 ```
4. Replace the cv_file variable with the filename of your CV. Make sure the CV file is in the same directory as the script, or provide the full file path:

```bash
    cv_file = 'your_cv.pdf'
```
5. Create a text file (emails.txt) containing the list of recipient email addresses (one email address per line).
6. Replace the file_path variable with the path to your emails.txt file:

```bash
    file_path = 'emails.txt'
```

7. Save your changes.
8. Run the script in your terminal:

```bash
    python sendemail.py
```

The script will read the recipient email addresses from the emails.txt file, send emails to each recipient with your CV attached, and print a success message for each email sent.
