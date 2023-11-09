from django.urls import path

# from news.api.views import article_list_create_api_view, article_details_api_view
from news.api.views import (
    ArticleListCreateAPIView,
    ArticleDetailAPIView,
    JounalistListCreateAPIView,
)


urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="articles-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("journalists/", JounalistListCreateAPIView.as_view(), name="journalists-list"),
    # path(
    #     "journalists/<int:pk>/", ArticleDetailAPIView.as_view(), name="journalists-detail"
    # ),
    # path("articles/", article_list_create_api_view, name="articles-list"),
    # path("articles/<int:pk>/", article_details_api_view, name="articles-detail")
]
