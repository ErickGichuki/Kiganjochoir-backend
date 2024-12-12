from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordedSongsViewSet, SongsView

router = DefaultRouter()
router.register(r'recordedsongs', RecordedSongsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("songs/", SongsView.as_view(), name='songs')
]
