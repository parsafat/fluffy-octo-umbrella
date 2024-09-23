#!/usr/bin/env python3

from peewee import *

database = SqliteDatabase("db.sqlite3", pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    email = CharField(unique=True)
    persistent = BooleanField()


class Hour(BaseModel):
    user = ForeignKeyField(User, backref="hours", on_delete="CASCADE")
    date = DateTimeField(null=False)
    rx = IntegerField(null=False)
    tx = IntegerField(null=False)

    class Meta:
        indexes = (
            (("user", "date"), True),
        )


def create_tables():
    with database:
        database.create_tables([User, Hour])
