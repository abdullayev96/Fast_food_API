from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .import services
from rest_framework.exceptions import NotFound
from .serializers import CustomerOrderSerializer



class CategoryProductAPI(GenericAPIView):
    def get(self, request, *args, **kwargs ):
        category_products = services.get_category_product()

        return Response(category_products)



class CustomerAPI(GenericAPIView):
    def get(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            raise NotFound("Mavjud bolmagan raqam!")
        customer = services.query_customers(phone_number)
        return Response(customer)



class CustomerOrderAPI(GenericAPIView):
    def post(self, request):
        serializer = CustomerOrderSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class ProductAPI(GenericAPIView):
    def get(self, request):
        ids = request.query_params.getlist("ids[]")
        if not ids:
            raise NotFound("Empty array")
        products = services.get_products_by_ids(ids)
        return Response(products)

