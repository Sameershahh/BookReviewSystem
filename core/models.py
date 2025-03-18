from django.db import models


class Book(models.Model):
    GENRE_CHOICE = [
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Sci-Fi', 'Science Fiction'),
    ('Mystery', 'Mystery'),
    ('Fantasy', 'Fantasy'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField(unique=True)
    genre = models.CharField(max_length=200, choices=GENRE_CHOICE)
    publication_date = models.DateField()
    rating = models.DecimalField( max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.title
    