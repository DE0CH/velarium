from django.db import models
import uuid
from enum import IntEnum
# Create your models here.


class TagClass(models.Model):
    """
    A group of tags that have a title. For example, "Topic" is a tag class and under it there would be tags such as
    "Cognitive processes", "The individual and the group", "Cultural influences on behavior", etc.
    """
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
    png = models.FileField(max_length=262)  # 36 for UUID, 1 for '/' and 225 for filename length
    pdf = models.FileField(default='failed.pdf', max_length=262)
    link = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)

    def is_bookmarked(self, user):
        """
        Get if the paper is bookmarked by the user.
        :param user: The User object in question.
        :return: Whether the paper is bookmarked.
        """
        return self.bookmarkers.filter(pk=user.pk).exists()

    def __str__(self):
        return self.title

    @property
    def nested_tag_names(self):
        """
        Get a dictionary of the names of all the tag classes as the keys, and the list of the names of all the tags as
        the values.
        :return: The dictionary.
        """
        tag_classes = {}
        for tag in self.tags.all():
            if tag.tag_class.name not in tag_classes:
                tag_classes[tag.tag_class.name] = []
            tag_classes[tag.tag_class.name].append(tag.name)
        return tag_classes


class UserType(IntEnum):
    """
    A Enum that maps the user type to integer. The mapping should be consistent with the front end JS code.
    """
    STANDARD = 1
    EDITOR = 2
    ADMIN = 3

    @classmethod
    def choices(cls):
        """
        Get a list of two-element tuples of the enum names and values. Helpful for specifying the data type in the database.
        :return: A list of two-element tuples of the enum names and values.
        """
        return [(key.value, key.name) for key in cls]


class User(models.Model):
    """
    Represents a logged in user.
    """
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
        """
        :return: All the user types as a dictionary of their names.
        """
        return [key.name for key in UserType]

    @property
    def can_edit(self):
        """
        :return: If the user have editing rights.
        """
        return self.type == UserType.EDITOR or self.type == UserType.ADMIN

    @property
    def is_admin(self):
        """
        :return: If the user is an admin
        """
        return self.type == UserType.ADMIN

    @property
    def type_lower(self):
        """

        :return: The name of the user type in lowercase.
        """
        return UserType(self.type).name.lower()

