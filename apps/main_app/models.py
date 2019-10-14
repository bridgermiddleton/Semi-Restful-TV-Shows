from __future__ import unicode_literals
from django.db import models
class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors['title'] = "Show title should be at least two characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network name should be at least 3 characters."
        if postData['description']:
            if len(postData['description']) < 10:
                errors['description'] = "Description should be at least 10 characters."
        return errors
        
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

# Create your models here.
