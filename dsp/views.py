from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from dal import autocomplete

from .forms import ParkingTicketForm
from . import create_schedules
from ScheduleCreator import create_cal, finish_cal, make_event

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

def findscene(request):
	context={}
	return render(request, 'dsp/Projects/findscene.html', context)

def website_code(request):
	context={}
	return render(request, 'dsp/Projects/website_code.html', context)

def budget_template(request):
	context={}
	return render(request, 'dsp/Projects/budget_template.html', context)

def create_project(pname, purl, desc):
	return {'project':pname, 'reflink':purl, 'description': desc}

def schedule_creator(request):
	week_lookup = {'1st':1, '2nd':2, '3rd':3, '4th':4}
	week_of_month = week_lookup[request.POST['week_of_month']]
	day_lookup = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday': 5, 'Sunday':6}
	day_of_week = day_lookup[request.POST['day_of_week']]
	results = create_schedules.get_events(week_of_month, day_of_week)
	return results

class PTFormInputAutocompleteDays(autocomplete.Select2ListView):
	def get_list(self):
		options = ParkingTicketForm.objects.all()
		options_tups = [i.option for i in option]
		return options_tups

def parking_tickets(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ParkingTicketForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required, redirect to a new URL:
			sc = ScheduleCreator()
			acal = sc.create_cal()
			acal += sc.make_event(acal, request)
			acal = finish_cal(acal)
			cal = schedule_creator(request)
			response = HttpResponse(cal, content_type='application/text charset=utf-8')
			response['Content-Disposition'] = 'attachment; filename="parking_reminders.ics"'
			return response
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ParkingTicketForm()
	context = {'form': form}
	return render(request, 'dsp/Projects/parking_tickets.html', context)

# all projects
def davesdatadepot(request):
	projects = []
	# findscene
	pname = "FindScene — App to Find Video Links"
	purl = "https://www.davidschneiderprojects.com/davesdatadepot/findscene/"
	desc = "Do you have a favorite line from a favorite TV show or movie, but don't remember what episode or time it's from? Let FindScene find the exact spot and link you to it."
	project = create_project(pname, purl, desc)
	projects.append(project)
	# mapping mountains
	pname = "Mapping Colorado Mountains"
	purl = "https://www.davidschneiderprojects.com/davesdatadepot/mapping_mountains/"
	desc = "Using Python with Folium to create an interactive map of the 100 highest peaks in Colorado."
	project = create_project(pname, purl, desc)
	projects.append(project)
	# denver zipcodes
	pname = "Mapping & Modeling Denver Zipcodes"
	purl = "https://www.davidschneiderprojects.com/davesdatadepot/denver_zipcodes/"
	desc = "Using Python with Folium to plot restaurants, income, etc., zoned by ZCTA, and sklearn to create a cluster model."
	project = create_project(pname, purl, desc)
	projects.append(project)
	# resume
	pname = "Stylized Resume From JSON"
	purl = "https://www.davidschneiderprojects.com/davesdatadepot/resume_from_plaintext/"
	desc = "Use Python to create a formatted .docx or PDF file from a plaintext JSON."
	project = create_project(pname, purl, desc)
	projects.append(project)
	# budget spreadsheet
	pname = "Monthly Budget Template"
	purl = "https://www.davidschneiderprojects.com/davesdatadepot/budget_template/"
	desc = "Spreadsheet for tracking personal expenses. Goal is maximum customizability, which unfortunately requires some manual input. Most useful feature is trajectory graphing of spending by category and total."
	project = create_project(pname, purl, desc)
	projects.append(project)
	# alteryx
	#pname = "Alteryx For Data Analysis"
	#purl = "http://www.davidschneiderprojects.com/davesdatadepot/alteryx_creations/"
	#desc = "Alteryx is a powerful, accessible tool that I am certified in and used at my past role to create a variety of custom tools and solutions."
	#project = create_project(pname, purl , desc)
	#projects.append(project)
	# parking tickets
	pname = "Automated Monthly Reminders"
	purl = "https://www.davidschneiderprojects.com/davesdatadepot/parking_tickets/"
	desc = 'Create reminders in "the #th <Weekday> of the month" format in a file ready for import on phone or computer. Helpful for Denverites avoiding street sweeping tickets.'
	project = create_project(pname, purl, desc)
	projects.append(project)
	# this site
	pname = "Code For This Website"
	purl = "https://www.davidschneiderprojects.com/davesdatadepot/website_code/"
	desc = "So meta. The internals of this site are mainly built with Django, Bootstrap, and Sass."
	project = create_project(pname, purl, desc)
	projects.append(project)
	return render(request, 'dsp/davesdatadepot.html', {"context": projects})