"""
TABLE OF CONTENT
- IMPORTS
- Models Serializers:
    - ImageSerializer
    - CategorySerializer
    - BillsSerializer

"""

########## IMPORTS ##########
from rest_framework import serializers
from .models import Bill, Image, Category, Reminder

########## Models Serializers ##########


# ImageSerializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


# CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# BillSerializer
class BillSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    locations = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = "__all__"


# ReminderSerializer
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"
