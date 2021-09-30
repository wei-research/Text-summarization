from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("summarizer", views.result, name = "summarizer" ),
    path("contact", views.contact, name = "contact" ),
    path("intro", views.intro, name = "intro" ),

]