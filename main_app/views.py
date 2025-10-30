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
from rest_framework import generics, status
from .models import Bill, Category
from .serializers import BillSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


# Home view
class Home(APIView):
    def get(self, request):
        content = {"message": "Welcome to the FAWATERI api home route!"}
        return Response(content)


# BillsList view
class BillsList(generics.ListCreateAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class BillDetails(generics.ListCreateAPIView):
    serializer_class = BillSerializer

    def get(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id)
            return Response(self.serializer_class(bill).data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id)
            serializer = self.serializer_class(bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Delete Requset
    def delete(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id)
            bill.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# BillsList view
class CategoriesList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# BillsList view
class Reminders(generics.ListCreateAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()
