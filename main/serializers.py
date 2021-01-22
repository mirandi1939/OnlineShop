from rest_framework import serializers

from .models import *
from comment.serializers import CommentDetailSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")


class ProductSerializer(serializers.ModelSerializer):
    commentaries = CommentDetailSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'categories', 'stock', 'commentaries')


    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'author_id', 'stock', 'commentaries')


    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        representation['categories'] = CategorySerializer(instance.categories.all(), many=True).data
        return representation


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'categories', 'stock')



class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'categories', 'stock')
