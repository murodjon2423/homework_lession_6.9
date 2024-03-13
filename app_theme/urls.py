# urls.py
from django.urls import path
from .views import faylni_oqish

urlpatterns = [
    path('', faylni_oqish, name='faylni_oqish'),
    
]
