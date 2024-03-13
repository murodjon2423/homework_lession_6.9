# urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('<int:id>/', index, name="index_with_id"),  # id parameter
]
