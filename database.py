#!/usr/bin/env python3

from peewee import *

database = SqliteDatabase("db.sqlite3")


class User(Model):
    email = CharField(unique=True)

    class Meta:
        database = database


def create_tables():
    with database:
        database.create_tables([User])
