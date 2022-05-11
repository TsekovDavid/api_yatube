from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "group", "pub_date")
        read_only_fields = ("pub_date", "group")


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field="username"
    )

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
        read_only_fields = ("post",)
