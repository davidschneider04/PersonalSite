from django.urls import path
from django.conf.urls import url 
from . import views

app_name = 'dsp'

urlpatterns = [
    path('', views.home, name='homeblank'),
    path('home/', views.home, name='home'),
    path('davesdatadepot/', views.davesdatadepot, name='davesdatadepot'),
    path('python/', views.pyython, name='pyython'),
    path('etc/', views.etc, name='etc'),
    path('contact/', views.contact, name='contact'),
]