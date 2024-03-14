from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("price/", views.price, name="price"),
    path("works/", views.works, name="works"),
    path("add_contact/", views.add_contact, name="add_contact"),
]
