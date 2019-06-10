from django.shortcuts import render
from rest_framework import generics
from articles.serializers import ArticleDetailSerializer, ArticleListSerializer
from articles.models import Article
from articles.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializer


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()
    permission_classes = (IsAuthenticated, )


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
