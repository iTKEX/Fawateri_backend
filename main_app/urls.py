"""
TABLE OF CONTENT
- IMPORTS
- URLs Patterns:
    - Bills URLs

"""

########## IMPORTS ##########
from django.urls import path
from .views import Home, BillsList, CategoriesList, BillDetails, BillImageView

########## URLs Patterns ##########
urlpatterns = [
    path("", Home.as_view(), name="home"),
    # Bills URLs
    path("bills/", BillsList.as_view(), name="bills-list"),
    path("bills/<int:bill_id>/", BillDetails.as_view(), name="bill-details"),
    path("bills/<int:bill_id>/image/", BillImageView.as_view(), name="images"),
    # Categories URLs
    path("categories/", CategoriesList.as_view(), name="categories-list"),
    # Bills URLs
    path("reminders/", BillsList.as_view(), name="bills-list"),
    # Users URLs
]
