
import pytest
from pizzainfo.serializers import PizzaSerializer
from pizzainfo.models import Pizza

@pytest.mark.django_db
def test_pizza_serializer():
    pizza = Pizza.objects.create(
        name="Margherita",
        description="Classic pizza with tomato and mozzarella",
        price=9.99
    )
    serializer = PizzaSerializer(pizza)
    data = serializer.data
    assert data['name'] == "Margherita"
    assert data['description'] == "Classic pizza with tomato and mozzarella"
    assert data['price'] == "9.99"  # Значение должно быть строкой, так как это DecimalField