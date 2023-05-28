from django.shortcuts import render
from rest_framework import viewsets

from auth_app.models import User_Profile
from auth_app.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User_Profile.objects.all()
    serializer_class = UserProfileSerializer