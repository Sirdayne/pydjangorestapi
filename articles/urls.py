from django.urls import path
from articles.views import *

app_name = 'article'
urlpatterns = [
    path('create/', ArticleCreateView.as_view()),
    path('list/', ArticleListView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view())
]