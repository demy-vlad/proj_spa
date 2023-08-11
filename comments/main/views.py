from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import CommentForm

def index(request):
    if request.method == 'POST':
        return handle_post_request(request)
    else:
        return handle_get_request(request)

def handle_post_request(request):
    parent_comment_id = request.POST.get('parent_comment_id')
    user_name = request.POST.get('user_name')
    email = request.POST.get('email')
    home_page = request.POST.get('home_page')
    text = request.POST.get('text')
    
    if not (user_name and email and text):
        error_message = "All fields are required."
        return render(request, 'main/index.html', {'error_message': error_message})

    parent_comment = None
    if parent_comment_id:
        parent_comment = CommentForm.objects.get(id=parent_comment_id)

    comment_form = CommentForm(user_name=user_name, email=email, home_page=home_page, text=text, parent_comment=parent_comment)
    comment_form.save()

    return redirect('index')

def handle_get_request(request):
    comment_list = CommentForm.objects.all()
    paginator = Paginator(comment_list, 2)  # Количество записей на одной странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/index.html', {'comment_forms': page_obj})
