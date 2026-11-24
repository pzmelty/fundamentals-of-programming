import re

# Returns sender email address
def email_sender(email):
    match = re.search(r'^From:\s*(.+)', email, re.MULTILINE)
    return match.group(1).strip() if match else ''


# Returns recipient email address
def email_recipient(email):
    match = re.search(r'^To:\s*(.+)', email, re.MULTILINE)
    return match.group(1).strip() if match else ''


# Returns email subject
def email_subject(email):
    match = re.search(r'^Subject:\s*(.+)', email, re.MULTILINE)
    return match.group(1).strip() if match else ''

# Returns email body
def email_body(email):
    match = re.search(r'\r?\n\r?\n(.*)', email, re.DOTALL)
    return match.group(1).strip() if match else ''