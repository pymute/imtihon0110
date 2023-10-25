from rest_framework.generics import CreateAPIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.generics import ListAPIView

class ListUserAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class SignUpView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
