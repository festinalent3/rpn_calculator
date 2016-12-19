from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import decode_and_convert

def infixConverter(request, q=None, *args, **kwargs):
    if request.method == "GET":
        try:
        	return JsonResponse({'error': False, 'result': decode_and_convert(request.GET['q'])})
        except Exception as e:
        	return JsonResponse({'error': True, 'message': str(e)})
        	