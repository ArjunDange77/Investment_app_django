from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name

class ProductMaster(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class Investment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer} - {self.product} - {self.investment_amount}"
