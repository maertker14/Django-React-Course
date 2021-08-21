from django.db import models


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


# Create your models here.
class Book(models.Model):  # blank or default almost always has to be within the fields parameters
    title = models.CharField(max_length=41, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    # cover2 = models.ImageField(upload_to='covers/', blank=True)
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):  # allows this class to be called as a string
        return self.title
