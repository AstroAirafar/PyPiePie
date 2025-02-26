from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "PyPiePie"
admin.site.site_title = "PyPiePie Admin Portal"
admin.site.index_title = "Welcome to PyPiePie Admin Portal"

urlpatterns = [
    path("", views.user_login, name="login"),
    path("home", views.home, name="home"),
    path("level", views.level, name="level"),
    path("index", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("faqs", views.faqs, name="faqs"),
    path("terms", views.terms, name="terms"),
    path("errorpage", views.errorpage, name="errorpage"),
    path("subscription", views.subscription, name="subscription"),
    path("preferences", views.preferences, name="preferences"),
    path("feedback", views.feedback, name="feedback"),
    path("p1s1", views.p1s1, name="p1s1"),
    path("p1s2", views.p1s2, name="p1s2"),
    path("p1s3", views.p1s3, name="p1s3"),
    path("p1s4", views.p1s4, name="p1s4"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)