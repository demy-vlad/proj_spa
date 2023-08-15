from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import CommentForm
from loguru import logger
from .validators import *


class CommentHandler(object):
    def handle_post_request(self, request):
        """
        Handles a POST request to create a new comment
        """
        parent_comment_id = request.POST.get('parent_comment_id')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        home_page = request.POST.get('home_page')
        text = request.POST.get('text')
        file = request.FILES.get('file')

        if file == None:
            error_message = "Invalid file"
            return render(request, 'main/index.html', {'error_message': error_message})

        if validate_format(file) == False:
            error_message = "Invalid file format. Allowed formats: JPG, PNG, GIF."
            return render(request, 'main/index.html', {'error_message': error_message})   

        if validate_file_size(file) == False:
            error_message = "File size exceeds the maximum limit of 100 KB."
            return render(request, 'main/index.html', {'error_message': error_message})    

        if not validate_username(user_name):
            error_message = "Invalid username"
            return render(request, 'main/index.html', {'error_message': error_message})

        if not validate_email(email):
            error_message = "Invalid email address"
            return render(request, 'main/index.html', {'error_message': error_message})
        
        if not is_valid_html(text):
            error_message = "Invalid HTML text format"
            return render(request, 'main/index.html', {'error_message': error_message})

        parent_comment = None
        if parent_comment_id:
            try:
                parent_comment = CommentForm.objects.get(id=parent_comment_id)
            except CommentForm.DoesNotExist as error:
                logger.error(error)
        
        self.create_comment(user_name, email, home_page, text, parent_comment, validate_image_size(file))
        return redirect('index')

    def create_comment(self, user_name, email, home_page, text, parent_comment, file):
        """
        Creates a new CommentForm object
        """
        comment_form = CommentForm(
            user_name=user_name,
            email=email,
            home_page=home_page,
            text=text,
            parent_comment=parent_comment,
            file=file
    )
        comment_form.save()

    def get_all_comments(self):
        """
        Gets all comments
        """
        return CommentForm.objects.filter(parent_comment__isnull=True).order_by('-created_at')

    def handle_get_request(self, request):
        """
        Handles a GET request to display a list of comments.
        Pagination for 25 posts.
        """
        comment_list = self.get_all_comments()
        if not comment_list:
            return render(request, 'main/no_comments.html')

        paginator = Paginator(comment_list, 25) 
        page_number = request.GET.get('page')
        response = {
            'comment_forms': paginator.get_page(page_number)
        }
        return render(request, 'main/index.html', response)

comment_handler = CommentHandler()