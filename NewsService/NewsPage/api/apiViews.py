from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import *



@api_view(['GET'])
def article_list(request, pk):

    if request.method == 'GET':
        article = Article.objects.all().filter(pk=pk)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def vote(request, pk):
    try:
        article = Article.objects.all().get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        article.amount_of_votes += 1
        article.save()
        serializers = AmounOfVoteSerializer(article, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_article(request):
    try:
        article = Article.objects.all()
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = CreateArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_article(request, pk):

    try:
        article = Article.objects.all().get(pk=pk)
    except Article.DoesNotExist:
        return Response('there is no article with this id:' + pk, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        article.delete()
        return Response('Article was successfuly deleted')


@api_view(['PUT'])
def article_edit(request, pk):
    try:
        article = Article.objects.all().get(pk=pk)
    except Article.DoesNotExist:
        return Response('there is no article with this id:' + pk, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if request.method == 'PUT':
            article.amount_of_votes += 1
            article.save()
            serializers = EditArticleSerializer(article, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)










