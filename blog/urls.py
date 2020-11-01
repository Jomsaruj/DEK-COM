from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog-index'),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('<int:post_id>/', views.blog_detail, name='blog-detail'),
]