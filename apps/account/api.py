# Django imports
from django.contrib.auth.hashers import make_password

# 3 party imports
from rest_framework import viewsets, mixins

# aydoor imports
from .models import User
from .serializers import UserSerializer


class AccountViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def create(self, request):

        request.data.update({
            'password': make_password(request.data.get("password")),
        })

        return super(AccountViewSet, self).create(request)