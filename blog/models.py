from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

class Post_colum(models.Model):  #栏目的模型
    title = models.CharField(max_length=100,verbose_name='栏目名称')
    create = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')

    class Meta:
        ordering=('-create',)
        verbose_name='栏目'
        verbose_name_plural = "栏目"

    def __str__(self):
        return self.title

class Post(models.Model):  #文章的模型
    status_choices=(('draft','草稿'),('published','发布'))
    title=models.CharField(max_length=250,verbose_name='标题')
    slug=models.ForeignKey(Post_colum,on_delete=models.CASCADE,related_name='post_colum',verbose_name='栏目')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post',verbose_name='作者')
    body= RichTextUploadingField(verbose_name='正文')
    create=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    update=models.DateTimeField(auto_now=True,verbose_name='更新时间')
    status=models.CharField(max_length=20,choices=status_choices,default='draft',verbose_name='状态')
    objects=models.Manager()
    #image=models.ImageField(upload_to='post/%Y/%m/%d')
    tags=TaggableManager(blank=True,verbose_name='标签')
    total_views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering=('-create',)
        verbose_name='文章'
        verbose_name_plural = "文章"

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])

    def __str__(self):
        return self.title




# Create your models here.
