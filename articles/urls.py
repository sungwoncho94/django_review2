from django.urls import path, include
from . import views
# view 함수를 쓰기 위해서는 import해야함
# . -> 현재 어플리케이션으로부터  /  view함수를 import함

# 여러 앱에 'create'라는 이름의 url이 있을 수 있으니까 app_name을 지정해서 헷갈리지 않도록!
app_name = 'articles'

urlpatterns = [
    path('create', views.create, name='create'),
]

