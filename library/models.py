from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(blank=True, null=True)
    ISBN = models.CharField(max_length=20, unique=True)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    books = models.ManyToManyField(Book, related_name='authors')
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Member(AbstractUser):
    email= models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+[1-9]\d{1,14}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )

    def __str__(self):
        return f"{self.username}"
    
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} {self.member} {self.borrow_date}"