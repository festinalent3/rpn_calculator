from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
# Create your views here.

from .models import calculate


def calculator(request, q=None, *args, **kwargs):
    print(request.GET['q'])
    if request.method == "GET":
    	return JsonResponse({'error': 'false', 
    		'result': calculate(request.GET['q'])})