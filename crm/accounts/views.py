from django.shortcuts import render

from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView
from knox.auth import TokenAuthentication as KnoxTokenAuthentication
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView

from .serializers import UserSerializer, RegisterSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        print(KnoxTokenAuthentication())

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class CheckAuthentication(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        try:
            user = request.user
            # If the user is authenticated, return a 200 status code
            return Response({'detail': 'Authenticated'}, status=200)
        except Exception:
            # If the token is not valid, log out the user and return a 401 status code
            LogoutView.as_view()(request._request)
            return Response({'detail': 'Invalid token. Please log in again.'}, status=401)

