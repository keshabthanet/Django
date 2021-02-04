from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'app/index.html')
    # return HttpResponse("<h1 >Hello<br> Welcome to Keshab World</h1>")

def about(request):
    return render(request,'app/about.html')

def password(request):
    character=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))
    if request.GET.get('specials'):
        character.extend(list('!?@#%^&*'))
    newpsw= ''
    for x in range(length):
        newpsw+=random.choice(character)
        
    return render(request,'app/password.html',{'password':newpsw})

    # return HttpResponse("egg is <b>teasty</b> for eating")

   
