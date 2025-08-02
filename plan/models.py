from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Register Plan"
        verbose_name_plural = "Register Plan"