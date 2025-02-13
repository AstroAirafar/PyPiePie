from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "PyPiePie"
admin.site.site_title = "PyPiePie Admin Portal"
admin.site.index_title = "Welcome to PyPiePie Admin Portal"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
]