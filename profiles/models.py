from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (User): The associated user for this profile.
        favorite_city (str): The favorite city of the user (optional).

    Methods:
        __str__(): Returns the username of the associated user.

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
