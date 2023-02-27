from django.urls import path
from .views import welcome

app_name = 'recipes'

urlpatterns = [
    path('', welcome),
]
