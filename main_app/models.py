"""
TABLE OF CONTENT
- IMPORTS
- Models Classes
    - Category model
    - Bill model
    - Image model
    - Reminder model
"""

########## IMPORTS ##########
from django.db import models


########## Models Classes ##########


# Category model
class Category(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Bill model
class Bill(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    warranty = models.CharField(max_length=50, blank=True)
    cost = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.company}, {self.title}"


# Image model
class Image(models.Model):
    title = models.CharField(max_length=50)
    url = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for Bill: {self.bill.id} @{self.url}"


# Reminder model
class Reminder(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    reminder_at = models.DateField()
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
