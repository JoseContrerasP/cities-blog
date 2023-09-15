from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    description = models.TextField()
    population = models.IntegerField(default=3000000)
    image = models.ImageField(upload_to="city/photos")

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class Like_comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
