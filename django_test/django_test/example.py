from django.http import HttpResponse


def world(request):
    return HttpResponse("Hello World")
