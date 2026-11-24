
from emails import email_sender, email_recipient, email_subject, email_body

# Read email from file
with open('08-FileHandling/email.txt', 'r', encoding='utf-8') as file:
    email = file.read()

# Print email information
print('Sender:', email_sender(email))
print('Recipient:', email_recipient(email))
print('Subject:', email_subject(email))
print('Body:', email_body(email))