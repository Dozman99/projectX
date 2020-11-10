from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:

        # this defines what data in the model we want to work with
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
        model = Post
