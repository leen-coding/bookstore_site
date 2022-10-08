from django.urls import path
from . import views

urlpatterns = [

    path("home/", views.home.as_view()),
    # path("send/msg/",views.send_msg),
    # path("getinfo/",views.getinfo.as_view())

]
