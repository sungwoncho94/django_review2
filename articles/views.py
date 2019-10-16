from django.shortcuts import render


# 사용자가 아티클을 생성하기 위해 내용을 적을 수 있는 페이지
def create(request):
    if request.method == 'POST':
        # Article을 생성해 달라는 요청
        pass
    else: # 'GET'
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        return render(request, 'articles/create.html')


