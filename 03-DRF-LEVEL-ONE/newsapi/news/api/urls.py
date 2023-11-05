from django.urls import path

# from news.api.views import article_list_create_api_view, article_details_api_view
from news.api.views import ArticleListCreateAPIView, ArticleDetailAPIView


urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="articles-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="articles-detail")
    # path("articles/", article_list_create_api_view, name="articles-list"),
    # path("articles/<int:pk>/", article_details_api_view, name="articles-detail")
]
