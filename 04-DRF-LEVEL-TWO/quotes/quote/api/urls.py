from rest_framework.urls import path

from quote.api.views import QuoteListAPIView, QuoteDetailAPIView


urlpatterns = [
    path("quote/", QuoteListAPIView.as_view(), name="quote-list"),
    path("quote/<int:pk>/", QuoteDetailAPIView.as_view(), name="quote-detail"),
]
