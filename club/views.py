from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("hello, 4Her. You're at the club index")
