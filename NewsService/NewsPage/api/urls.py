from django.urls import path
from .apiViews import *


urlpatterns = [
    path('api/<str:pk>', article_list),
    path('api/<str:pk>/vote', vote),
    path('article_create', create_article),
    path('article_delete/<str:pk>', delete_article),
    path('article_edit/<str:pk>', article_edit),
]