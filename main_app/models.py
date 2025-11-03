"""
TABLE OF CONTENT
- IMPORTS
- MODELS CLASSES
    - Category model
    - Bill model
    - Image model
    - Reminder model
"""

########## IMPORTS ##########
from django.db import models
from django.contrib.auth.models import User


########## MODELS CLASSES ##########


# Category model
class Category(models.Model):
    """Represents a category tag for bills (e.g., car, electronics, repair)."""

    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Bill model
class Bill(models.Model):
    """Main bill model containing merchant info, warranty, and relations."""

    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    warranty = models.CharField(max_length=50, blank=True)
    cost = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bills")

    def __str__(self):
        return f"{self.company}, {self.title}"


# Image model
class Image(models.Model):
    """Stores a single image related to a bill."""

    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for Bill: {self.bill.id} @{self.url}"


# Reminder model
class Reminder(models.Model):
    """Reminder for warranty or bill-related dates."""

    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    reminder_at = models.DateField()
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
