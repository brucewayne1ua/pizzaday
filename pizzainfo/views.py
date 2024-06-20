from rest_framework import viewsets
from .models import Pizza
from .serializers import PizzaSerializer
from .permissions import IsAdminOrReadOnly

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [IsAdminOrReadOnly]