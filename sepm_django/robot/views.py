from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Home Page</h1>')

def tours(request):
	return HttpResponse('<h1>Tours Page</h1>')
