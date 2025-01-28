from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField('Author')
    year = models.IntegerField()
    genre = models.ForeignKey('Genre', on_delete=models.RESTRICT)
    publisher = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='author_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name