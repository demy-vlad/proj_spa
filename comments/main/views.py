from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import CommentForm
from .validators import *



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
    
    """У меня есть два способо добавь валидацию. 
    Первый с помощью ифов, второй общий иф общий 
    который должен вернуть всё True"""

    if not (user_name and email and text):
        error_message = "Все поля обязательны для заполнения. (user_name, email, text)"
        return render(request, 'main/index.html', {'error_message': error_message})
    elif not validate_username(user_name):
        error_message = "Неверное имя пользователя."
        return render(request, 'main/index.html', {'error_message': error_message})
    elif not validate_email(email):
        error_message = "Неверный адрес электронной почты."
        return render(request, 'main/index.html', {'error_message': error_message})
    else:
        comment_form = create_comment(
        user_name,
        email,
        home_page,
        text,
        get_parent_comment(parent_comment_id),
    )
    save_comment(comment_form)


    # # Второй способ
    # if (
    #     validate_username(user_name)
    #     and validate_email(email)
    # ):
    #     comment_form = create_comment(
    #         user_name,
    #         email,
    #         home_page,
    #         text,
    #         get_parent_comment(parent_comment_id),
    #     )
    #     save_comment(comment_form)
    # else:
    #     error_message = "Все поля обязательны для заполнения."
    #     return render(request, 'main/index.html', {'error_message': error_message})
    return redirect('index')

def create_comment(
        user_name, 
        email, 
        home_page, 
        text, 
        parent_comment
        ):
    return CommentForm(
        user_name=user_name, 
        email=email, 
        home_page=home_page, 
        text=text, 
        parent_comment=parent_comment,
    )

def get_parent_comment(parent_comment_id):
    if parent_comment_id:
        return CommentForm.objects.get(id=parent_comment_id)
    return None

def save_comment(comment_form):
    comment_form.save()

def handle_get_request(request):
    comment_list = CommentForm.objects.all()
    paginator = Paginator(comment_list, 2) 

    page_number = request.GET.get('page')
    response = {
        'comment_forms': paginator.get_page(page_number)
    }
    return render(request, 'main/index.html', response)