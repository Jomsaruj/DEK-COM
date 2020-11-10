from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog-index'),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('<int:post_id>/', views.blog_detail, name='blog-detail'),
    path('<int:post_id>/edit-blog/', views.edit_blog, name='edit-blog'),
    path('<int:post_id>/delete-blog/', views.delete_blog, name='delete-blog'),
    path('<comment_tag>/delete-comment', views.delete_comment, name='delete-comment'),
    path('<comment_tag>/create-subcomment', views.create_subcomment, name='create-subcomment'),
]