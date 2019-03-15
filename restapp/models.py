from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Hotel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    star_num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])