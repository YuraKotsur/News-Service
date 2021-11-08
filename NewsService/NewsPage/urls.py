from django.urls import path
from .views import *



urlpatterns = [
    path('news', main, name='base'),
    path('article/<str:pk>', articlepage),
    path('article/<str:pk>/upvote', vote)
]