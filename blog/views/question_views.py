from ..models import Question
from ..models.id_code import IdCode
from ..models.id_code_manager import IdCodeManager


def create_question(request):
    """Create the qustion for DEK_COM site."""
    topic = request.POST['post topic']
    content = request.POST['post content']
    question = Question(topic=topic, content=content, author=request.user, id_code=IdCodeManager.get_new_id())
    print("Genarated code for question")
    question.save()
    return question
