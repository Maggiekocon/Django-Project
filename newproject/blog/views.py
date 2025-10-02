from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    sentence = "This is the first Django view thing"
    header = 'HEADER'
    
    return render(request, 'index.html',{"sentence": sentence,"mywords": header} )

def show_post(request):
    # collect all objects from Post model and sort created at date
    post = Post.objects.order_by('title') 
    return render(request, 'post_list.html',{'post':post})

def add_post(request):
    blogform= PostForm()
    if request.method == 'POST':
        blogform = PostForm(request.POST)
        if blogform.is_valid():
            blogform.save()
            return redirect("post")
    return render(request, "post_form.html", {'blogform':blogform})

# filter post based on id

def find_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_detail.html", {"post":post})

# create an update view

def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    blogform = PostForm(instance=post)
    if request.method == 'POST':
        blogform = PostForm(request.POST, instance=post)
        if blogform.is_valid():
            blogform.save()
            return redirect("post")
    return render(request, "post_form.html", {'blogform':blogform})



def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("post")
