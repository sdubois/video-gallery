# Create your views here.
from django.http import HttpResponse

def main_page(request):
    output = u'''
    <html>
    <head><title>%s</title></head>
    <body>
    <h1>%s</h1><p>%s</p>
    </body>
    </html>
    ''' % (
    u'Video Gallery',
    u'Welcome to Video Gallery',
    u'Where you can upload and share videos!'
    )
    return HttpResponse(output)
