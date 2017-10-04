from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def post_list(request):
    posts = Post.objects.order_by('-published_date')
    context = {
        'posts' : posts
    }
    # return render(request, 'blog/post_list.html', context)
    return render(request, 'blog/post_list.html', context)
