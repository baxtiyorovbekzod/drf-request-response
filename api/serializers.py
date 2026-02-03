from rest_framework import serializers

from .models import Item


class ItemsQueryParamsSerializer(serializers.Serializer):
    min_price = serializers.IntegerField()
    max_price = serializers.IntegerField()
    category = serializers.CharField()
    is_active = serializers.BooleanField()


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        item = Item(
            name=validated_data['name'],
            desc=validated_data['desc'],
            price=validated_data['price'],
            category=validated_data['category'],
            is_active=validated_data['is_active'],
        )
        item.save()
        return item
    