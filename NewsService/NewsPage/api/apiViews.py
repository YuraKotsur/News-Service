from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .apifunctions import *
from .serializer import *
from ..models import *


@api_view(['GET','POST'])
def article(request, pk):

    if request.method == 'GET':
        return article_GET(request, pk)

    elif request.method == 'POST':
        return article_POST(request)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#
#     try:
#         article = Post.objects.filter(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data )
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
