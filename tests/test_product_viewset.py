from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
import json

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory
from product.models.product import Product
from order.models.order import Order

class TestProductViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        token.save()

        self.product = ProductFactory(
            title= 'smartphone',
            price=650.00,
        )

    def test_all_products(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(
            reverse('product-list' , kwargs={'version' : 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)
        self.assertEqual(product_data['results'][0]['title'], self.product.title)
        self.assertEqual(product_data['results'][0]['price'], self.product.price)
        self.assertEqual(product_data['results'][0]['active'], self.product.active)

    def test_create_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        category = CategoryFactory()
        data = json.dumps({
            'title' : 'TV',
            'price' : 800.00,   
            'categories_id': [ category.id ]
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version' : 'v1'}),
            data=data,
            content_type = 'application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_product = Product.objects.get(title='TV')

        self.assertEqual(created_product.title, 'TV')
        self.assertEqual(created_product.price, 800.00)