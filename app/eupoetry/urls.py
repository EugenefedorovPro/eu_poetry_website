from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.content, name="content"),
    path("<str:html_name>/", views.single_text, name="single_text"),
    re_path(
        r".*\/*back_to_content",
        views.back_to_content,
        name="back_to_content"
            ),
    re_path(r".*\/*eupro", views.eupro, name="eupro"),
]
