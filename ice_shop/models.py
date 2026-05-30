from django.db import models


class IceCream(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название")
    description = models.TextField(
        max_length=500,
        verbose_name="Описание"
    )
    price = models.IntegerField(
        verbose_name="Цена"
    )
    photo = models.ImageField(
        upload_to='media/'
    )

    def __str__(self):
        return self.title
