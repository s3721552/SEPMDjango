from django.shortcuts import render
from django.http import HttpResponse

tour_planner = [
	{
		'name_location': 'Bali',
		'xy_coordinates': '8 S, 115 E',
		'description': 'one stop trip(temporary)',
		'min_time_spent': '2 days'

	},
	{
		'name_location': 'Sydney',
		'xy_coordinates': '33 S, 151 E',
		'description': 'one stop trip(temporary)',
		'min_time_spent': '4 days'

	}
]

def home(request):
	context = {
		'tour_planner': tour_planner
	}
	return render(request, 'robot/home.html', context)

def tours(request):
	return render(request, 'robot/tours.html', {'title': 'Tours'})