import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def list_postgraduates(request):
    with open('./postgraduates_backend/scrapy_service/postgrados/spiders/careers.json', mode='r+', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return JsonResponse(data)

def index(request):
    string = 'youre probably looking for /postgraduates/show' 
    return HttpResponse(string)