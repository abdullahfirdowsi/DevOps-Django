from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    pub_date=models.DateField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def is_expensive(self):
        if self.price>200:
            return True
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    is_enrolled = models.BooleanField()
    def is_passing(self):
        if self.grade>='C':
            return True
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveBigIntegerField()
    def calculate_total_cost(self):
        total=self.price*self.quantity
        return total
class Order(models.Model):
    order_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def is_high_value(self):
        return self.total_amount > 1000
class Productdetail(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.TextField()
    def __str__(self):
        return self.name