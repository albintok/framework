from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bikes.serializers import BikeSerializers,BikeModelSerializer
from bikes.models import Vechicles

class BikeView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Vechicles.objects.all()
        if "colour" in request.query_params:
            qs=qs.filter(colour=request.query_params.get("colour"))
        if "name" in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get("name"))
        serialiazer=BikeSerializers(qs,many=True)
        return Response(data=serialiazer.data)
    def post(self,request,*args,**kwargs):
        serializer=BikeSerializers(data=request.data)
        if serializer.is_valid():
            Vechicles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class BikeViewDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Vechicles.objects.get(id=id)
        serializer=BikeSerializers(qs)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Vechicles.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Vechicles.objects.filter(id=id)
        serializer=BikeSerializers(instance=qs,data=request.data)
        if serializer.is_valid():
            qs.update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# Create your views here.




#modelserializerview

class BikeModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Vechicles.objects.all()
        serializer=BikeModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=BikeModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class BikeDetailModelView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Vechicles.objects.get(id=id)
        serializer=BikeModelSerializer(qs)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bike=Vechicles.objects.get(id=id)
        serializer=BikeModelSerializer(instance=bike,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.data)

