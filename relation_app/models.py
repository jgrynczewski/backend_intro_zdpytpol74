from django.db import models


# One-to-one relation
class Country(models.Model):
    name = models.CharField(max_length=128)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)

    def __str__(self):
        return f"Country: [{self.id}] {self.name}"


class Capital(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"Captial: [{self.id}] self.name"


# One-to-many relation
class Language(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} [{self.id}]"


class Framework(models.Model):
    name = models.CharField(max_length=64)
    language = models.ForeignKey("Language", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} [{self.id}]"


# Many-to-many
class Actor(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} [{self.id}]"


class Movie(models.Model):
    name = models.CharField(max_length=128)
    actors = models.ManyToManyField("Actor")

    def __str__(self):
        return f"{self.name} [{self.id}]"
