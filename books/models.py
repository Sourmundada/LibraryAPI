from django.db import models

# Book Model.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13) 

    def __str__(self):
        return self.title

