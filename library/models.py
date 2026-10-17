from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField(blank=True, null=True)
    ISBN = models.BigIntegerField(unique=True)
    availability_status = models.BooleanField(default=True)

class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)

class Member(models.Model):
    name = models.CharField(max_length=200) 
    email= models.EmailField(max_length=200, unique=True)
    contact_number= models.IntegerField()

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()