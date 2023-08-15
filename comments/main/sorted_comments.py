from django.shortcuts import render
from .handlers import CommentHandler

class SortedComments(object):
    def sorted_comments_get_request(self, request):
        """
        GET request handler for sorting comments
        """

        # Getting sort options from a GET request
        sort_by = request.GET.get('sort_by', 'created_at')
        order = request.GET.get('order', '-')

        # Checking if there are comments
        if not comment_handler.get_all_comments():
            return render(request, 'main/no_sorted_comments.html')

        # Apply sorting according to the specified parameters
        if order == '-':
            sort_by = '-' + sort_by

        # Remove duplicates and sort comments
        comments = self.remove_duplicates()
        comments_sorted = sorted(comments, key=lambda x: x.get(sort_by, ''), reverse=(order == 'desc'))

        context = {
            'comments': comments_sorted,
            'order': order,
        }
        
        return render(request, 'main/handler.html', context)

    def remove_duplicates(self):
        """
        Returns a list of unique comments with information about parent comments
        """
        comments = comment_handler.get_all_comments()
            
        comment_list = [{
            'parent_comment_id': comment.parent_comment_id,
            'id': comment.id,
            'user_name': comment.user_name,
            'email': comment.email,
            'created_at': comment.created_at,
            'text': comment.text,
        } for comment in comments]

        return comment_list

sorted_comments = SortedComments()
comment_handler = CommentHandler()