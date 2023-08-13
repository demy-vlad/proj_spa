# models.py
from django.db import models

class CommentForm(models.Model):
    user_name = models.CharField("User name", max_length=100)
    email = models.EmailField("E-mail", max_length=50)
    home_page = models.URLField("Home page", blank=True)
    text = models.TextField("Text", max_length=300)
    created_at = models.DateTimeField("Date", auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_at']
