from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<html><h1>This is CICD test page version-1.0</h1></html>")



