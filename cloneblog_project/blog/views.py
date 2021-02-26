from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import PostForm,CommentForm
from .models import Post
from django.db import Error
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    post=Post.objects.order_by('-created_date')
    return render(request,'blog/home.html',{'post':post})
def current(request):
    post=Post.objects.all()
    return render(request,'blog/current.html',{'post':post})


# def signupuser(request):
#     if request.method=="GET":
#         return render(request,'blog/signupuser.html',{'form':UserCreationForm()})
#     else:
#         if request.POST["password1"] == request.POST["password2"]:
#             user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
#             user.save()
#             login(request,user)
#             return redirect('home')
def loginuser(request):
    if request.method=="GET":
        return render(request,'blog/loginuser.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user  is None:
            return render(request,'blog/loginuser.html',{'form':AuthenticationForm(),'error':'username n password sidnot match'})

        else:
            login(request,user)

            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

@login_required
def createpost(request):
    if request.method=="GET":
        return render(request,'blog/createpost.html',{'postform':PostForm()})
    else:
        try:
            postform=PostForm(request.POST)
            newtodoform=postform.save(commit=False)
            newtodoform.user=request.user
            newtodoform.save()
            return redirect('home')
        except Error:
            return render(request,'blog/createpost.html',{'postform':PostForm(),'error':'Bad data for the creating todo'})


def viewpost(request,blog_id):
    post=get_object_or_404(Post,pk=blog_id)
    if request.method=="GET":
        todoform=PostForm(instance= post)
        return render(request,'blog/viewpost.html',{'post':post,'postform':todoform})
    else:
        try:
            todoform=PostForm(request.POST,instance=post)
            todoform.save()
            return redirect('home')
        except ValueError:
            return render(request,'blog/viewpost.html',{'post':post,'postform':todoform,'error':'Bad information'})


# def viewmypost(request,blog_id):
#     post=get_object_or_404(Post,pk=blog_id)
#     return render(request,'blog/viewmypost.html',{'post':post})
@login_required
def deletepost(request,blog_id):
    post=get_object_or_404(Post,pk=blog_id)
    if request.method=="POST":
        post.delete()
        return redirect('home')
def about(request):
    return render(request,'blog/about.html')



def add_comment_to_post(request,blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {'form': form})
