from django.db import models

# Create your models here.


class PDF(models.Model):
    pass


class TagClass(models.Model):
    name = models.TextField()


class Tag(models.Model):
    tag_class = models.ForeignKey(TagClass, on_delete=models.CASCADE)
    name = models.TextField()
