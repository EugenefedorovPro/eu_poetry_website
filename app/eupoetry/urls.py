from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.content, name="content"),
    path("list_verse/", views.list_verses, name="list_verses"),
    path("<str:html_name>/", views.single_text, name="single_text"),

    re_path(
        r".*\/*back_to_content",
        views.back_to_content,
        name="back_to_content"
            ),
    re_path(r".*\/*eupro", views.eupro, name="eupro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
