"""
TABLE OF CONTENT
- IMPORTS
- HOME VIEW
- BILLS VIEWS
    - BillsList
    - BillDetails
    - BillImage
    - BillCategories
    - BillReminders
- CATEGORIES VIEW
- AUTH VIEWS
    - CreateUserView
    - LoginView
    - VerifyUserView
"""

########## IMPORTS ##########
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Bill, Category, Image, Reminder
from .serializers import (
    BillSerializer,
    CategorySerializer,
    ImageSerializer,
    ReminderSerializer,
    UserSerializer,
)


########## HOME VIEW ##########
class Home(APIView):
    """Simple home route for API testing."""

    def get(self, request):
        return Response({"message": "Welcome to the FAWATERI API home route!"})


########## BILLS VIEWS ##########


# BillsList
class BillsList(generics.ListCreateAPIView):
    """List all bills or create a new bill (authenticated user only)."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BillSerializer

    def get_queryset(self):
        """Return bills for the authenticated user only."""
        return Bill.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Link created bill to the authenticated user."""
        serializer.save(user=self.request.user)


# BillDetails
class BillDetails(APIView):
    """Retrieve, update, or delete a single bill."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BillSerializer

    def get(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            return Response(self.serializer_class(bill).data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            serializer = self.serializer_class(bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            bill.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# BillImage
class BillImage(APIView):
    """Handle image upload or deletion for a bill."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def post(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            Image.objects.filter(bill_id=bill_id).delete()

            payload = request.data.copy()
            payload["bill"] = bill_id

            serializer = self.serializer_class(data=payload)
            if serializer.is_valid():
                serializer.save()
                return Response(BillSerializer(bill).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            Image.objects.filter(bill_id=bill_id).delete()
            return Response(BillSerializer(bill).data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# BillCategories
class BillCategories(APIView):
    """Assign categories to a specific bill."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            ids = request.data.get("category_ids", [])
            if not isinstance(ids, list):
                return Response(
                    {"error": "category_ids must be a list"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            categories = Category.objects.filter(id__in=ids)
            bill.category.set(categories)
            bill.save()
            return Response(BillSerializer(bill).data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# BillReminders
class BillReminders(APIView):
    """Add or delete reminders related to a bill."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, bill_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            payload = request.data.copy()
            payload["bill"] = bill_id

            serializer = ReminderSerializer(data=payload)
            if serializer.is_valid():
                serializer.save()
                return Response(BillSerializer(bill).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, bill_id, reminder_id):
        try:
            bill = get_object_or_404(Bill, id=bill_id, user=request.user)
            reminder = get_object_or_404(Reminder, id=reminder_id, bill=bill)
            reminder.delete()
            return Response(BillSerializer(bill).data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


########## CATEGORIES VIEW ##########
class CategoriesList(generics.ListCreateAPIView):
    """List or create categories (authenticated only)."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


########## AUTH VIEWS ##########


# CreateUserView
class CreateUserView(generics.CreateAPIView):
    """Handle user registration and return JWT tokens."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# LoginView
class LoginView(APIView):
    """Authenticate user and return JWT tokens."""

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                content = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                }
                return Response(content, status=status.HTTP_200_OK)
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# VerifyUserView
class VerifyUserView(APIView):
    """Verify user token and return refreshed tokens."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            return Response(
                {"detail": "Failed to generate token.", "error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
