from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import HymnViewSet, SignupView, LoginView

router = DefaultRouter()
router.register(r'hymns', HymnViewSet, basename='hymn')

urlpatterns = router.urls
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
