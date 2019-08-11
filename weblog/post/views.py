from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.filter(
        published=True
    )
    return render(
        request,
        'post/index.html',
        {'posts': posts}
    )

def detail(request, id):
    post = get_object_or_404(
        Post.objects.filter(published=True),
        id=id
    )
    return render(
        request,
        'post/detail.html',
        {'post': post}
    )
