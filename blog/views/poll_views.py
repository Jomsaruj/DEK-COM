from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required

from ..models import Poll, Choice, Vote
from ..models.id_code import IdCode
from ..models.id_code_manager import IdCodeManager


def create_poll(request):
    """Create the polll with the question."""
    topic = request.POST['poll topic']
    content = request.POST['poll content']
    poll = Poll(topic=topic, content=content, author=request.user, id_code=IdCodeManager.get_new_id())
    poll.save()
    for key in request.POST:
            if "choice" in key:
                choice_name = request.POST[key]
                color = request.POST['color'+key.replace('choice', '')]
                if choice_name.strip():  # If tag are empty string just ignore it.
                    choice = Choice(content=choice_name, id_code=IdCodeManager.get_new_id(), poll_id_code=poll.id_code, color=color)
                    choice.save()
                    poll.choices.add(choice)
                    poll.save()
    return poll


@login_required
def vote(request, choice_id_code):
    """Count the amount the vote for the poll."""
    choice = Choice.objects.get(id_code=choice_id_code)
    poll = Poll.objects.filter(id_code=choice.poll_id_code).first()
    vote = Vote.objects.filter(question=poll, voter=request.user).first()
    if vote:
        old_choice = vote.choice
        old_choice.votes -= 1
        old_choice.save()

        vote.choice = choice
        vote.save()

        choice.votes += 1
        choice.save()
    else:
        vote = Vote(choice=choice, question=poll, voter=request.user)
        vote.save()
        choice.votes += 1
        choice.save()
        for _choice in poll.get_choices():
            _choice.all_votes += 1
            _choice.save()
    return redirect(reverse('blog:blog-detail', args=[poll.id_code]))