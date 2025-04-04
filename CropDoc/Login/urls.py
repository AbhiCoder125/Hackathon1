from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Registration_view, name='Registration_view'),
    path('login/', login_view, name='login')
]