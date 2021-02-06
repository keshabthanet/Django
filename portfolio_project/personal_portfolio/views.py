from django.shortcuts import render
from .models import post


# Create your views here.
def home(request):
    portfo=post.objects.all()
    return render(request,'personal_portfolio/home.html',{'profile':portfo})
