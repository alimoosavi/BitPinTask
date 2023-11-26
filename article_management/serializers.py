from django.db import transaction
from rest_framework import serializers
from article_management.models import Article, Score


class ScoreSerializer(serializers.Serializer):
    article = serializers.IntegerField(required=True)
    score = serializers.IntegerField(required=True)

    def validate(self, attrs):
        if not Article.objects.filter(id=attrs['article']).exists():
            raise serializers.ValidationError({"article": "Article doesn't exist."})
        if not (0 <= attrs['score'] <= 5):
            raise serializers.ValidationError({"score": "Score must be in range of 0 upto 5."})
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        article_id = validated_data['article']
        article_obj = Article.objects.filter(id=article_id).first()
        current_score = validated_data['score']
        previous_score = 0
        with transaction.atomic():
            if Score.objects.filter(user=user, article_id=article_id).exists():
                score_obj = Score.objects.filter(user=user, article_id=article_id).first()
                previous_score = score_obj.score
                score_obj.score = current_score
                score_obj.save()
            else:
                Score.objects.create(
                    article_id=article_id,
                    user=user,
                    score=current_score
                )
                article_obj.total_scores_count += 1

            article_obj.total_scores_summation += (current_score - previous_score)
            article_obj.save()

        return {'article': article_id, 'score': current_score}


class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    total_scores_count = serializers.IntegerField()
    average_ratings = serializers.FloatField()
    user_rating = serializers.IntegerField(allow_null=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        article_id = data['id']

        if Score.objects.filter(user=user, article_id=article_id).exists():
            data['user_rating'] = Score.objects.filter(user=user, article_id=article_id).first().score

        return data
