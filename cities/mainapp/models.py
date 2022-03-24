from django.db import models
from django.urls import reverse
from django.db.models import ForeignKey, CharField, SlugField
from django.db.models.deletion import SET_NULL


class City(models.Model):

    name = CharField(max_length=50, verbose_name='Название', unique=True)
    slug = SlugField(max_length=50, unique=True)

    def get_absolute_url(self) -> str:
        return reverse('city', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return self.name

    class Meta:

        verbose_name='город'
        verbose_name_plural='города'


class Citizen(models.Model):

    full_name = CharField(max_length=50, verbose_name='ФИО')
    city = ForeignKey(
        City,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        verbose_name='город',
        related_name='citizens',
    )

    def get_absolute_url(self) -> str:
        return reverse('citizen', args=[self.pk])

    def __str__(self) -> str:
        return self.full_name

    class Meta:

        verbose_name='гражданин'
        verbose_name_plural='граждане'
