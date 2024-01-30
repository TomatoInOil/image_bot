from django.urls import path

from images.views import ImageView

BASE_URL = "api/v1"

app_name = "images"

urlpatterns = [path(f"{BASE_URL}/photos/", ImageView.as_view(), name="photos")]
