from django.shortcuts import render
from django.core import management
from django.http import HttpResponseRedirect


def index(request):
	return render(request, 'home/home.html')

def submit1(request):
	management.call_command('light')

def submit2(request):
	management.call_command('light2')

def submit3(request):
	management.call_command('light3')

def submit4(request):
	management.call_command('light4')

def submit5(request):
	management.call_command('light5')

def submit6(request):
	management.call_command('light6')

def submit7(request):
	management.call_command('light7')

def submit8(request):
	management.call_command('light8')



