from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAuthenticated
from .models import Card
from .serializers import CardSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class SmallCursorPagination(CursorPagination):
    page_size = 3
    ordering = '-id'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = SmallCursorPagination

    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]



class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pagination_class = SmallCursorPagination

    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


