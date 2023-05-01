from django.db import models

# Create your models here.
class Cats(models.Model):
    name = models.CharField("Имя кота", max_length=20)
    description = models.TextField("Описание")
    breed = models.CharField("Порода", max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.id}"

    class Meta:
        verbose_name = "Кот"
        verbose_name_plural = "Коты"