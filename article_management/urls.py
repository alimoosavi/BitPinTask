from django.urls import path
from article_management.views import ScoreCreateAndUpdateViewSet, ArticleListViewSet

urlpatterns = [
    path('score/', ScoreCreateAndUpdateViewSet.as_view(), name='scoring'),
    path('article/', ArticleListViewSet.as_view(), name='article-list'),
]
