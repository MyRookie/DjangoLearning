from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
# 	context = {}
# 	context['hello'] = "Hello World"
# 	return render(request,'hello,html',context)

def display(request):
	return HttpResponse("Hello world ! ")

def home(request):
	return render(request,'home.html')