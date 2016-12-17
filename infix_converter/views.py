from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import decode_and_convert

# Create your views here.

def infixConverter(request, q=None, *args, **kwargs):
    print(request.GET['q'])
    if request.method == "GET":
    	return JsonResponse({'error': 'false', 
    		'result': decode_and_convert(request.GET['q'])})
