from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY=(
    ('Papelería','Papelería'),
    ('Electrónicos','Electrónicos'),
    ('Materiales de Construcción','Materiales de Construcción'),
    ('Herramientas','Herramientas'),
    
)
class Product(models.Model):
    name= models.CharField(max_length=100, null=True)
    category=models.CharField(max_length=30, choices=CATEGORY, null=True)
    quantity=models.PositiveIntegerField (null=True)

    class   Meta:
        verbose_name_plural= 'Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff=models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    order_quantity=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('denegada', 'Denegada'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendiente'
    )

    class   Meta:
        verbose_name_plural= 'Order'


    def __str__(self):
        return f'{self.product} ordered by {self.staff.username if self.staff else "Unknown"}'