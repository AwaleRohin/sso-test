# urls.py
from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    # Add other URL patterns here
]