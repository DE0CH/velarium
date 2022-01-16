from django.db import models
import re
from enum import IntEnum
# Create your models here.

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
    registered= models.BooleanField(default=False)
    name = models.TextField()
    given_name = models.TextField()
    family_name = models.TextField()
    email = models.TextField()

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

    @property
    def username(self):
        email_validation = re.compile('(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])')
        if not email_validation.match(self.email):
            raise ValueError("User email is not a valid email.")
        email_append = re.compile('@.+$')
        unclean = email_append.sub('', self.email)
        unix_unsafe = re.compile("[^-._a-zA-Z0-9]")
        clean= unix_unsafe.sub('', unclean)
        return clean
