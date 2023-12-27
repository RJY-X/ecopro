from django.urls import path

from . import views


app_name = "ecom"

urlpatterns = [
    path("", views.index, name="index")
]