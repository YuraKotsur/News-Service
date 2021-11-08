from django.urls import path
from .apiViews import *

urlpatterns = [
    path('api/<str:pk>', article_list),
    path('api-create', article_detail),
]