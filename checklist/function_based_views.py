# this file is same as views.py but all logic written is in function_based views 

from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import ListAPIView , CreateAPIView , DestroyAPIView , UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from checklist.serializers import CheckListSerializer , CheckListItemSerializer
from rest_framework.permissions import IsAuthenticated 
from checklist.permissions import IsOwner
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, status








class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated , IsOwner]

    def get(self, request, format=None):
        data = Checklist.objects.filter(user=request.user )     
        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.dat      
        return Response(serialized_data, status=status.HTTP_200_OK )    

    def post(self, request, format=None):
        # Code for creation
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  
 


class ChecklistUpdateDelete(APIView):
    serializer_class = CheckListSerializer

    def get_object(self, pk):
        try:
            obj = Checklist.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Checklist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class CheckListItemCreateAPIView(APIView):
    """
    Creation of check list item
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, request, format=None):
        # Code for creation
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  

class CheckListItemAPIView(APIView):
    """
    Retrieve, Update, Delete of check list items 
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
  

    def get_object(self, pk):
        try:
            obj = CheckListItem.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except CheckListItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   