from django.shortcuts import render, get_object_or_404
from .models import Post

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})
