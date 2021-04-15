from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse



class Book(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    book_title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=20)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    book_cover = models.FileField()

    
    def get_absolute_url(self):
        return reverse("book:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.book_title