from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


# Create your models here.
class Address(models.Model):
    """
    Model representing an address.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        String representation of an Address.
        """
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Adresses"


class Letting(models.Model):
    """
    Model representing a letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of a Letting.
        """
        return self.title
