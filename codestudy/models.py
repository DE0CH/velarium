from django.db import models
from django.dispatch import receiver
import uuid
# Create your models here.


class TagClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag_class = models.ForeignKey(TagClass, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class Paper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    description = models.TextField()
    text = models.TextField()
    png = models.FileField(default='failed.png')
    pdf = models.FileField(default='failed.pdf')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class User(models.Model):
    id = models.TextField(primary_key=True, editable=False)
    name = models.TextField()
    given_name = models.TextField()
    family_name = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.name
