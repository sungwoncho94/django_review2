from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()  # 뒤 괄호() 필수
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-pk', )


class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
        max_length=50,
        validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
    )
    age = models.IntegerField(
        validators=[MinValueValidator(19, message='미성년자 ㄴㄴ')]
    )