from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api2.serializers import CategorySerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from api2.models import Category


# Create your views here.
@csrf_exempt
def category_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = CategorySerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse (json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)   
        return HttpResponse (json_data, content_type='application/json')

@csrf_exempt    
def update(request):
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        cat = Category.objects.get(id=id)
        serializer = CategorySerializer(cat, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message":"updated"})
        return JsonResponse(serializer.errors)