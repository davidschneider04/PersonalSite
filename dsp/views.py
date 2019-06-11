from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	context={}
	return render(request, 'dsp/home.html', context)

def resume(request):
	context={}
	return render(request, 'dsp/resume.html', context)

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

def denver_zipcodes(request):
	context={}
	return render(request, 'dsp/Projects/denver_zipcodes.html', context)

def resume_from_plaintext(request):
	context={}
	return render(request, 'dsp/Projects/resume_from_plaintext.html', context)

def alteryx_creations(request):
	context={}
	return render(request, 'dsp/Projects/alteryx_creations.html', context)

def saywhen(request):
	context={}
	return render(request, 'dsp/Projects/saywhen.html', context)

def website_code(request):
	context={}
	return render(request, 'dsp/Projects/website_code.html', context)

def budget_template(request):
	context={}
	return render(request, 'dsp/Projects/budget_template.html', context)

def create_project(pname, purl, desc):
	return {'project':pname, 'reflink':purl, 'description': desc}

#all projects
def davesdatadepot(request):
	projects = []
	#saywhen
	pname = "SayWhen — Movie/TV Scene Finder"
	purl = "http://www.davidschneiderprojects.com/davesdatadepot/saywhen/"
	desc = "Do you have a favorite line from a favorite TV show or movie, but don't remember what episode or time it's from? Let SayWhen find the exact spot and link you to it."
	project = create_project(pname, purl , desc)
	projects.append(project)
	#mapping mountains
	pname = "Mapping Colorado Mountains"
	purl = "http://www.davidschneiderprojects.com/davesdatadepot/mapping_mountains/"
	desc = "Using Python with Folium to create an interactive map of the 100 highest peaks in Colorado."
	project = create_project(pname, purl , desc)
	projects.append(project)
	#denver zipcodes
	pname = "Mapping & Modeling Denver Zipcodes"
	purl = "http://www.davidschneiderprojects.com/davesdatadepot/denver_zipcodes/"
	desc = "An exploratory project I did for a Coursera assignment. Using Python with Folium to plot restaurants, income, etc., zoned by ZCTA."
	project = create_project(pname, purl , desc)
	projects.append(project)
	#resume
	pname = "Stylized Resume From JSON"
	purl = "http://www.davidschneiderprojects.com/davesdatadepot/resume_from_plaintext/"
	desc = "Use Python to create a formatted .docx or PDF file from a plaintext JSON."
	project = create_project(pname, purl, desc)
	projects.append(project)
	#budget spreadsheet
	pname = "Monthly Budget Template"
	purl = "http://www.davidschneiderprojects.com/davesdatadepot/budget_template/"
	desc = "Spreadsheet for tracking personal expenses. Goal is maximum customizability, which unfortunately requires some manual input. Most useful feature is trajectory graphing of spending by category and total."
	project = create_project(pname, purl, desc)
	projects.append(project)
	#alteryx
	pname = "Alteryx For Data Analysis"
	purl = "http://www.davidschneiderprojects.com/davesdatadepot/alteryx_creations/"
	desc = "Alteryx is a powerful, accessible tool that I am certified in and used at my past role to create a variety of custom tools and solutions."
	project = create_project(pname, purl , desc)
	projects.append(project)
	#this site
	pname = "Code For This Website"
	purl = "http://www.davidschneiderprojects.com/davesdatadepot/website_code/"
	desc = "So meta. The internals of this site are mainly built with Django, Bootstrap, and Sass."
	project = create_project(pname, purl, desc)
	projects.append(project)
	return render(request, 'dsp/davesdatadepot.html', {"context": projects})