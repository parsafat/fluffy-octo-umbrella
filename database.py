#!/usr/bin/env python3

from peewee import *

database = SqliteDatabase("db.sqlite3")


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    email = CharField(unique=True)
    persistent = BooleanField()


def create_tables():
    with database:
        database.create_tables([User])
