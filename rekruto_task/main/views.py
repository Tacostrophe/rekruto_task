from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        name = request.GET.get('name', 'Guest')
        message = request.GET.get('message', 'Your message could be here')
        return HttpResponse(f'Hello {name}! {message}!')
