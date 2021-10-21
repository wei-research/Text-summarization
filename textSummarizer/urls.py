from django.urls import path

from . import views

urlpatterns = [
    path('', views.intro, name='index'),
    path("summarizer", views.result, name = "summarizer" ),
    path("contact", views.contact, name = "contact" ),
    path("model", views.model, name = "model" ),
    path("error", views.error, name = "error"),


]