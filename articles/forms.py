from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):
    # articleform에 대한 meta data 들이 작성되는 곳
    # meta data = 입력받을 데이터에 대한 부가적인 데이터
    class Meta:
        # 어느 model의 form인지 정의해줄 수 있음
        model = Article
        fields = '__all__'

