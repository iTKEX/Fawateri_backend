from django.db import models

# Create your models here.
class Bill(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    warranty = models.CharField(max_length=50, blank=True)
    cost = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.company}, {self.title}'