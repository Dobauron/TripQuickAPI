from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from .serializers import RegisterSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": {
                    "email": user.email,
                    "username": user.username,
                },
                "message": "Account created successfully",
            },
            status=status.HTTP_201_CREATED,
        )
