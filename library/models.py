from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(blank=True, null=True)
    ISBN = models.CharField(max_length=200, unique=True)
    availability_status = models.BooleanField(default=True)

class Author(models.Model):
    book = models.ManyToManyField(Book)
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

class Member(AbstractUser):
    email= models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()