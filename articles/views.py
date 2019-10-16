from django.shortcuts import render, redirect, get_object_or_404  # redirect = 어느 페이지로 이동시킴
from .forms import ArticleForm
from django.views.decorators.http import require_GET, require_POST
from .models import Article
from IPython import embed

@require_GET
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


@require_GET
def detail(request, article_pk):
    # 사용자가 url에 적어보낸 article_pk를 통해 디테일 페이지를 보여준다  /  get_object_or_404 import
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


# 사용자가 아티클을 생성하기 위해 내용을 적을 수 있는 페이지
def create(request):
    if request.method == 'POST':
        # Article을 생성해 달라는 요청
        # data꺼내서 Article 생성
        
        form = ArticleForm(request.POST)
        embed()
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)

    else: # 'GET'
        form = ArticleForm()
        #     context = {'form': form}
        # return render(request, 'articles/create.html', context)

    context = {'form': form}
    # Article을 생성하기 위한 페이지를 달라고 하는 요청
    return render(request, 'articles/create.html', context)


def update(request, article_pk):
    # article이 있는지 없는지 먼저 확인, 없으면 404페이지 반환
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # 기존의 instance에 새로 받은 내용을 추가할 것.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    # get method로 들어왔을 때에는 update.html render해서 보여주기
    else:
        # form을 작성할 때 그 안에 특정 instance data를 넣어놓겠다는 뜻
        form = ArticleForm(instance=article)
        context = {'form': form}
        return render(request, 'articles/update.html', context)


@require_POST
def delete(request, article_pk):
    # article_pk에 맞는 article을 꺼낸다.
    article = get_object_or_404(Article, pk=article_pk)
    # if POST요청으로 왔을때만, 삭제한다

    article.delete()
    # 목록으로 돌려보내준다
    return redirect('articles:index')