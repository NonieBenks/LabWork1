from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
# Create your views here.

def show(request):
    return HttpResponse('<h3>This is Aplication4</h3>')
def Redirect(request):
    return HttpResponsePermanentRedirect('redirected/')
def redirected(request):
    return HttpResponse('You were redirected')

def html(request):
    render_html = """
    <html>
    <head>
        <title>TITLE</title>
    </head>
    <body>
        <h1>HTML!</h1>
    </body>
    </html>
    """
    return HttpResponse(render_html)

def render_html(request):
    list = [0, 232, 45, 123, 0, 4, 53423, 54, 23]
    context = {
        'text': 'TEXT!',
        'list': list,
        'name': 'Adam',
        'surname': "Smith",
        'coords': {
            'x': "x coords",
            'y': "y coords"
        }
    }
    return render(request, "index.html", context)
def postmethod(request):
    if request.POST:
        return HttpResponse("This is method post")
    else:
        return HttpResponse('Get method!')