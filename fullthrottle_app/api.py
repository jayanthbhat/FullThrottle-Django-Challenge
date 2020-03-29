from rest_framework import generics
from .serializers import UserListAPISerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import get_user_model
User = get_user_model()

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListAPISerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserListAPISerializer(queryset, many=True)
        content={
            "ok": True,
            "members": serializer.data
        }
        return Response(content)

       
