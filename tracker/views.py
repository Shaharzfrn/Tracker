from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request.user.is_authenticated)
	return render(request, "home.html", {'img': 'img/face.jpg'})

def tasks_view(request, *args, **kwargs):
	print(request.user.is_authenticated)
	return render(request, "home.html", {'img': 'img/face.jpg'})