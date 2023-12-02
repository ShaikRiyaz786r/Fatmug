from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

class VendorView(viewsets.ViewSet):
    def list(self,request):
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        if pk is not None:
            record = Vendor.objects.get(id=id)
            serializer = VendorSerializer(record)
            return Response(serializer.data)


    def create(self,request):
        serializer = VendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'data posted'}
            return Response(response)
        
    def update(self,request,id):
        record = Vendor.objects.get(id=id) 
        serializer = VendorSerializer(record,request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'data updated'}
            return Response(response)

    def partial_update(self,request,id):
        record = Vendor.objects.get(id=id)
        serializer = VendorSerializer(record,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'partially data updated'}
            return Response(response)


    def destroy(self,request,id):
        record = Vendor.objects.get(id=id)
        record.delete()
        response = {'message':'data deleted'}
        return Response(response)

class PurchaseOrderView(viewsets.ViewSet):
    def list(self,request):
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        if pk is not None:
            record = Vendor.objects.get(id=id)
            serializer = VendorSerializer(record)
            return Response(serializer.data)


    def create(self,request):
        serializer = VendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'data posted'}
            return Response(response)
        
    def update(self,request,id):
        record = Vendor.objects.get(id=id) 
        serializer = VendorSerializer(record,request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'data updated'}
            return Response(response)

    def partial_update(self,request,id):
        record = Vendor.objects.get(id=id)
        serializer = VendorSerializer(record,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'partially data updated'}
            return Response(response)


    def destroy(self,request,id):
        record = Vendor.objects.get(id=id)
        record.delete()
        response = {'message':'data deleted'}
        return Response(response)

class VendorPerformanceView(viewsets.ViewSet):
    def list(self,request):
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        if pk is not None:
            record = Vendor.objects.get(id=id)
            serializer = VendorSerializer(record)
            return Response(serializer.data)


    def create(self,request):
        serializer = VendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'data posted'}
            return Response(response)
        
    def update(self,request,id):
        record = Vendor.objects.get(id=id) 
        serializer = VendorSerializer(record,request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'data updated'}
            return Response(response)

    def partial_update(self,request,id):
        record = Vendor.objects.get(id=id)
        serializer = VendorSerializer(record,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'partially data updated'}
            return Response(response)


    def destroy(self,request,id):
        record = Vendor.objects.get(id=id)
        record.delete()
        response = {'message':'data deleted'}
        return Response(response)