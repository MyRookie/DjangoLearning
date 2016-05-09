from django.shortcuts import render

# Create your views here.
def home(request):
	string = u"This is a string which used to learn templetes of Django!"
	TutorialList = ["HTML","CSS","jQuery","Python","Django"]
	return render(request,'home.html',{'TutorialList':TutorialList})

def add(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))