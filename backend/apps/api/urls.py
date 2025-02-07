from django.urls import include, path
from .views import CheckEnharmonicView


urlpatterns = [
    path("check_enharmonic/", CheckEnharmonicView.as_view(), name="check_enharmonic"),
]
