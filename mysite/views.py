from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    View function for the home page.
    """
    return HttpResponse("Welcome to My Django Site!")

def about(request):
    """
    View function for the about page.
    """
    return HttpResponse("About Us - This is a Django project.")