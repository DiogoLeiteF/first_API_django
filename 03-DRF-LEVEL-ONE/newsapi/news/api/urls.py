from django.urls import path

from news.api.views import article_list_create_api_view, article_details_api_view


urlpatterns = [
    path("articles/", article_list_create_api_view, name="articles-list"),
    path("articles/<int:pk>/", article_details_api_view, name="articles-detail")
]
