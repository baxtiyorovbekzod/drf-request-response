from rest_framework import serializers




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

class ProductsQueryParamsSerializer(serializers.Serializer):
    min_price = serializers.IntegerField()
    max_price = serializers.IntegerField()
    category = serializers.CharField()
    is_active = serializers.BooleanField()


class Productserializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    is_active = serializers.BooleanField()
    stock= serializers.IntegerField()    

