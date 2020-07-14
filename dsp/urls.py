from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'dsp'

urlpatterns = [
    path('', views.home, name='homeblank'),
    path('/', views.home, name='homeslash'),
    path('home/', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('davesdatadepot/', views.davesdatadepot, name='davesdatadepot'),
    path('python/', views.pyython, name='pyython'),
    path('etc/', views.etc, name='etc'),
    path('contact/', views.contact, name='contact'),
    path('/resume/', views.resume, name='resume'),
    path('davesdatadepot/nfl_stats/',
        views.nfl_stats, name='nfl_stats'),
    path('davesdatadepot/mapping_mountains/',
    	views.mapping_mountains, name='mapping_mountains'),
    path('davesdatadepot/denver_zipcodes/',
    	views.denver_zipcodes, name='denver_zipcodes'),
    path('davesdatadepot/alteryx_creations/',
        views.alteryx_creations, name='alteryx_creations'),
    path('davesdatadepot/budget_template/',
        views.budget_template, name='budget_template'),
    path('davesdatadepot/website_code/',
        views.website_code, name='website_code'),
    path('davesdatadepot/findscene/',
        views.findscene, name='findscene'),
    path('davesdatadepot/resume_from_plaintext/',
        views.resume_from_plaintext, name='resume_from_plaintext'),
    path('davesdatadepot/parking_tickets/',
        views.parking_tickets, name='parking_tickets'),
    path('davesdatadepot/sw/',
        views.sw_signin, name='sw_signin')
    url(
        r'^ptform-options-autocomplete/$',
        views.PTFormInputAutocompleteDays.as_view(),
        name='ptform-options-autocomplete',
    ),

]