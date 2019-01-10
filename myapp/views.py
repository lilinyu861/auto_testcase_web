# Create your views here.
from django.shortcuts import render_to_response, render
from myapp.models import User


def index(request):
    return render_to_response('index.html', {"user_name": "lily"})


def user(request):
    str = User.objects.get(name='lily').user_email
    return render(request, 'user.html', {'str': str})