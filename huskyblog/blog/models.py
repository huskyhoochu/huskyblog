from django.conf import settings
from django.db import models
from markdownx.models import MarkdownxField


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
    category = models.ForeignKey('blog.Category', blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    markdown = MarkdownxField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)


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

class Image(models.Model):
    """
    이미지 업로드
    related_name으로 역참조 키워드를 붙인다
    """
    post = models.ForeignKey(Post, related_name='posts')
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(blank=True, null=True, upload_to='./covers/%Y/%m')

    def __str__(self):
        return self.title

