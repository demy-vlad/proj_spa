import re
import bleach

def validate_username(user_name):
    """
    Checks if the username matches the given criteria
    """
    if len(user_name) <= 256 and re.match(r'^[a-zA-Z0-9]+$', user_name):
        return True

def validate_email(email):
    """
    Checks that an email address matches the given criteria
    """
    if len(email) <= 50:
        return True
    
def is_valid_html(text):
    """
    Checks that the passed HTML text contains only allowed tags
    """
    allowed_tags = [
        'a',
        'code',
        'i',
        'strong',
    ]
    cleaned_text = bleach.clean(text, tags=allowed_tags, strip=True)
    return cleaned_text == text