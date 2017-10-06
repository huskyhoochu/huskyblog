from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request):
    """
    메인 페이지를
    """
    posts = Post.objects.order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def archive_list(request):
    """
    전체 게시글 리스트 페이지
    """
    arch_list = Post.objects.order_by('-published_date')
    paginator = Paginator(arch_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/archive_list.html', {'posts': posts})

def essay_list(request):
    """
    카테고리: 에세이 리스트 페이지
    """
    essay_list = Post.objects.filter(category__exact='1')
    paginator = Paginator(essay_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/essay_list.html', {'posts': posts})
