from django.urls import path
from django.contrib import admin
from . import views

app_name='blog'

urlpatterns=[
    path('admin/',views.admin,name='admin'),
    path('',views.post_home,name='post_home'),
    path('post/<int:id>',views.post_detail,name='post_detail'),
    path('slug/<str:slug>',views.post_list,name='post_list'),
    ]