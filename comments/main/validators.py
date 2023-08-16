import re
import bleach
from django.conf import settings
import os
from PIL import Image


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

def validate_file_size(file):
        file_extension = file.name.split('.')[-1].lower()
        if file_extension in 'txt':
            max_size = 100 * 1024  # 100 KB
            if file.size > max_size:
                return False

def validate_image_size(file):
    """
    Checks that the image size
    """
    file_extension = file.name.split('.')[-1].lower()
    if file_extension not in 'txt':
        img = Image.open(file)
        max_size = (320, 240)    
        if img.width > max_size[0] or img.height > max_size[1]:
            img.thumbnail(max_size)
            file_path = os.path.join(settings.MEDIA_ROOT, "uploads", file.name)
            img.save(file_path, quality=95)
            return file_path
    else:
        return file

def validate_format(file):
    """
    Checks that the validate format
    """
    try:
        allowed_extensions = ['jpg', 'png', 'gif', 'txt']
        file_extension = file.name.split('.')[-1].lower()
        if file_extension not in allowed_extensions:
            return False
    except AttributeError:
        pass