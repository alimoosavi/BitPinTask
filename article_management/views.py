from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from article_management.models import Score, Article
from article_management.serializers import ScoreSerializer, ArticleListSerializer


class ScoreCreateAndUpdateViewSet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Score.objects.filter(self.request.user)

    serializer_class = ScoreSerializer


class ArticleListViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
