from django.shortcuts import render, redirect,reverse

from ..models import Tag


def tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
    except:
        return redirect(reverse('blog:blog-index'))
    try:
        latest_url = request.META.get('HTTP_REFERER').split('/')
        if latest_url[-2] != 'blog':
            tag.active_status = True
        else:
            tag.active_status = not tag.active_status
    except:
        tag.active_status = not tag.active_status
    tag.save()
    try:  # get previous url and redirect to that url
        type = request.META.get('HTTP_REFERER').split('/')[-1]
        # print(request.META.get('HTTP_REFERER'))
        # print(type)

        if type in ['post', 'question', 'poll', 'job']:
            return redirect(reverse('blog:filter-blog', args=[type]))
        else:  # not from index
            return redirect(reverse('blog:blog-index'))
    except:
        # print("from other site")
        pass
    return redirect(reverse('blog:blog-index'))