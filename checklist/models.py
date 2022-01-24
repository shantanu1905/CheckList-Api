from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Checklist(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class CheckListItem(models.Model):
    text = models.CharField(max_length=250)
    is_checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE) # CASCADE : agar checklist delete hota hai toh checklist items bhi delete hoga
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text