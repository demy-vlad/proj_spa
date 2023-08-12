from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import CommentForm
from .validators import validate_username, validate_email

class CommentHandler:
    def handle_post_request(self, request):
        parent_comment_id = request.POST.get('parent_comment_id')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        home_page = request.POST.get('home_page')
        text = request.POST.get('text')

        if not self.validate_input(user_name, email, text):
            error_message = "Все поля обязательны для заполнения. (user_name, email, text)"
            return render(request, 'main/index.html', {'error_message': error_message})

        if not validate_username(user_name):
            error_message = "Неверное имя пользователя."
            return render(request, 'main/index.html', {'error_message': error_message})

        if not validate_email(email):
            error_message = "Неверный адрес электронной почты."
            return render(request, 'main/index.html', {'error_message': error_message})

        comment_form = self.create_comment(user_name, email, home_page, text, self.get_parent_comment(parent_comment_id))
        self.save_comment(comment_form)
        
        return redirect('index')

    def validate_input(self, user_name, email, text):
        return user_name and email and text

    def create_comment(self, user_name, email, home_page, text, parent_comment):
        return CommentForm(
            user_name=user_name, 
            email=email, 
            home_page=home_page, 
            text=text, 
            parent_comment=parent_comment,
        )

    def get_parent_comment(self, parent_comment_id):
        if parent_comment_id:
            return CommentForm.objects.get(id=parent_comment_id)
        return None

    def save_comment(self, comment_form):
        comment_form.save()

    def handle_get_request(self, request):
        comment_list = CommentForm.objects.all()
        paginator = Paginator(comment_list, 2) 

        page_number = request.GET.get('page')
        response = {
            'comment_forms': paginator.get_page(page_number)
        }
        return render(request, 'main/index.html', response)

comment_handler = CommentHandler()

def index(request):
    if request.method == 'POST':
        return comment_handler.handle_post_request(request)
    else:
        return comment_handler.handle_get_request(request)
