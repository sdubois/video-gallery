# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
            'head_title': u'Video Gallery',
            'page_title': u'Welcome to Video Gallery',
            'page_body': u'Where you can upload videos',
            'user': request.user
    })
    output = template.render(variables)
    return HttpResponse(output)

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
    videos = user.video_set.all()
    template = get_template('user_page.html')
    variables = Context({
            'username': username,
            'videos': videos
    })
    output = template.render(variables)
    return HttpResponse(output)
