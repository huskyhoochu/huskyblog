from django.conf import settings
from django.db import models

class Post(models.Model):
    """
    Post 모델을 정의한다
    1. 글쓴이 (author)
    2. 제목 (title)
    3. 내용 (content)
    4. 생성일 (created_date)
    5. 게시일 (published_date)
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('blog.Category', blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    Category 모델을 정의한다
    1. 제목 (title)
    """
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
