from django.shortcuts import render
from django.http.response import HttpResponse

def foods(request):
    return HttpResponse('Good Foods, Good Help, Good Menu')

def food(request, food_id):
    return HttpResponse('MENU ID = ', str(food_id))
