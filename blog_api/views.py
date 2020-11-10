# from django.shortcuts import render
# we dont need the render
from blog.models import Post
from rest_framework import generics
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    # queryset= Post.objects.all()
    # returns all the post that are flaged as published
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


""" Concrete View Classes
#CreateAPIView
used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instance
#RetriveAPIView
used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
#ListCreateAPIView
Used for read-write endpoints to represent a collection of model instance.
RetriveUpdateAPIView
#Used for read or update endpoints to represent a single model instance
RetriveDestroyAPIView
#Used for read or delete endpoints to represent a single model instance
RetriveUpdateDestroyAPIView
#Used for read-write-delete endpoints to represent a single model instance

"""
