from django.urls import path
from .views import Registration_view

urlpatterns = [
    path('register/', Registration_view, name='Registration_view'),
]