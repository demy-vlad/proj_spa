from django.shortcuts import render, redirect
from .handlers import comment_handler

def index(request):
    if request.method == 'POST':
        return comment_handler.handle_post_request(request)
    else:
        return comment_handler.handle_get_request(request)