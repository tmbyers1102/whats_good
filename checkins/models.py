from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import CharField

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Checkin(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=120)
    publish_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.location_name