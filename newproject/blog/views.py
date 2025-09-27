from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    sentence = "This is the first Django view thing"
    header = 'HEADER'
    
    return render(request, 'index.html',{"sentence": sentence,"mywords": header} )

def show_post(request):
    post = Post.objects.all() 
    return render(request, 'post_list.html',{'post':post})
