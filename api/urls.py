from django.urls import path
from .views import health_check, ImageViewSet

image_list = ImageViewSet.as_view({"get": "list", "post": "create"})
image_detail = ImageViewSet.as_view({"delete": "destroy"})

urlpatterns = [
    path("check", health_check, name="health_check"),
    path("images/", image_list, name="images-list"),
    path("images/<int:pk>/", image_detail, name="images-detail"),
]
