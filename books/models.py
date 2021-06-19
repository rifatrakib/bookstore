from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

CATEGORIES = (
    ('Novel', 'Novel'),
    ('Academic', 'Academic'),
    ('Action & Adventure', 'Action & Adventure'),
    ('Classic', 'Classic'),
    ('Mystery', 'Mystery'),
    ('Fantasy', 'Fantasy'),
    ('Fiction', 'Fiction'),
    ('Horror', 'Horror'),
    ('Romance', 'Romance'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Thriller', 'Thriller'),
    ('Biography', 'Biography'),
    ('Literature', 'Literature'),
)


class Author(models.Model):
    author_name = models.CharField(max_length=250)
    biography = models.TextField(default='', null=True)

    def __str__(self) -> str:
        return self.author_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)
    establish_date = models.DateTimeField('est')
    address = models.TextField()

    def __str__(self) -> str:
        return self.publisher_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    publication_date = models.DateTimeField('Publishing date')
    page_count = models.IntegerField(default=0)
    description = models.TextField()
    stock = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), ]
    )

    def __str__(self) -> str:
        return self.book_name


class Rating(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )
    comment = models.TextField(
        default='', null=True,
    )
    time = models.DateTimeField(auto_now_add=True)
