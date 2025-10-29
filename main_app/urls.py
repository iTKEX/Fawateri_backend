"""
TABLE OF CONTENT
- IMPORTS
- URLs Patterns:
    - Bills URLs

"""

########## IMPORTS ##########
from django.urls import path
from .views import Home, BillsList

########## URLs Patterns ##########
urlpatterns = [
    path("", Home.as_view(), name="home"),
    
    # Bills URLs
    path("bills/", BillsList.as_view(), name="bills-list"),
]
