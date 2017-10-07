from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Image


def index(request):
    """
    메인 페이지를
    """
    posts = Post.objects.order_by('-published_date')
    images = Image.objects.order_by('-post')
    context = {
        'posts': posts,
        'images': images,
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
    essay_list = Post.objects.filter(category__exact='1').order_by('-published_date')
    paginator = Paginator(essay_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/category_list.html', {'posts': posts})

def review_list(request):
    """
    카테고리: 리뷰 리스트 페이지
    """
    review_list = Post.objects.filter(category__exact='2')
    paginator = Paginator(review_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/category_list.html', {'posts': posts})

def programming_list(request):
    """
    카테고리: 프로그래밍 리스트 페이지
    """
    programming_list = Post.objects.filter(category__exact='3')
    paginator = Paginator(programming_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/category_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    image = Image.objects.get(post__id=post.pk)
    context = {
        'post': post,
        'image': image,
    }
    return render(request, 'blog/post_detail.html', context)