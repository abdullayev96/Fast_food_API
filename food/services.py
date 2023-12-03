from django.db import connection
from contextlib import closing
from collections import OrderedDict
import json
from rest_framework.exceptions import NotFound




def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_category_product():
    category_products = query_category_products()
    items = []
    for category_product in category_products:
        items.append(
            OrderedDict(
                {
                    "id":category_product['id'],
                    "title":category_product['title'],
                    "products": json.loads(category_product['products'])
                }
            )
        )
    return items

def query_category_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """WITH table1 AS (SELECT c.*, (SELECT JSONB_AGG(v) FROM (SELECT food_product.* FROM food_product WHERE 
            food_product.category_id = c.id) v) AS products FROM food_category c)
            SELECT table1.* from table1 where table1.products is not null;"""
        )
        category_products = dictfetchall(cursor)
    return category_products


def get_customer_by_phone(phone_number):
    customers = query_customers(phone_number)
    items = []
    for customer in customers:
        items.append(
            OrderedDict(
                {
                    "phone_number": customer['phone_number'],
                    "first_name": customer['first_name'],
                    "last_name": customer['last_name'],
                    "create_at": customer['create_at'],

                    "customers": json.loads(customer['customers'])
                }
            )
        )
    return items


def query_customers(customer_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """SELECT * FROM food_customer WHERE phone_number = %s """, [customer_id]
        )
        category_products = dictfetchall(cursor)
    return category_products


def get_products_by_ids(ids):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            f"""SELECT * FROM food_product WHERE id in ({str(ids).strip("[]")})"""
        )
        products = dictfetchall(cursor)
    return products
