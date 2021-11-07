from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from ..models import Article

def article_GET(request, pk):
    article = Article.objects.filter(pk=pk)
    serializer = ArticleSerializer(article, many=True)
    return Response(serializer.data)


def article_POST(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)