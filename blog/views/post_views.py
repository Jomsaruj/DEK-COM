from ..models import Post
from django.utils import timezone

from ..models.id_code import IdCode
from ..models.id_code_manager import IdCodeManager


def create_post(request):
    topic = request.POST['post topic']
    content = request.POST['post content']
    post = Post(topic=topic, content=content, author=request.user, id_code=IdCodeManager.get_new_id())
    print("Genarated code for post")
    post.save()
    return post

def edit_post(request, blog):
    blog.topic = request.POST['post topic']
    blog.content = request.POST['post content']
    blog.pub_date = timezone.now()
    blog.save()