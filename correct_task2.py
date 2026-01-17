import re

def count_valid_emails(emails):
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    valid_email_count = 0

    for email in emails:
        if isinstance(email, str) and email_pattern.match(email):
            valid_email_count += 1

    return valid_email_count


