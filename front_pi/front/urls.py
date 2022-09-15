from django.urls import path
from .views import login

app_name = 'front'

"""
Urls do app front.
"""

urlpatterns = [
    path('login/', login, name='login'),
]