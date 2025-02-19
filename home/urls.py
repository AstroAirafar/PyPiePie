from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "PyPiePie"
admin.site.site_title = "PyPiePie Admin Portal"
admin.site.index_title = "Welcome to PyPiePie Admin Portal"

urlpatterns = [
    path("", views.home, name="home"),
    path("level", views.level, name="level"),
    path("index", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("faqs", views.faqs, name="faqs"),
    path("terms", views.terms, name="terms"),
    path("errorpage", views.errorpage, name="errorpage"),
    path("subscription", views.subscription, name="subscription"),
    path("preferences", views.preferences, name="preferences"),
    path("feedback", views.feedback, name="feedback"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)