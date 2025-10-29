"""
TABLE OF CONTENT
- IMPORTS
- Models Serializers:
    - BillsSerializer

"""

########## IMPORTS ##########
from rest_framework import serializers
from .models import Bills

########## Models Serializers ##########


# BillSerializer
class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bills
        fields = "__all__"
