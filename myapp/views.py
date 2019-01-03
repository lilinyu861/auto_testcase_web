# Create your views here.
from django.shortcuts import render_to_response, render
from myapp.models import Person


def index(request):
    return render_to_response('index.html', {"name": "lily"})


def user(request):
    str = Person.objects.get(name='lily').password
    return render(request, 'user.html', {'str': str})