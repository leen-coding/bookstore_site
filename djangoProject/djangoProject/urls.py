"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_get_post', view.view_get_post),
    path('test_if_for', view.test_if_for),
    path('cal_plus_minus', view.calculator),
    path('base', view.base, name="base_url"),
    path('sport', view.sport, name = "sport_url"),
    path('img',view.test_img),
    path('firstapp/', include('firstapp.urls')),
    path('cardstore/',include('database_test.urls'))
]
