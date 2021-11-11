from django.shortcuts import render
from .models import Results
from django.core.paginator import Paginator

def total_distinguish(request):
    return render(request, 'iguessso_app/total_distinguish.html')

def detail_distinguish(request):
    return render(request, 'iguessso_app/detail_distinguish.html')

def grade_table(request):
    result = Results.objects.all()
    # 페이지 처리 시작
    paginator = Paginator(result, 5)
    page = int(request.Get.get('page', 1))
    page_obj = paginator.page(page)
    # 페이지 처리 끝
    print(result)

    # response = render(request, "iguessso_app/total_distinguish.html",{"result":result})
    response = render(request, "iguessso_app/total_distinguish.html",{"page_obj":page_obj})
    return response