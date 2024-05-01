from rest_framework import serializers
from .models import Product
from accounts.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    def get_author(self, obj):
        return obj.author.username
    
    class Meta:
        model = Product
        fields = "__all__"
