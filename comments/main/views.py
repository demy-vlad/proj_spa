from django.shortcuts import render, redirect
from .handlers import comment_handler
from .sorted_comments import sorted_comments

def index(request):
    if request.method == 'POST':
        return comment_handler.handle_post_request(request)
    else:
        return comment_handler.handle_get_request(request)
    
def handler(request):
    return sorted_comments.sorted_comments_get_request(request)