from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .viewsets import PostViewset

router =DefaultRouter()

router.register("posts", PostViewset, basename="posts")


urlpatterns = [
    path("", include(router.urls), name="api"),
]