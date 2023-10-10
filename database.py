#!/usr/bin/env python3

from peewee import *

database = SqliteDatabase("db.sqlite3")


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    email = CharField(unique=True)

    def remove(self):
        (TrafficStats
         .delete()
         .where(TrafficStats.user == self)
         .execute())
        self.delete_instance()


class TrafficStats(BaseModel):
    user = ForeignKeyField(User, backref="traffic_stats")
    value = IntegerField()
    direction = CharField()
    date = DateTimeField()


def create_tables():
    with database:
        database.create_tables([User, TrafficStats])
