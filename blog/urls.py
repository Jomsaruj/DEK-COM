from django.urls import path

from .views import *

app_name = 'blog'
urlpatterns = [
    path('', blog, name='blog-index'),
    path('create-blog/<blog_type>', create_blog, name='create-blog'),
    path('<blog_type>', filter_blog, name='filter-blog'),
    path('<id_code>/', blog_detail, name='blog-detail'),
    path('<post_id_code>/edit-blog/', edit_blog, name='edit-blog'),
    path('<post_id_code>/delete-blog/', delete_blog, name='delete-blog'),
    path('<post_id_code>/crete-comment', create_comment, name='create-comment'),
    path('<comment_id_code>/delete-comment', delete_comment, name='delete-comment'),
    path('<comment_id_code>/create-subcomment', create_subcomment, name='create-subcomment'),
    path('<comment_id_code>/choose-solution', choose_solution, name='choose-solution'),
    path('tag/<tag_name>', tag, name='tag'),
    path('poll/vote/<choice_id_code>',vote, name='vote'),
    path('like/<id>',like, name='like'),
    path('like/detail/<id>',like_detail, name='like-detail'),
    path('apply-job/<job_id_code>',apply_job, name='apply-job'),
]