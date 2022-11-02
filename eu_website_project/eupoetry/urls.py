from django.urls import path
from . import views


urlpatterns = [
    path("", views.content, name="content"),
    path("1/", views.avva, name="avva"),
    path("bachinichego/", views.bachinichego, name="bachinichego"),
    path("gdeyarostnej/", views.gdeyarostnej, name="gdeyarostnej"),
]
