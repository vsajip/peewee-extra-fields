#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Extra Fields for Peewee ORM. Old Peewee 2.x Legacy Fields live here.
Fields missing on Peewee >=3 but still relevant and useful."""


from peewee import BlobField

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    from bcrypt import hashpw, gensalt
except ImportError:
    hashpw = gensalt = PasswordField = PasswordHash = None


class PickledField(BlobField):
    def db_value(self, value):
        if value is not None:
            return pickle.dumps(value)

    def python_value(self, value):
        if value is not None:
            return pickle.loads(value)


if hashpw and gensalt:
    class PasswordHash(bytes):
        def check_password(self, password):
            password = password.encode('utf-8')
            return hashpw(password, self) == self

    class PasswordField(BlobField):
        def __init__(self, iterations=12, *args, **kwargs):
            if None in (hashpw, gensalt):
                raise ValueError(
                    f'{self.__class__.__name__} Module not found: BCrypt.')
            self.bcrypt_iterations = iterations
            self.raw_password = None
            super(PasswordField, self).__init__(*args, **kwargs)

        def db_value(self, value):
            """Convert the python value for storage in the database."""
            if isinstance(value, PasswordHash):
                return bytes(value)
            if isinstance(value, str):
                value = value.encode('utf-8')
            salt = gensalt(self.bcrypt_iterations)
            return value if value is None else hashpw(value, salt)

        def python_value(self, value):
            """Convert the database value to a pythonic value."""
            if isinstance(value, str):
                value = value.encode('utf-8')
            return PasswordHash(value)
