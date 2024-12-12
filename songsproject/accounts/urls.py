from django.urls import path
from .views import ContactView, LoginView, SignupView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/<int:id>/', ContactView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
