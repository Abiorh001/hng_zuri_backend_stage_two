from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import ZuriApisModel
from .serializers import ZuriSerializer


class ZuriEndpoints(APIView):

    def get(self, request: Request):

        name = request.GET.get("name")
        try:
            queryset = ZuriApisModel.objects.get(name=name)
        except ZuriApisModel.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ZuriSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK) 
 
    def post(self, request: Request):
        data = request.data
        name = data.get("name")
        if not isinstance(name, str):
            return Response({"error": "name must be a string"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ZuriSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request):
        existing_name = request.GET.get("name")
        name = request.data.get("name")
        if not isinstance(name, str):
            return Response({"error": "name must be a string"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            queryset = ZuriApisModel.objects.get(name=existing_name)
        except ZuriApisModel.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        queryset.name = name
        
        serializer = ZuriSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request):
        name = request.GET.get("name")
        try:
            queryset = ZuriApisModel.objects.get(name=name)
        except ZuriApisModel.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
class ZuriEndpointsForRetrieveUpdateDelete(APIView):

    def get(self, request: Request, pk):
        try:
            queryset = ZuriApisModel.objects.get(pk=pk)
        except ZuriApisModel.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ZuriSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        data = request.data
        name = data.get("name")
        if not isinstance(name, str):
            return Response({"error": "name must be a string"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            queryset = ZuriApisModel.objects.get(pk=pk)
        except ZuriApisModel.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        queryset.name = name
        serializer = ZuriSerializer(instance=queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk):
        try:
            queryset = ZuriApisModel.objects.get(pk=pk)
        except ZuriApisModel.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

    
