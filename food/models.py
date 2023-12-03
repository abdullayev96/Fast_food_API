from django.db import models
from django.utils.text import slugify
from baseapp.models import BaseModel



class Category(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, blank=False, unique=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name=  "Kategoriya_"


class Product(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    cost = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/products')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mahsulot_"


class Customer(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name}{self.last_name}"



class Order(BaseModel):
    payment_type = models.IntegerField()
    status = models.IntegerField()
    address = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Haridor_"


class OrderProduct(BaseModel):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Haridor_tavari_"





