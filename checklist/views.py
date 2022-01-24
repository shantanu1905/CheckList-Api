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
# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, 
)



class CheckListsAPIView(ListCreateAPIView):
    """
    Creation of check list 
    """
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated , IsOwner]

    def get_queryset(self):
        queryset = Checklist.objects.filter(user=self.request.user)
        return queryset

 


class ChecklistUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CheckListSerializer
    def get_queryset(self):
        queryset = Checklist.objects.filter(user=self.request.user)
        return queryset


class CheckListItemCreateAPIView(CreateAPIView):
    """
    Creation of check list item
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
  

class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Delete of check list items 
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user=self.request.user)
        return queryset
