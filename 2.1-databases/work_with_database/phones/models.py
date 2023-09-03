from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=None)
    image = models.URLField(default=None)
    release_date = models.DateTimeField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(default=None)

    def __str__(self):
        return f"{self.id};" \
               f" {self.name};" \
               f" {self.price};" \
               f" {self.image};" \
               f" {self.release_date};" \
               f" {self.lte_exists};" \
               f" {self.slug}"

