from .serializers import BookSerializer
from rest_framework import generics, permissions
from books.models import Book
from rest_framework.exceptions import ValidationError

class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer