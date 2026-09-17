from django.urls import path

from fakelogin import views

app_name = "fakelogin"

urlpatterns = [
    path("", views.fakelogin, name="modal"),
]
