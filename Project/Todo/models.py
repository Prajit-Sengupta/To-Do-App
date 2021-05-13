from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)  #to check status of whether task is complete or not
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  
        #f you wanna interact with the database with the model, for example create an instance of the model and save it or retrieve the model from db;. Thsi will come handy.
