import re

def validate_emails(email_list):
    valid_emails = []
    pattern = re.compile(r"^[a-zA-Z0-9_.+-][a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    for email in email_list:
        if pattern.match(email):
            valid_emails.append(email)
    return valid_emails
