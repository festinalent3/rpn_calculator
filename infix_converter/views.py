from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import decode_and_convert

def infixConverter(request, q=None, *args, **kwargs):
    if request.method == "GET":
        response = {'error': False, 'result': ''}

        try:
            response['result'] = decode_and_convert(request.GET['q'])
        except Exception as e:
            response['result'] = str(e)
            response['error'] = True

        return JsonResponse(response)
