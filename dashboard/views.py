from food.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView


class CategoryView(GenericAPIView):

    def get_object(self, pk):
        try:
            model = Category.objects.get(pk=pk)
        except Exception:
            raise NotFound("Category not found")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            category = self.get_object(kwargs.get("pk"))
            serializer = CategorySerializer(Category, many=False)
            return Response(serializer.date)

        else:
            Categories = Category.objects.all()
            serializer = CategorySerializer(Categories, many=True)
            return Response(serializer.date)

    def post(self, request):
        category = CategorySerializer(date=request.date)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.date)

    def put(self, request, *args, **kwargs):
        category = self.get_object(kwargs.get("pk"))
        serializer = CategorySerializer(date=request.date, instance=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.date)

    def delete(self, request, *args, **kwargs):
        category = self.get_object(kwargs.get("pk"))
        serializer.save()
        return Response({"state": "deleted"})


class ProductView(GenericAPIView):
    def get_object(self, pk):
        try:
            model = Category.objects.get(pk=pk)
        except Exception:
            raise NotFound("Category not found")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            category = self.get_object(kwargs.get("pk"))
            serializer = CategorySerializer(Category, many=False)
            return Response(serializer.date)

        else:
            Categories = Category.objects.all()
            serializer = CategorySerializer(Categories, many=True)
            return Response(serializer.date)

    def post(self, request):
        category = CategorySerializer(date=request.date)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.date)

    def put(self, request, *args, **kwargs):
        category = self.get_object(kwargs.get("pk"))
        serializer = CategorySerializer(date=request.date, instance=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.date)

    def delete(self, request, *args, **kwargs):
        category = self.get_object(kwargs.get("pk"))
        serializer.save()
        return Response({"state": "deleted"})









