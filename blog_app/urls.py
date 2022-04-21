"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_app import views, generic_views

urlpatterns = [
    path('druga/', views.IndexView2.as_view(), name='index2'),
    path('add_blog/', views.AddBlogView.as_view(), name='add_blog'),
    path('show_blogs/', views.ShowBlogView.as_view(), name='show_blogs'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('show_post/', views.ShowPostView.as_view(), name='show_post'),
    path('blog/<int:id>/', views.ShowDetailBlog.as_view(), name='show_detail_blog'),
    path('post/<int:id>/', views.ShowDetailPost.as_view(), name='show_detail_post'),
    path('add_comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('comments/<int:id>/', views.CommentsView.as_view(), name='comments'),
    path('update_post/<int:id>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:id>/', views.DeletePostView.as_view(), name='delete_post'),
    path('create_post_generic_view/', generic_views.CreatePostView.as_view(), name='gen_post_create_view'),
    path('dpv_gen/<int:pk>/', generic_views.DetailPostVIew.as_view(), name='det_post_view_gen'),
]
