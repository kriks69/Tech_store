from django.db import models
from django.contrib.auth.models import User
from show_product.models import product


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username