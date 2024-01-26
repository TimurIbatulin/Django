from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefon_number = models.IntegerField()
    adress = models.TextField()
    Clientregistration_date = models.DateTimeField()

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, telefon: {self.telefon_number}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    data_add_product = models.DateTimeField()


class order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_prise_order = models.DecimalField(max_digits=8, decimal_places=2)
    data_order = models.DateTimeField()
