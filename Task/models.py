from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    no_of_pages = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title