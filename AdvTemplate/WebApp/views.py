
from django.shortcuts import render
#Create your view here
def Home_View(request):
	return render(request,'MyApp/home.html')
def Sports_View(request):
	return render(request,'MyApp/sports.html')
def News_View(request):
	return render(request,'MyApp/news.html')
def Courses_View(request):
	return render(request,'MyApp/courses.html')