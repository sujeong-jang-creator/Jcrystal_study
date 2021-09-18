from django.shortcuts import render,redirect,get_object_or_404
from .models import Write
from .forms import WriteForm

def home(request):
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('index') # 글 쓰고 인덱스로 감
    else:
        create_form = WriteForm()
    return render(request,'create.html',{'create_form':create_form})

def index(request):
    all_write = Write.objects.all()
    return render(request, 'index.html',{'all_write':all_write})
