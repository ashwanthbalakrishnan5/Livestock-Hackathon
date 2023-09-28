from django.db import models


class Animals(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name


class Breeds(models.Model):
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    breed_name = models.CharField(max_length=100)
    short_description = models.TextField()

    def __str__(self):
        return self.animal.name + " - " + self.breed_name


class Info(models.Model):
    breed = models.ForeignKey(Breeds, on_delete=models.CASCADE)
    description = models.TextField()
    habbitual_climate = models.CharField(max_length=100)

    morning_feed = models.TextField()
    afternoon_feed = models.TextField()
    night_feed = models.TextField()

    care = models.JSONField()

    def __str__(self):
        return self.breed.animal.name + " - " + self.breed.breed_name + "[Info]"
