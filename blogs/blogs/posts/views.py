from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': post})