from django.db import models

class CommentForm(models.Model):
    user_name = models.CharField("User name", max_length=100)
    email = models.EmailField("E-mail", max_length=50)
    home_page = models.URLField("Home page", blank=True)
    text = models.TextField("Text", max_length=300)
    created_at = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Comments"
        verbose_name_plural = "Comments"
        ordering = ['-user_name', '-email', '-created_at']
