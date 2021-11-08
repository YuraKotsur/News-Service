from django.http import HttpResponse
from django.shortcuts import render
from .models import *

from django.template import Context

def main(request):
    article = Article.objects.all()

    context = {
        'article': article,
    }
    return render(request, 'newspage.html', context = context)

def articlepage(request, pk, context={}):
    if request.method == 'GET':
        article = Article.objects.all().filter(pk=pk)
        context = {
            'article': article,
            'pk': pk,
            'url': 'http://localhost:8000/article/' + pk + '/upvote'
        }
        return render(request, "articlepage.html", context = context)

def vote(request, pk):
    if request.method == 'GET':
        article = Article.objects.all().get(pk=pk)
        article.amount_of_votes += 1
        article.save()
        context = {
            'article': article,
            'pk':pk,
            'url': 'article/' + pk
        }

        return articlepage(request, pk, context=context)



