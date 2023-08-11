from django.conf import settings
from django.shortcuts import render
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import CommentForm

def index(request):
    if request.method == 'POST':
        return handle_post_request(request)
    else:
        return handle_get_request(request)

def handle_post_request(request):
    user_name = request.POST.get('user_name')
    email = request.POST.get('email')
    home_page = request.POST.get('home_page')
    text = request.POST.get('text')
    
    if not (user_name and email and text):
        error_message = "All fields are required."
        return render(request, 'main/index.html', {'error_message': error_message})
    else:
        comment_form = CommentForm(user_name=user_name, email=email, home_page=home_page, text=text)
        comment_form.save()
    return redirect('index')

def handle_get_request(request):
    comment_forms = CommentForm.objects.all()
    return render(request, 'main/index.html', {'comment_forms': comment_forms})

