from django.urls import path
from . import views

urlpatterns = [
    path('all_card', views.all_card)
]
