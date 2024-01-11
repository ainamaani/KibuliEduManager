from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    isbn = models.CharField(max_length=18)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    number_of_pages = models.PositiveSmallIntegerField()
    description = models.TextField()
    publication_date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30)
    language = models.CharField(max_length=20)
    edition = models.PositiveSmallIntegerField()
    number_of_copies = models.PositiveSmallIntegerField()
    availability_status = models.CharField(max_length=10, choices=[('available','Available'),('borrowed','Borrowed')])

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
