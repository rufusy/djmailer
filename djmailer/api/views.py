from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import permissions

from .SubscriberSerializer import SubsciberSerializer
from .models import Subscriber


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubsciberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = (IsAuthenticated,)


@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'GET':
        return Response({"message":"Hello world"})

    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error":"Login Failed"},status=HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"Token":token.key})


# authentication example from DRF docs
class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        if not username:
            return None
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")

        return (user, None)


# global permission from DRF docs
class BlackListPermission(permissions.BasePermission):
    # Check for blacklisted IP addresses
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted


# per object permission from DRf docs
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions re allowed to any request
        # So we'll always allow GET, READ OR OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named owner
        return obj.owner == request.user


   


