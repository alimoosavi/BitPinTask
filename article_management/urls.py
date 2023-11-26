from django.urls import path
from article_management.views import ScoreCreateAndUpdateViewSet, ArticleListViewSet, ArticleRetrieveViewSet

urlpatterns = [
    path('score/', ScoreCreateAndUpdateViewSet.as_view(), name='scoring'),
    path('article/', ArticleListViewSet.as_view(), name='article-list'),
    path('article-details/<int:pk>/', ArticleRetrieveViewSet.as_view(), name='article-detail'),
]
