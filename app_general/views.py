from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    return HttpResponse('Phenomenal')
