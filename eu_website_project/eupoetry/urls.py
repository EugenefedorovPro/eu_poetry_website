from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.content, name="content"),
    path("<int:verse_id>/", views.verse, name="verse"),
    re_path(".*/back_to_content", views.back_to_content, name="back_to_content"),
    path("eupro/", views.eupro, name="eupro"),
]
