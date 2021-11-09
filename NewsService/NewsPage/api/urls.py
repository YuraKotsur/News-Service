from django.urls import path
from .apiViews import *


urlpatterns = [
    path('news_page_api_view', newsPageView),
    path('article/<str:pk>/vote', vote),
    path('article_create', create_article),
    path('article_delete/<str:pk>', delete_article),
    path('article_edit/<str:pk>', article_edit),
]