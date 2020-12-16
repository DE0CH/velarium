from django.db import models
from django.dispatch import receiver
# Create your models here.


class TagClass(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_class = models.ForeignKey(TagClass, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class Paper(models.Model):
    title = models.TextField()
    description = models.TextField()
    text = models.TextField()
    png = models.FileField()
    pdf = models.FileField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


@receiver(models.signals.post_delete, sender=Paper)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Paper` object is deleted.
    """
    instance.pdf.delete(save=False)
