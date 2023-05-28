from rest_framework import serializers
from .models import product, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = product
        fields = '__all__'



# from rest_framework import serializers
#
# from show_product.models import product, Comment
#
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
# class ProductSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = product
#         fields = '__all__'