#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copied from http://docs.peewee-orm.com/en/latest/peewee/quickstart.html


from datetime import date
from peewee import Model, SqliteDatabase
from peewee_extra_fields import *


db = SqliteDatabase('')


class Person(Model):  # All peewee_extra_fields.
    name = CharFieldCustom()
    birthday = PastDateField()
    cuit = ARCUITField()
    postal_code = ARPostalCodeField()
    country = CountryISOCodeField()
    currency = CurrencyISOCodeField()
    language = LanguageISOCodeField()
    ip = IPNetworkField()
    age = PositiveIntegerField()
    interests = CSVField()


if __name__ in "__main__":
    db.create_tables([Person], safe=True)

    zoe = Person(name="Zoe", birthday=date(1985, 1, 1), cuit="20-30900000-6",
                 postal_code="1010", country="ar", currency="usd",
                 language="en", ip="::1", age=30, interests="python,peewee")
    zoe.save()
    del zoe  # Bye Zoe.

    zoe = Person.get(Person.name == "Zoe")  # Zoe is back.
    print(f"""Name:  {zoe.name},        Python Type: {type(zoe.name)}.
          Birthday:  {zoe.birthday},    Python Type: {type(zoe.birthday)}.
          CUIT:      {zoe.cuit},        Python Type: {type(zoe.cuit)}.
          Postal:    {zoe.postal_code}, Python Type: {type(zoe.postal_code)}.
          IPv6:      {zoe.ip},          Python Type: {type(zoe.ip)}.
          Age:       {zoe.age},         Python Type: {type(zoe.age)}.
          interests: {zoe.interests},   Python Type: {type(zoe.interests)}.
          Country:   {zoe.country},     Python Type: {type(zoe.country)}.
          Currency:  {zoe.currency},    Python Type: {type(zoe.currency)}.
          Language:  {zoe.language},    Python Type: {type(zoe.language)}.""")
