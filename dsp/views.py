from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	context={}
	return render(request, 'dsp/home.html', context)

def resume(request):
	context={}
	return render(request, 'dsp/resume.html', context)

def davesdatadepot(request):
	context={}
	return render(request, 'dsp/davesdatadepot.html', context)

def pyython(request):
	context={}
	return render(request, 'dsp/pyython.html', context)

def etc(request):
	context={}
	return render(request, 'dsp/etc.html', context)

def contact(request):
	context={}
	return render(request, 'dsp/contact.html', context)

#individual projects
def mapping_mountains(request):
	context={}
	return render(request, 'dsp/Projects/mountainmapping.html', context)