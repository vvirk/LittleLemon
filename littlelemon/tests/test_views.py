from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=50, inventory=20)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/items/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)