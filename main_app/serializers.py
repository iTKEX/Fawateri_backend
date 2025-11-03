"""
TABLE OF CONTENT
- IMPORTS
- SERIALIZER CLASSES
    - ImageSerializer
    - CategorySerializer
    - ReminderSerializer
    - BillSerializer
    - UserSerializer
"""

########## IMPORTS ##########
from rest_framework import serializers
from .models import Bill, Image, Category, Reminder
from django.contrib.auth.models import User


########## SERIALIZER CLASSES ##########


# ImageSerializer
class ImageSerializer(serializers.ModelSerializer):
    """Serializer for Image model."""

    class Meta:
        model = Image
        fields = "__all__"


# CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""

    class Meta:
        model = Category
        fields = "__all__"


# ReminderSerializer
class ReminderSerializer(serializers.ModelSerializer):
    """Serializer for Reminder model."""

    class Meta:
        model = Reminder
        fields = "__all__"


# BillSerializer
class BillSerializer(serializers.ModelSerializer):
    """Serializer for Bill model, including related image, categories, and reminders."""

    image = ImageSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    reminders = ReminderSerializer(many=True, read_only=True, source="reminder_set")
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Bill
        fields = "__all__"


# UserSerializer
class UserSerializer(serializers.ModelSerializer):
    """Serializer for Django User model with password hashing support."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        """Override create to use create_user (handles password hashing)."""
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
