from django.db import models
from django.urls import reverse


# Create your models here.

class Customer(models.Model):
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100)
    add3 = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    registered = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.forename)

    def full_name(self):
        return '%s %s' % (self.forename, self.surname)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('customer', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField("imageCat")
    price = models.FloatField()

    def __str__(self):
        return '%s' % (self.name)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    payment_type = models.CharField(max_length=100)
    date = models.DateField("ngay dat hang")
    status = models.TextField(max_length=200)

    def __str__(self):
        return '%s' % (self.customer)

    def get_absolute_url(self):
        return reverse('updateOrder', kwargs={'pk': self.pk})


class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    quanlity = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.order.customer)
