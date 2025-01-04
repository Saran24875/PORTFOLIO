# models.py

from django.db import models # type: ignore

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def _str_(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.title