from django.urls import path
from .views import inquiry_view, inquiry_success  # Ensure these views exist in views.py

urlpatterns = [
    path('get-quote/', inquiry_view, name='inquiry_form'),
    path('get-quote/success/', inquiry_success, name='inquiry_success'),
]
