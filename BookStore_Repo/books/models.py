from django.db import models
from django.core.validators import MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    brief = models.TextField()                                        
    image = models.ImageField(upload_to="books/", null=True, blank=True)
    no_of_page = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.id})"