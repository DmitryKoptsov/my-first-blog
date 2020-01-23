from django.urls import path
from . import views

urlpatterns = [
#    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/<int:pk>/post_new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blog/new/', views.blog_new, name='blog_new'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('comment/<int:pk>/edit', views.comment_edit, name='comment_edit'),

]