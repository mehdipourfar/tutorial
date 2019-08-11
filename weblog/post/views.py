from django.shortcuts import render

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
    pass
