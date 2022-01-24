# this file is used to convert native datatype to JSON format
from re import T
from rest_framework import serializers
from .models import *



class CheckListItemSerializer(serializers.ModelSerializer):
    # hide user info when we retrive data from database and show data for user who is currently logged in
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())    
                                                                                
    
    class Meta:
        model = CheckListItem
        fields = "__all__"


class CheckListSerializer(serializers.ModelSerializer):
    # hide user info when we retrive data from database and show data for user who is currently logged in
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = CheckListItemSerializer(source = 'checklistitem_set' , many=True , read_only = True)

    class Meta:
        model = Checklist
        fields = "__all__"

