from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog-index'),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('<post_tag>/', views.blog_detail, name='blog-detail'),
    path('<post_tag>/edit-blog/', views.edit_blog, name='edit-blog'),
    path('<post_tag>/delete-blog/', views.delete_blog, name='delete-blog'),
    path('<post_tag>/crete-comment', views.create_comment, name='create-comment'),
    path('<comment_tag>/delete-comment', views.delete_comment, name='delete-comment'),
    path('<comment_tag>/create-subcomment', views.create_subcomment, name='create-subcomment'),
]