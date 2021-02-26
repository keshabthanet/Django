from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    names=request.GET.get('search')
    return render(request,'find/home.html',{'name':names})
def add(request):
    if request.method == "POST":
        names=request.GET.get('search')
        names.save()
        names=Post.objects.al()
