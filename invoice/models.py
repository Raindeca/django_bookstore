from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import date
from book.models import Book

# Create your models here.

class Payment(models.Model):
    payment_method = models.CharField(max_length=10)

    def __str__(self):
        return self.payment_method

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_date = models.DateField(default=date.today)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(Payment, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.id + ' ' + self.invoice_date + ' ' + self.item