"""
Table of Contents
- Imports
- Model Registration
"""

# ========================
# - Imports
# ========================
from django.contrib import admin
from .models import Bill, Category, Reminder, Image

# ========================
# - Model Registration
# ========================

# Register models to appear in Django Admin site.
admin.site.register(Bill)
admin.site.register(Category)
admin.site.register(Reminder)
admin.site.register(Image)
