from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Museum(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country})"

class Painting(models.Model):
    name = models.CharField(max_length=200)
    creating_year = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
