from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.meals.pagination import ReactAdminPagination


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "is_staff"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = ReactAdminPagination

