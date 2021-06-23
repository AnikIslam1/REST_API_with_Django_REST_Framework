from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255)
    num_page = models.IntegerField(default = 0)
    isbn13 = models.name = models.CharField(max_length = 13, blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    