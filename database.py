#!/usr/bin/env python3

from peewee import *

database = SqliteDatabase("db.sqlite3", pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    email = CharField(unique=True)
    persistent = BooleanField()


class TrafficStatsBaseModel(BaseModel):
    user = ForeignKeyField(User, on_delete="CASCADE", null=False)
    date = DateTimeField(null=False)
    rx = IntegerField(null=False)
    tx = IntegerField(null=False)

    class Meta:
        indexes = (
            (("user", "date"), True),
        )


class Hour(TrafficStatsBaseModel):
    user = ForeignKeyField(User, backref="hours", on_delete="CASCADE", null=False)


class FiveMinute(TrafficStatsBaseModel):
    user = ForeignKeyField(User, backref="five_minutes", on_delete="CASCADE", null=False)


def create_tables():
    with database:
        database.create_tables([User, Hour, FiveMinute])
