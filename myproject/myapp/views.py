from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'index.html')
    

def about(request):
    return HttpResponse("this is aboutpage")

def services(request):
    return HttpResponse("this is servicepage")

def contact(request):
    return HttpResponse("this is contactpage")