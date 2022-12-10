from functools import partial
import io
from django import dispatch
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.response import Response

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from apicrud.models import(
    Category
)
from apicrud.serializers import CategorySerializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.views import APIView


#function based
@csrf_exempt
def category_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            cat = Category.objects.get(id=id)
            serializer = CategorySerializers(cat)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")

        bar = Category.objects.all()
        serializer = CategorySerializers(bar, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = CategorySerializers(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse (json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse (json_data, content_type='application/json')

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Category.objects.get(id=id)
        serializer = CategorySerializers(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Updated"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application.json")

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Category.objects.get(id=id)
        stu.delete()
        res = {"msg":"deleted"}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(res, safe=False)

#class based
@method_decorator(csrf_exempt, name="dispatch")
class CategoryAPI(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get("id", None)
            if id is not None:
                cat = Category.objects.get(id=id)
                serializer = CategorySerializers(cat)
                # json_data = JSONRenderer().render(serializer.data)
                return JsonResponse(serializer.data, safe=False)
            all = Category.objects.all()
            serializer = CategorySerializers(all, many=True)
            return JsonResponse(serializer.data)
    # def get(self, request, format=None):
    #     transformers = Category.objects.all()
    #     serializer = CategorySerializers(transformers, many=True)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = CategorySerializers(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg":"created"})
            return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        if request.method == "PUT":
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get("id")
            cat = Category.objects.get(id=id)
            serializer = CategorySerializers(cat, data=pythondata)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"updated"})
            return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        if request.method == "DELETE":
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get("id")
            cat = Category.objects.get(id=id)
            cat.delete()
            return JsonResponse({"message":"deleted"})