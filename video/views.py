from django.http import HttpResponse

def main_page(request):
    ouput = u'''
        <html>
            <head><title>%s</title></head>
            <body>
                <h1>%s</h1><p>%s</p>
            </body>
        </html>
    ''' % ( u'CSH RedTube', u'Welcome to CSH red tube', u'Where you can view videos until your eyes fall out')
    return HttpResponse(output)