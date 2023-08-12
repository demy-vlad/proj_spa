import re


def validate_username(user_name):
    if len(user_name) <= 256 and re.match(r'^[a-zA-Z0-9]+$', user_name):
        return True
    return False

def validate_email(email):
    if len(email) <= 50:
        return True
    return False