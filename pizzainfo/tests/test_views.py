import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from pizzainfo.models import Pizza

@pytest.mark.django_db
def test_get_pizzas():
    client = APIClient()
    url = reverse('pizza-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_pizza():
    client = APIClient()
    url = reverse('pizza-list')
    data = {
        "name": "Pepperoni",
        "description": "Pizza with pepperoni and cheese",
        "price": "12.99"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Pizza.objects.count() == 1
    assert Pizza.objects.get().name == "Pepperoni"