from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    books_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average_rating = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
