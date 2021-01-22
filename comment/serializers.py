from rest_framework import serializers

from .models import Comment
from account.serializers import UserSerializer



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'product')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user
        comment = Comment.objects.create(**validated_data)
        return comment


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = UserSerializer(instance.author_id).data
        return representation


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author_id', 'id', 'text', 'product')