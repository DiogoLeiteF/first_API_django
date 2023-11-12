from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from quote.models import Quote
from quote.api.serializers import QuoteSerializer
from quote.api.pagination import UserPagination
from quote.api.permissions import IsAdmminUserOrReadOnly


class QuoteListAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdmminUserOrReadOnly]
    pagination_class = UserPagination


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [
        IsAdminUser,
    ]
