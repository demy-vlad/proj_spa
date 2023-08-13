from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .validators import validate_email, validate_username
from .models import CommentForm

class CommentHandler:
    
    def handle_post_request(self, request):
        parent_comment_id = request.POST.get('parent_comment_id')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        home_page = request.POST.get('home_page')
        text = request.POST.get('text')

        if not self.validate_input(user_name, email, text):
            error_message = "All fields are required. (user_name, email, text)"
            return render(request, 'main/index.html', {'error_message': error_message})

        if not validate_username(user_name):
            error_message = "Invalid username."
            return render(request, 'main/index.html', {'error_message': error_message})

        if not validate_email(email):
            error_message = "Invalid email address."
            return render(request, 'main/index.html', {'error_message': error_message})

        parent_comment = None
        if parent_comment_id:
            try:
                parent_comment = CommentForm.objects.get(id=parent_comment_id)
            except CommentForm.DoesNotExist:
                pass

        comment_form = self.create_comment(
            user_name,
            email,
            home_page,
            text,
            parent_comment
        )
        self.save_comment(comment_form)

        return redirect('index')

    def validate_input(self, user_name, email, text):
        return user_name and email and text

    def  validate_email(self, email):
        return validate_email(email)
    
    def validate_username(self, email):
        return validate_username(email)

    def create_comment(self, user_name, email, home_page, text, parent_comment):
        return CommentForm(
            user_name=user_name, 
            email=email, 
            home_page=home_page, 
            text=text, 
            parent_comment=parent_comment,
        )

    def save_comment(self, comment_form):
        comment_form.save()

    def get_all_comments(self):
        return CommentForm.objects.filter(parent_comment__isnull=True).order_by('-created_at')

    def handle_get_request(self, request):
        comment_list = self.get_all_comments()
        paginator = Paginator(comment_list, 25) 
        page_number = request.GET.get('page')
        response = {
            'comment_forms': paginator.get_page(page_number)
        }
        return render(request, 'main/index.html', response)

comment_handler = CommentHandler()