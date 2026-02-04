from rest_framework import serializers




class ItemsQueryParamsSerializer(serializers.Serializer):
    min_price = serializers.IntegerField(required=False)
    max_price = serializers.IntegerField(required=False)
    category = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)



class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    is_active = serializers.BooleanField()

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    is_active = serializers.BooleanField()
    stock= serializers.IntegerField()



class ProductsQueryParamsSerializer(serializers.Serializer):
    min_price = serializers.IntegerField(required=False)
    max_price = serializers.IntegerField(required=False)
    category = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
    stock = serializers.IntegerField(required=False)    

