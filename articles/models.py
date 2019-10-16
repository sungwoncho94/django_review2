from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()  # 뒤 괄호() 필수
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-pk', )