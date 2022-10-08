from django.urls import path
from . import views

urlpatterns = {

    path('index', views.app_view_test)
}
