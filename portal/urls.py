from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("ong/", views.ong, name="ong"),
    path("contato/", views.contato, name="contato")
]