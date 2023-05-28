from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.name