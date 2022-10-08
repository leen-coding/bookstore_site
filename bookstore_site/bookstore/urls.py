from django.urls import path
from . import  views

urlpatterns = [
    path("all_books",views.show_all_books),
    path("operate_storages/<int:bookid>",views.operate_storages)
]