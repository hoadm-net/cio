from django.urls import path
from .views import sentiment_analyze, dependency_parsing

urlpatterns = [
    path('api/v1/sentiment_analyze', sentiment_analyze, name='sentiment_analyze'),
    path('api/v1/dependency_parsing', dependency_parsing, name='dependency_parsing')
]
