"""
TABLE OF CONTENT
- IMPORTS
- Views:
  - Home view
  - BillsList view

"""

########## IMPORTS ##########
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer

# Home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the FAWATERI api home route!'}
    return Response(content)

# BillsList view
class BillsList(generics.ListCreateAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()