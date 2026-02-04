from rest_framework.views import APIView
from rest_framework.decorators import api_view, APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Item , Product
from .serializers import ItemsQueryParamsSerializer, ItemSerializer ,ProductSerializer ,ProductsQueryParamsSerializer



class ItemListView(APIView):
    
    def get(self, request: Request) -> Response:
        

        query_params = request.query_params

        query_serializer = ItemsQueryParamsSerializer(data=query_params)

        if query_serializer.is_valid(raise_exception=True):
            
            items = Item.objects.all()

            item_serializer = ItemSerializer(items, many=True)

            return Response(item_serializer.data, status=status.HTTP_200_OK)

        return Response(data="error", status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request: Request) -> Response:
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        
        item = Item.objects.create(
            name=serializer.validated_data['name'],
            desc=serializer.validated_data['desc'],
            category=serializer.validated_data['category'],
            price=serializer.validated_data['price'],
            is_active=serializer.validated_data['is_active'],
        )

        response_serializer = ItemSerializer(item)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
class ItemDetailView(APIView):
    
    def get(self, request: Request, pk: int) -> Response:

        item = Item.objects.filter(pk=pk).first()
        if item:
            serializer = ItemSerializer(item)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'no item'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request: Request, pk: int) -> Response:
        item = Item.objects.filter(pk=pk).first()
        if not item:
            return Response({'error': 'no item'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

      
        for field, value in serializer.validated_data.items():
            setattr(item, field, value)
        item.save()

        response_serializer = ItemSerializer(item)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        item = Item.objects.filter(pk=pk).first()
        if not item:
            return Response({'error': 'no item'}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# client(chrome, js, postman) -> WSGI -> URL -> View (HttpRequest) -> APIView (Request)
# client(chrome, js, postman) <- WSGI -> URL <- View (HttpResponse) <- APIView (Response)

class ProductListView(APIView):
    
    def get(self, request: Request) -> Response:
        

        query_params = request.query_params

        query_serializer = ProductsQueryParamsSerializer(data=query_params)

        if query_serializer.is_valid(raise_exception=True):
            
            products = Product.objects.all()

            product_serializer = ProductSerializer(products, many=True)

            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(data="error", status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request: Request) -> Response:
        data = request.data

        product_serializer = ProductSerializer(data=data)
        if product_serializer.is_valid(raise_exception=True):
            validated_data = product_serializer.validated_data

            product = Product(
                name=validated_data['name'],
                desc=validated_data['desc'],
                price=validated_data['price'],
                category=validated_data['category'],
                is_active=validated_data['is_active'],
                stock=validated_data['stock'],
            )
            product.save()

            response_serializer = ProductSerializer(product)

            return Response(response_serializer.data)
        
class ProductDetailView(APIView):

    def get(self, request: Request, pk: int) -> Response:
        product = Product.objects.filter(pk=pk).first()
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'no product'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, pk: int) -> Response:
        product = Product.objects.filter(pk=pk).first()
        if not product:
            return Response({'error': 'no product'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

       
        for field, value in serializer.validated_data.items():
            setattr(product, field, value)
        product.save()

        response_serializer = ProductSerializer(product)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        product = Product.objects.filter(pk=pk).first()
        if not product:
            return Response({'error': 'no product'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        