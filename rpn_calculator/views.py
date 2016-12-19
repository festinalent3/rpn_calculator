from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import calculate


def calculator(request, q=None, *args, **kwargs):
    print(request.GET['q'])
    if request.method == "GET":
        try:
            return JsonResponse({'error': False, 'result': calculate(request.GET['q'])})
        except Exception as e:
            return JsonResponse({'error': True, 'message': str(e)})
