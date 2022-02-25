from django.db import models
import uuid
from django.contrib.auth.models import User

# Register your models here.
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        return f'{self.id}pus genre is {self.name}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField('Genre')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=13, unique=True)

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'Author Name is {self.first_name} {self.last_name}'


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Student(models.Model):
    name = models.CharField(max_length=20)
