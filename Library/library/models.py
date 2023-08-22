from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed')
    )
    book_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    GENRE_CHOICES = (
        ('fantasy', 'Fantasy'),
        ('action & adventure', 'Action & Adventure'),
        ('mystery', 'Mystery'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller & suspense', 'Thriller & Suspense'),
        ('historical fiction', 'Historical Fiction'),
        ('young adult', 'Young Adult'),
        ('graphic novel', 'Graphic Novel'),
        ('self help', 'Self help'),
        ('history', 'History')
    )
    book_genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='fantasy')


    def __str__(self):
        return self.title
