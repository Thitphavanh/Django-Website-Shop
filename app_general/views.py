from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    return HttpResponse('<h1>PHENOMENAL</h1>')

def about(request):
    return HttpResponse('ABOUT PHENOMENAL')
