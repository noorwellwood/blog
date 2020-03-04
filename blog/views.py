from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib import admin
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
import datetime

def admin(request):
    return render(request,admin.site.urls)

def post_home(request):
    daytime=(datetime.datetime.now()-datetime.datetime(2020,3,4)).days
    posts = Post.objects.filter(status='published')  # home-page所有文章显示
    post_news = Post.objects.filter(status='published')[:3]  # 最新文章筛选
    post_ranges = Post.objects.filter(status='published').order_by('-total_views')[:3]  # 点击排行文章筛选
    paginator = Paginator(posts, 5)  # 分页
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            posts = paginator.get_page(page)  # 以下为捕获异常
        except PageNotAnInteger:  # 如果请求的页数不是整数, 返回第一页。
            home_posts = paginator.get_page(1)
        except InvalidPage:  # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:  # 如果请求的页数不在合法的页数范围内，返回结果的最后一页
            posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post-list.html',({'posts':posts,'post_news':post_news,'post_ranges':post_ranges,'daytime':daytime}))

def post_list(request,slug=None):
    daytime=(datetime.datetime.now()-datetime.datetime(2020,3,4)).days
    posts = Post.objects.filter(status='published',slug__title=slug)  # list-page所有文章显示
    post_news = Post.objects.filter(status='published')[:3]  # 最新文章筛选
    post_ranges = Post.objects.filter(status='published').order_by('-total_views')[:3]  # 点击排行文章筛选
    paginator = Paginator(posts, 5)  # 分页
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            posts = paginator.get_page(page)  # 以下为捕获异常
        except PageNotAnInteger:  # 如果请求的页数不是整数, 返回第一页。
            home_posts = paginator.get_page(1)
        except InvalidPage:  # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:  # 如果请求的页数不在合法的页数范围内，返回结果的最后一页
            posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post-list.html',({'posts':posts,'post_news':post_news,'post_ranges':post_ranges,'daytime':daytime}))

def post_detail(request,id=None,):
    daytime=(datetime.datetime.now()-datetime.datetime(2020,3,4)).days 
    post_news = Post.objects.filter(status='published')[:3]  # 最新文章筛选
    post_ranges = Post.objects.filter(status='published').order_by('-total_views')[:3]  # 点击排行文章筛选
    post = get_object_or_404(Post, id=id)  # 文章详情，id为该文章的ID
    post.total_views += 1  # 浏览量统计，每点击该文章详情一次，就增1
    post.save(update_fields=['total_views'])  # 浏览量每次增加后，只保存浏览量，优化性能
    return render(request,'blog/post-detail.html',({'post':post,'post_news':post_news,'post_ranges':post_ranges,'daytime':daytime}))

# Create your views here.
