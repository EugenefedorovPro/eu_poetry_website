from django.urls import path
from . import views


urlpatterns = [
    path("", views.content, name="content"),
    path("<int:verse_id>/", views.verse, name="verse"),
    path("<int:no_use>/back_to_content", views.back_to_content, name="back_to_content"),
]
