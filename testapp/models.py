from django.db import models
from django.utils import timezone
# Create your models here.

class EbookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.DateField(default=timezone.now)
    publisher = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers/')
    books_pdf = models.FileField(upload_to='pdfs/')

    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return f"Tittle > {self.title}"

    # delete from the directory also

