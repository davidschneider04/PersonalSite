from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	context={}
	return render(request, 'dsp/home.html', context)