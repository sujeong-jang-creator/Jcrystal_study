from django.shortcuts import render

def total_distinguish(request):
    return render(request, 'iguessso_app/total_distinguish.html')

def detail_distinguish(request):
    return render(request, 'iguessso_app/detail_distinguish.html')
