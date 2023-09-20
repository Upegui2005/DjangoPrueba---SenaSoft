from django.urls import path

from . import views

app_name = "pagina"

urlpatterns = [
    path("", views.index, name="index")
]