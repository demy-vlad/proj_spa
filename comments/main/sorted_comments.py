# Sorted Comments
from django.shortcuts import render
from .models import CommentForm

class SortedComments:
    def sorted_comments_get_request(self, request):
        sort_by = request.GET.get('sort_by', 'created_at')
        order = request.GET.get('order', '-')

        if order == '-':
            sort_by = '-' + sort_by

        comments = CommentForm.objects.all().order_by(sort_by)

        context = {
            'comments': comments,
            'order': order,
        }

        return render(request, 'main/handler.html', context)


sorted_comments = SortedComments()