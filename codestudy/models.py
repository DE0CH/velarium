from django.db import models
import uuid
from enum import IntEnum
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

    def is_bookmarked(self, user):
        return self.bookmarkers.filter(pk=user.pk).exists()

    def __str__(self):
        return self.title

    @property
    def nested_tag_names(self):
        tag_classes = {}
        for tag in self.tags.all():
            if tag.tag_class.name not in tag_classes:
                tag_classes[tag.tag_class.name] = []
            tag_classes[tag.tag_class.name].append(tag.name)
        return tag_classes


class UserType(IntEnum):
    STANDARD = 1
    EDITOR = 2
    ADMIN = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class User(models.Model):
    id = models.TextField(primary_key=True, editable=False)
    type = models.IntegerField(choices=UserType.choices(), default=UserType.STANDARD)
    name = models.TextField()
    given_name = models.TextField()
    family_name = models.TextField()
    email = models.TextField()
    bookmarks = models.ManyToManyField(Paper, related_name='bookmarkers')

    def __str__(self):
        return self.name

    @property
    def all_types(self):
        return [key.name for key in UserType]

    @property
    def can_edit(self):
        return self.type == UserType.EDITOR or self.type == UserType.ADMIN

    @property
    def is_admin(self):
        return self.type == UserType.ADMIN

    @property
    def type_lower(self):
        return UserType(self.type).name.lower()

