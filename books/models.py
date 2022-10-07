from django.db import models
from django.utils import timezone
# Create your models here.





class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField( max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=100)

    image = models.ImageField(null=False, blank=False, upload_to = 'images/')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    
    def __str__(self) -> str:
        return f'{self.title}'

    
    class Meta:
        ordering = ['-created_at']