from django.contrib import admin
from .models import Bill, Category, Reminder, Image

# Register your models here.
admin.site.register(Bill)
admin.site.register(Category)
admin.site.register(Reminder)
admin.site.register(Image)