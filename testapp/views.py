from django.shortcuts import render, HttpResponse

# Basic Python Page
def index(request):
    return HttpResponse("<html><h1>This is CICD test page version-1.0</h1></html>")



