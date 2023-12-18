from django.db import models


class Message(models.Model):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=10, choices=CHOICES)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
