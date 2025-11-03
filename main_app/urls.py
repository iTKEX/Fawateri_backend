"""
TABLE OF CONTENT
- IMPORTS
- URL PATTERNS
    - Home
    - Bills
    - Categories
    - Reminders
    - Users (Auth)
"""

########## IMPORTS ##########
from django.urls import path
from .views import (
    Home,
    BillsList,
    CategoriesList,
    BillDetails,
    BillImage,
    BillCategories,
    BillReminders,
    CreateUserView,
    LoginView,
    VerifyUserView,
)


########## URL PATTERNS ##########
urlpatterns = [
    # - Home
    path("", Home.as_view(), name="home"),
    
    # - Bills
    path("bills/", BillsList.as_view(), name="bills-list"),
    path("bills/<int:bill_id>/", BillDetails.as_view(), name="bill-details"),
    path("bills/<int:bill_id>/image/", BillImage.as_view(), name="images"),
    path("bills/<int:bill_id>/categories/", BillCategories.as_view(), name="bill-categories"),
    
    # - Reminders
    path("bills/<int:bill_id>/reminders/", BillReminders.as_view(), name="bill-reminders"),
    path("bills/<int:bill_id>/reminders/<int:reminder_id>/", BillReminders.as_view(), name="bill-reminder-detail"),
    
    # - Categories
    path("categories/", CategoriesList.as_view(), name="categories-list"),
    
    # - Users (Auth)
    path("users/signup/", CreateUserView.as_view(), name="signup"),
    path("users/login/", LoginView.as_view(), name="login"),
    path("users/verify/", VerifyUserView.as_view(), name="verify"),
]
