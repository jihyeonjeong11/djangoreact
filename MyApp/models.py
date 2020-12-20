from django.db import models
from django.utils import timezone

# this is many to many relation model.

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ('title',)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    Publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline


    class Meta:
        ordering = ('headline',)



# this is many to one relation model.

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class ArticleOne(models.Model):
    headline = models.CharField(max_length=30)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

# this is one to one relation model.

class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.place.name