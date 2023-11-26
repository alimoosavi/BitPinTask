from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.CharField(max_length=200, null=False, blank=False)
    total_scores_count = models.IntegerField(default=0)
    total_scores_summation = models.IntegerField(default=0)

    @property
    def average_ratings(self):
        if self.total_scores_count == 0:
            return 0
        return self.total_scores_summation / self.total_scores_count


class Score(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    score = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=0),
            MaxValueValidator(limit_value=5)
        ]
    )

    class Meta:
        unique_together = ('article', 'user',)
