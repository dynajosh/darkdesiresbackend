from django.urls import path, re_path, include
from macpath import basename
from rest_framework.routers import DefaultRouter

from .viewsets import PostViewset, InfluencerViewset, CompanyViewset
from .views import getTweet, getLikingUsers, testInstagram

router =DefaultRouter()

router.register("posts", PostViewset, basename="posts")
router.register("influencer", InfluencerViewset, basename="influencer")
router.register("company", CompanyViewset, basename="company")

urlpatterns = [
    path("", include(router.urls), name="api"),
    path(r"get-tweet", getTweet, name="get-tweet"),
    path(r"liking-users/", getLikingUsers, name="get-likers"),
    path(r"test-instagram/", testInstagram, name="test-instagram"),
]