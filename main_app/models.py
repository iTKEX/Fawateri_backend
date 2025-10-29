"""
TABLE OF CONTENT
- IMPORTS
- Models Classes
    - Bill model

"""

########## IMPORTS ##########
from django.db import models


########## Models Classes ##########


# Bill model
class Bill(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    warranty = models.CharField(max_length=50, blank=True)
    cost = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.company}, {self.title}"
    
class Image(models.Model):
    title = models.CharField(max_length=50)
    url = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for Bill: {self.bill.id} @{self.url}"
