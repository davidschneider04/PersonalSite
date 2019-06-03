from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	context={}
	return render(request, 'dsp/home.html', context)

def resume(request):
	context={}
	return render(request, 'dsp/resume.html', context)

#def davesdatadepot(request):
#	context={}
#	return render(request, 'dsp/davesdatadepot.html', {"context": context})

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
	return render(request, 'dsp/Projects/map.html', context)

def denver_zipcodes(request):
	context={}
	return render(request, 'dsp/Projects/denver_zipcodes.html', context)

def create_project(pname, purl, desc):
	return {'project':pname, 'reflink':purl, 'description': desc}

def davesdatadepot(request):
	projects = []
	#saywhen
	pname = "SayWhen-- Movie/TV Scene Finder"
	purl = "https://saywhen.app"
	desc = "Do you have a favorite line from a favorite TV show or movie, but don't remember what episode or time it's from? Let SayWhen find the exact spot and link you to it."
	project = create_project(pname, purl , desc)
	projects.append(project)
	#mapping mountains
	pname = "Mapping Colorado Mountains"
	purl = "http://davidschneiderprojects.com/davesdatadepot/mapping_mountains/"
	desc = "Using Python with Folium to create an interactive map of the 100 highest peaks in Colorado."
	project = create_project(pname, purl , desc)
	projects.append(project)
	#denver zipcodes
	pname = "Mapping & Modeling Denver Zipcodes"
	purl = "http://davidschneiderprojects.com/davesdatadepot/denver_zipcodes/"
	desc = "An exploratory project I did for a Coursera assignment. Using Python with Folium to plot restaurants, income, etc., zoned by ZCTA."
	project = create_project(pname, purl , desc)
	projects.append(project)
	return render(request, 'dsp/davesdatadepot.html', {"context": projects})