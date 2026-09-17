from django.urls import path

from demo import views

app_name = "tst"

urlpatterns = [
    path("full/", views.index_full, name="full"),
    path("modal/", views.modal, name="modal"),
    path("", views.index, name="index"),
]
