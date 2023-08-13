import re
from .models import CommentForm

def validate_username(user_name):
    if len(user_name) <= 256 and re.match(r'^[a-zA-Z0-9]+$', user_name):
        return True

def validate_email(email):
    if len(email) <= 50:
        return True

def remove_duplicates(comment_list=None, filtered_data=None):
    if (comment_list and filtered_data) is None:
            comment_list = []
            filtered_data = []

    comments = CommentForm.objects.all()
    for comment in comments:
        comment_data = {
            'parent_comment_id': comment.parent_comment_id,
            'id': comment.id,
            'user_name': comment.user_name,
        }
        comment_list.append(comment_data)


    # for item in comment_list:
    #     if item['parent_comment_id'] is None:
    #         filtered_data.append(item)
    return comment_list
