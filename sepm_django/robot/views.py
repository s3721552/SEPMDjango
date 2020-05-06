from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour

def home(request):
	context = {
		'tour_planner': Tour.objects.all()
	}
	return render(request, 'robot/home.html', context)

def tours(request):
	return render(request, 'robot/tours.html', {'title': 'Tours'})