from ..models import *
from rest_framework import serializers


class AmounOfVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'amount_of_votes',
        ]

class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'article_content',
            'author_name',
        ]

class DeleteArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'




