from django.urls import path
from .views import ScaleView


urlpatterns = [
    path("get_scale/", ScaleView.as_view(), name="get_scale"),
]
