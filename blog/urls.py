from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog-blog'),
    path('blog/', views.blog, name='blog-blog'),
    path('blog/blog/', views.blog, name='blog-blog'),
    path('about/', views.about, name='blog-about')
]