from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour, Locations

def home(request):
	return render(request, 'robot/home.html')

def tours(request):
	context = {
		'tour_planner': Tour.objects.all()
	}
	return render(request, 'robot/tours.html', context)

def locations(request):
	context = {
		'location_identify': Locations.objects.all()
	}
	return render(request, 'robot/locations.html', context)