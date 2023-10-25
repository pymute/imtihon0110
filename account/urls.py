from django.urls import path
from .views import SignUpView,ListAPIView

urlpatterns = [
    path('sign-up/', SignUpView.as_view())
]
