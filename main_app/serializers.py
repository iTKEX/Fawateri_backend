"""
TABLE OF CONTENT
- IMPORTS
- Models Serializers:
    - BillsSerializer

"""

########## IMPORTS ##########
from rest_framework import serializers
from .models import Bill, Image

########## Models Serializers ##########


# ImageSerializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


# BillSerializer
class BillSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)

    class Meta:
        model = Bill
        fields = "__all__"
