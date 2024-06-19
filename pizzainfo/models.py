from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pizzas')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.customer_name}'

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity}x {self.pizza.name} for {self.order.customer_name}'
