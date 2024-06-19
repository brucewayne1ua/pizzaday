import pytest
from pizzainfo.models import Pizza

@pytest.mark.django_db
def test_pizza_creation():
    pizza = Pizza.objects.create(
        name="Margherita",
        description="Classic pizza with tomato and mozzarella",
        price=9.99
    )
    assert pizza.name == "Margherita"
    assert pizza.description == "Classic pizza with tomato and mozzarella"
    assert pizza.price == 9.99