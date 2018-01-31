# peewee-extra-fields

[Extra additional Fields](http://docs.peewee-orm.com/en/latest/peewee/models.html#creating-a-custom-field) for [Peewee ORM.](http://docs.peewee-orm.com) [![Build Status](https://travis-ci.org/juancarlospaco/peewee-extra-fields.svg?branch=master)](https://travis-ci.org/juancarlospaco/peewee-extra-fields)

ARCUITField, ARPostalCodeField, CSVField, CharFieldCustom, CountryISOCodeField, CurrencyISOCodeField, IANCodeField,
IBANISOCodeField, IPAddressField, IPNetworkField, LanguageISOCodeField, PastDateField, PastDateTimeField,
PositiveBigIntegerField, PositiveDecimalField, PositiveFloatField, PositiveIntegerField, PositiveSmallIntegerField, SWIFTISOCodeField,USSocialSecurityNumberField, USZipCodeField, and more. Autogeneration of HTML5 Widgets for Fields.

We want to be a hub for all custom Fields. If your created a Custom Peewee Field feel free to [Send Pull Requests!!!.](https://github.com/juancarlospaco/peewee-extra-fields/compare)
Open Repo access to anyone who want to contribute, just contact me.

![screenshot](https://source.unsplash.com/IClZBVw5W5A/800x400 "Illustrative Photo by https://unsplash.com/@toddquackenbush")

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg)](http://opensource.org/licenses/GPL-3.0)
[![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg)](http://opensource.org/licenses/LGPL-3.0)
[![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg)](http://python.org)


# Documentation

##### PositiveIntegerField, PositiveSmallIntegerField, PositiveBigIntegerField
<details>

`peewee_extra_fields.PositiveSmallIntegerField()`

`peewee_extra_fields.PositiveIntegerField()`

`peewee_extra_fields.PositiveBigIntegerField()`

**Description:** [`IntegerField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Positive** values (>= 0).

`PositiveSmallIntegerField` accepts positive integers from `0` to `32_767` according to [the Standard SQL Oficial Specs](https://www.postgresql.org/docs/current/static/datatype-numeric.html).

`PositiveIntegerField` accepts positive integers from `0` to `2_147_483_647` according to [the Standard SQL Oficial Specs](https://www.postgresql.org/docs/current/static/datatype-numeric.html).

`PositiveBigIntegerField` accepts positive integers from `0` to `9_223_372_036_854_775_807` according to [the Standard SQL Oficial Specs](https://www.postgresql.org/docs/current/static/datatype-numeric.html).

The smaller integer field type you can use, the faster performance, by definition.

**Arguments:** None (should take the same `*args` and `**kwargs` as `IntegerField`)

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `IntegerField`).

**Returns:** `int`.

**Base Class:** `IntegerField`, `SmallIntegerField`, `BigIntegerField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PositiveIntegerField  # its the same with PositiveSmallIntegerField and PositiveBigIntegerField
>>> PositiveIntegerField().db_value(1)
1
>>> PositiveIntegerField().db_value(0)
0
>>> PositiveIntegerField().db_value(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: PositiveIntegerField Value is not a Positive Integer (valid values must be Integers >=0): -1.

```
</details>


##### PositiveFloatField
<details>

`peewee_extra_fields.PositiveFloatField(round_by: int=None)`

**Description:** [`FloatField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Positive** values (>= 0).
Optionally it can round Floats using Pythons `round()` with `round_by` integer argument.

`PositiveFloatField` from `0` to `6` decimal digits precision according to [the Standard SQL Oficial Specs](https://www.postgresql.org/docs/current/static/datatype-numeric.html).

**Arguments:**
- `round()` round `float` using Pythons `round()`, optional, defaults to `None`, integer type, positive value.

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `FloatField`).

**Returns:** `float`.

**Base Class:** `FloatField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PositiveFloatField
>>> PositiveFloatField().db_value(1.0)
1.0
>>> PositiveFloatField().db_value(0.0)
0.0
>>> PositiveFloatField().db_value(-1.0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: PositiveFloatField Value is not a Positive Float (valid values must be Floats >=0): -1.0.

>>> PositiveFloatField(round_by=2).db_value(1.123456789)
1.12
>>> PositiveFloatField(round_by=4).db_value(1.123456789)
1.1235
>>> PositiveFloatField(round_by=-2).db_value(1.123456789)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: PositiveFloatField 'round_by' argument is not a Non-Zero Positive Integer number (valid values must be Integers > 0): -2.

```
</details>


##### PositiveDecimalField
<details>

`peewee_extra_fields.PositiveDecimalField(round_by: int=None)`

**Description:** [`DecimalField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Positive** values (>= 0).

`PositiveDecimalField` from `0` to `131_072` decimal digits precision before the decimal point and from `0` to `16_383` decimal digits precision after the decimal point according to [the Standard SQL Oficial Specs](https://www.postgresql.org/docs/current/static/datatype-numeric.html).

up to 131072 digits before the decimal point; up to 16383 digits after the decimal point
**Arguments:**
- `round()` round `decimal.Decimal` using Pythons `Decimal().quantize().normalize()`, optional, defaults to `None`, integer type, positive value.

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `DecimalField`).

**Returns:** `decimal.Decimal`.

**Base Class:** `DecimalField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PositiveDecimalField
>>> from decimal import Decimal
>>> PositiveDecimalField().db_value(Decimal("1.0"))
Decimal('1.0')
>>> PositiveDecimalField().db_value(Decimal("0.0"))
Decimal('0.0')
>>> PositiveDecimalField().db_value(Decimal("-1.0"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: PositiveDecimalField Value is not a Positive Decimal (valid values must be Decimals >=0): -1.0.

>>> PositiveDecimalField(round_by=2).db_value(Decimal("1.123456789"))
Decimal('1.12')
>>> PositiveDecimalField(round_by=4).db_value(Decimal("1.123456789"))
Decimal('1.1235')
>>> PositiveDecimalField(round_by=-2).db_value(Decimal("1.123456789"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: PositiveDecimalField 'round_by' argument is not a Non-Zero Positive Integer numbers (valid values must be Integers > 0): -2.

```
</details>


##### IPAddressField
<details>

`peewee_extra_fields.IPAddressField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **IP Addresses** values (IPv4 & IPv6).

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `IPv4Address` or `IPv6Address`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import IPAddressField
>>> IPAddressField().db_value("127.0.0.1")
'127.0.0.1'
>>> IPAddressField().db_value("::1")
'::1'
>>> IPAddressField().db_value("10.0.0.1")
'10.0.0.1'
>>> IPAddressField().db_value("10.0.256")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IPAddressField Value string is not a Valid IP v4 or v6 Address (valid values must be a valid <class 'ipaddress.IPv4Address'>): 10.0.256 --> '10.0.256' does not appear to be an IPv4 or IPv6 address.

>>> IPAddressField().db_value("a.b.c")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IPAddressField Value string is not a Valid IP v4 or v6 Address (valid values must be a valid <class 'ipaddress.IPv4Address'>): a.b.c --> 'a.b.c' does not appear to be an IPv4 or IPv6 address.

>>> IPAddressField().python_value("::1")
IPv6Address('::1')
>>> IPAddressField().python_value("172.16.0.1")
IPv4Address('172.16.0.1')
```
</details>


##### IPNetworkField
<details>

`peewee_extra_fields.IPNetworkField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **IP Networks** values (IPv4 & IPv6).

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `IPv4Network` or `IPv6Network`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import IPNetworkField
>>> IPNetworkField().db_value("10.0.0.0")
'10.0.0.0'
>>> IPNetworkField().db_value("10.0.0.0/23")
'10.0.0.0/23'
>>> IPNetworkField().db_value("256.0.0.0/23")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IPNetworkField Value string is not a Valid IP v4 or v6 Network (valid values must be a valid <class 'ipaddress.IPv4Network'>): 256.0.0.0/23 --> '256.0.0.0/23' does not appear to be an IPv4 or IPv6 network.

>>> IPNetworkField().python_value("10.0.0.0/23")
IPv4Network('10.0.0.0/23')
```
</details>


##### PastDateField
<details>

`peewee_extra_fields.PastDateField()`

**Description:** [`DateField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts dates **Not on the Future** values.
Past is Ok, Present is Ok, Future is Not Ok.
Most of times you need Dates on the Past, eg. your Birthday cant be in the Future.

This Field has an additional helper method for lazy devs:
`peewee_extra_fields.PastDateField().get_html_widget(clas: tuple=None, ids: str=None, required: bool=False)`
that will build and return a string with 1 HTML5 widget element fit for purpose for the possible values of the Field,
No CSS, No JS, Nothing Embed, just plain clear text HTML,
you can set the DOM Classes with `class` argument of `tuple` type, you can set the DOM ID with `ids` argument of `str` type,
you can set the DOM "required" with `required` argument of `bool` type, return type is always `str`,
it just returns an string does not affect the internals of the Field.

**Arguments:** None (should take the same `*args` and `**kwargs` as `IntegerField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `IntegerField`).

**Returns:** `date`.

**Base Class:** `DateField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PastDateField
>>> from datetime import date
>>> PastDateField().db_value(date(year=2010, month=1, day=1))
datetime.date(2010, 1, 1)
>>> PastDateField().db_value(date(year=2017, month=1, day=1))
datetime.date(2017, 1, 1)
>>> PastDateField().db_value(date(year=2020, month=1, day=1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: PastDateField Dates Value is not in the Past (valid values must be in the Past): 2020-01-01.

>>> print(PastDateField().get_html_widget())
<input type="date" name="date"  max="2017-12-14">

```
</details>


##### PastDateTimeField
<details>

`peewee_extra_fields.PastDateTimeField()`

**Description:** [`DateTimeField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts dates **Not on the Future** values.
Past is Ok, Present is Ok, Future is Not Ok.
Most of times you need DateTimes on the Past, eg. your Birthday cant be in the Future.

This Field has an additional helper method for lazy devs:
`peewee_extra_fields.PastDateTimeField().get_html_widget(clas: tuple=None, ids: str=None, required: bool=False)`
that will build and return a string with 1 HTML5 widget element fit for purpose for the possible values of the Field,
No CSS, No JS, Nothing Embed, just plain clear text HTML,
you can set the DOM Classes with `class` argument of `tuple` type, you can set the DOM ID with `ids` argument of `str` type,
you can set the DOM "required" with `required` argument of `bool` type, return type is always `str`,
it just returns an string does not affect the internals of the Field.

**Arguments:** None (should take the same `*args` and `**kwargs` as `DateTimeField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `DateTimeField`).

**Returns:** `datetime`.

**Base Class:** `DateTimeField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PastDateTimeField
>>> from datetime import datetime
>>> PastDateTimeField().db_value(datetime(year=2010, month=1, day=1))
datetime.datetime(2010, 1, 1, 0, 0)
>>> PastDateTimeField().db_value(datetime(year=2017, month=1, day=1))
datetime.datetime(2017, 1, 1, 0, 0)
>>> PastDateTimeField().db_value(datetime(year=2020, month=1, day=1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: PastDateTimeField Dates & Times Value is not in the Past (valid values must be in the Past): 2020-01-01 00:00:00.

>>> print(PastDateTimeField().get_html_widget())
<input type="datetime-local" name="datetime" max="2017-12-14T04:40">

```
</details>



##### LanguageISOCodeField
<details>

`peewee_extra_fields.LanguageISOCodeField()`

**Description:** [`FixedCharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Language ISO Code** values (ISO-639_1).
Uses hardcoded `max_length = 2`.

This Field has an additional helper method for lazy devs:
`peewee_extra_fields.LanguageISOCodeField().get_html_widget(clas: tuple=None, ids: str=None, required: bool=False)`
that will build and return a string with 1 HTML5 widget element fit for purpose for the possible values of the Field,
No CSS, No JS, Nothing Embed, just plain clear text HTML,
you can set the DOM Classes with `class` argument of `tuple` type, you can set the DOM ID with `ids` argument of `str` type,
you can set the DOM "required" with `required` argument of `bool` type, return type is always `str`,
it just returns an string does not affect the internals of the Field.

**Arguments:** None (should take the same `*args` and `**kwargs` as `FixedCharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `FixedCharField`).

**Returns:** `collections.namedtuple`.

**Base Class:** `FixedCharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import LanguageISOCodeField
>>> LanguageISOCodeField().db_value("en")
'en'
>>> LanguageISOCodeField().db_value("es")
'es'
>>> LanguageISOCodeField().python_value("es")
LanguageISO639(code='es', name='Spanish')
>>> LanguageISOCodeField().python_value("en")
LanguageISO639(code='en', name='English')
>>> LanguageISOCodeField().db_value("not valid")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: LanguageISOCodeField Value is 9 Characters long instead of 2 Characters long (valid values must be ISO-639_1 Language Codes): not valid.

>>> LanguageISOCodeField().db_value("xx")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: LanguageISOCodeField Value is not an ISO-639_1 Standard Language Code of 2 Characters long (valid values must be ISO-639_1 Language Codes): xx.

>>> print(LanguageISOCodeField().get_html_widget())
<select name="language" >
    <option selected disabled value=""></option>
    <option value="aa">(AA) Afar (afaraf)</option>
    <option value="af">(AF) Afrikaans (afrikaans)</option>
    <option value="ak">(AK) Akan (akan)</option>
#    . . . All the other ISO-639 Languages here on several HTML option elements autogenerated for you . . .  
    <option value="xh">(XH) Xhosa (isixhosa)</option>
    <option value="zu">(ZU) Zulu (isizulu)</option>
</select>

```
</details>


##### CountryISOCodeField
<details>

`peewee_extra_fields.CountryISOCodeField()`

**Description:** [`SmallIntegerField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass only accepts **Country ISO Code** string values.

It converts the 2-Characters Country ISO Code to integer Country ISO Code,
saves to Database the SmallInt, when reading from Database, reverts back,
small integer Country ISO Code to 2-Characters string Country ISO Code.

Returns 1 namedtuple with iso3166_a3, iso3166_numeric, capital, continent,
currency_code, currency_name, geoname_id, is_developed, is_independent,
languages, name, name_human, phone_code, timezones and tld.

This always stores only small positive Integer numbers of 3 digits max,
that maps 1-to-1 to 2-Characters string Country Codes, according to ISO.

Small integer is always faster than varchar or text in every aspect.

This Field has an additional helper method for lazy devs:
`peewee_extra_fields.CountryISOCodeField().get_html_widget(clas: tuple=None, ids: str=None, required: bool=False)`
that will build and return a string with 1 HTML5 widget element fit for purpose for the possible values of the Field,
No CSS, No JS, Nothing Embed, just plain clear text HTML,
you can set the DOM Classes with `class` argument of `tuple` type, you can set the DOM ID with `ids` argument of `str` type,
you can set the DOM "required" with `required` argument of `bool` type, return type is always `str`,
it just returns an string does not affect the internals of the Field.

**Arguments:** None (should take the same `*args` and `**kwargs` as `SmallIntegerField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `SmallIntegerField`).

**Returns:** `collections.namedtuple`.

**Base Class:** `SmallIntegerField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import CountryISOCodeField
>>> CountryISOCodeField().db_value("ar")
32
>>> CountryISOCodeField().python_value(32)
CountryISO3166(iso3166_a3='ARG', iso3166_numeric=32, capital='Buenos Aires', continent='Americas', currency_code='ARS', currency_name='Argentine Peso', geoname_id=3865483, is_developed=False, is_independent=True, languages=['es-AR', 'en', 'it', 'de', 'fr', 'gn'], name='Argentina', name_human='The Argentine Republic', phone_code='54', timezones=['america/argentina/buenos_aires', 'america/argentina/cordoba', 'america/argentina/jujuy', 'america/argentina/tucuman', 'america/argentina/catamarca', 'america/argentina/la_rioja', 'america/argentina/san_juan', 'america/argentina/mendoza', 'america/argentina/rio_gallegos', 'america/argentina/ushuaia'], tld='.ar')
>>> CountryISOCodeField().db_value("xx")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: CountryISOCodeField Value is not an ISO-3166 Standard Country Code of 2 Characters long (valid values must be ISO-3166 Country Codes): xx.

>>> print(CountryISOCodeField().get_html_widget())
<select name="country" >
    <option selected disabled value=""></option>
    <option value="ad" data-iso3166numeric="20"  data-iso3166a3="and">(AD) Andorra</option>
    <option value="ae" data-iso3166numeric="784" data-iso3166a3="are">(AE) United Arab Emirates</option>
    <option value="af" data-iso3166numeric="4"   data-iso3166a3="afg">(AF) Afghanistan</option>
#    . . . All the other ISO-3166 Countries here on several HTML option elements autogenerated for you . . .
    <option value="za" data-iso3166numeric="710" data-iso3166a3="zaf">(ZA) South Africa</option>
    <option value="zm" data-iso3166numeric="894" data-iso3166a3="zmb">(ZM) Zambia</option>
    <option value="zw" data-iso3166numeric="716" data-iso3166a3="zwe">(ZW) Zimbabwe</option>
</select>

```
</details>


##### CurrencyISOCodeField
<details>

`peewee_extra_fields.CurrencyISOCodeField()`

**Description:** [`SmallIntegerField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass only accepts **Currency ISO Code** values.

It converts 3-Characters Currency ISO Code to integer Currency ISO Code,
saves to Database the SmallInt, when reading from Database, reverts back,
small integer Currency ISO Code to 3-Characters string Currency ISO Code.

Returns 1 namedtuple with code, name, iso4217_numeric.

This always stores only small positive Integer numbers of 3 digits max,
that maps 1-to-1 to 3-Characters string Currency Codes, according to ISO.

Small integer is always faster than varchar or text in every aspect.

This Field has an additional helper method for lazy devs:
`peewee_extra_fields.CurrencyISOCodeField().get_html_widget(clas: tuple=None, ids: str=None, required: bool=False)`
that will build and return a string with 1 HTML5 widget element fit for purpose for the possible values of the Field,
No CSS, No JS, Nothing Embed, just plain clear text HTML,
you can set the DOM Classes with `class` argument of `tuple` type, you can set the DOM ID with `ids` argument of `str` type,
you can set the DOM "required" with `required` argument of `bool` type, return type is always `str`,
it just returns an string does not affect the internals of the Field.

**Arguments:** None (should take the same `*args` and `**kwargs` as `SmallIntegerField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `SmallIntegerField`).

**Returns:** `collections.namedtuple`.

**Base Class:** `SmallIntegerField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import CurrencyISOCodeField
>>> CurrencyISOCodeField().db_value("usd")
840
>>> CurrencyISOCodeField().python_value(840)
CurrencyISO4217(code='usd', name='United States Dollar', iso4217_numeric=840)
>>> CurrencyISOCodeField().db_value("not valid")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: CurrencyISOCodeField Value is 9 Characters long instead of 3 Characters long (valid values must be ISO-4217 Currency Codes): not valid.

>>> CurrencyISOCodeField().db_value("lol")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: CurrencyISOCodeField Value is not an ISO-4217 Standard Currency Code of 3 Characters long (valid values must be ISO-4217 Currency Codes): lol.

>>> print(CurrencyISOCodeField().get_html_widget())
<select name="currency" >
    <option selected disabled value=""></option>
    <option value="aed" data-iso4217numeric="784">(AED) United Arab Emirates Dirham</option>
    <option value="afn" data-iso4217numeric="971">(AFN) Afghan Afghani</option>
    <option value="all" data-iso4217numeric="8"  >(ALL) Albanian Lek</option>
#    . . . All the other ISO-4217 Currencies here on several HTML option elements autogenerated for you . . .
    <option value="zar" data-iso4217numeric="710">(ZAR) South African Rand</option>
    <option value="zmw" data-iso4217numeric="967">(ZMW) Zambian Kwacha</option>
    <option value="zwl" data-iso4217numeric="932">(ZWL) Zimbabwean Dollar</option>
</select>

```
</details>


##### SWIFTISOCodeField
<details>

`peewee_extra_fields.SWIFTISOCodeField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **SWIFT-Codes ISO-9362** values (SWIFT Business Identifier Code BIC ISO-9362:2014, AKA SWIFT).

Has a hardcoded `max_length = 11` according to ISO-9362 Standard.

`country_code` must be a valid ISO-3166 country code according to ISO-9362 Standard.

`branch_code` can be a `str` or `None` according to ISO-9362 Standard.

This code is also known as: SWIFT-BIC, BIC code, SWIFT ID, SWIFT code or ISO-9362.

Returns a `collections.namedtuple` with `bank_code`, `country_code`, `location_code`, `branch_code`, `swift`.

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`)

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `collections.namedtuple`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import SWIFTISOCodeField  
>>> SWIFTISOCodeField().python_value("DEUTDEFF")
SWIFTCodeISO9362(bank_code='DEUT', country_code='DE', location_code='FF', branch_code=None, swift='DEUTDEFF')

>>> SWIFTISOCodeField().python_value("NEDSZAJJ")
SWIFTCodeISO9362(bank_code='NEDS', country_code='ZA', location_code='JJ', branch_code=None, swift='NEDSZAJJ')

>>> SWIFTISOCodeField().python_value("DABADKKK")
SWIFTCodeISO9362(bank_code='DABA', country_code='DK', location_code='KK', branch_code=None, swift='DABADKKK')

>>> SWIFTISOCodeField().python_value("UNCRITMM")
SWIFTCodeISO9362(bank_code='UNCR', country_code='IT', location_code='MM', branch_code=None, swift='UNCRITMM')

>>> SWIFTISOCodeField().db_value("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: SWIFTISOCodeField Value string is not a Valid SWIFT-Code ISO-9362:2014 (valid values must not be an Empty String): "".

>>> SWIFTISOCodeField().db_value("None")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: SWIFTISOCodeField Value string is not a Valid SWIFT-Code ISO-9362:2014 (valid values must be a valid SWIFT-Code of 8 or 11 characters long): NONE.

```
</details>


##### IBANISOCodeField
<details>

`peewee_extra_fields.IBANISOCodeField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **IBAN-Codes ISO 13616:2007** values (International Bank Account Number (IBAN).

Has a hardcoded `max_length = 34` according to ISO-13616 Standard.

`country_code` must be a valid ISO-3166 country code according to ISO-13616 Standard.

Returns a `collections.namedtuple` with `country_code`, `checksum`, `bban`, `iban_pretty`, `iban`.

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`)

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `collections.namedtuple`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import IBANISOCodeField  
>>> IBANISOCodeField().db_value("DE44 5001 0517 5407 3249 31")
'DE44500105175407324931'

>>> IBANISOCodeField().python_value("DE44 5001 0517 5407 3249 31")
SWIFTCodeISO9362(country_code='DE', check_code='44', bban='500105175407324931', iban_pretty='DE44 5001 0517 5407 3249 31', iban='DE44500105175407324931')

>>> IBANISOCodeField().python_value("GB29 NWBK 6016 1331 9268 19")
SWIFTCodeISO9362(country_code='GB', check_code='29', bban='NWBK60161331926819', iban_pretty='GB29 NWBK 6016 1331 9268 19', iban='GB29NWBK60161331926819')

>>> IBANISOCodeField().python_value("SA03 8000 0000 6080 1016 7519")
SWIFTCodeISO9362(country_code='SA', check_code='03', bban='80000000608010167519', iban_pretty='SA03 8000 0000 6080 1016 7519', iban='SA0380000000608010167519')

>>> IBANISOCodeField().python_value("CH93 0076 2011 6238 5295 7")
SWIFTCodeISO9362(country_code='CH', check_code='93', bban='00762011623852957', iban_pretty='CH93 0076 2011 6238 5295 7', iban='CH9300762011623852957')
>>> IBANISOCodeField().python_value("GB82 WEST 1234 5698 7654 32")
SWIFTCodeISO9362(country_code='GB', check_code='82', bban='WEST12345698765432', iban_pretty='GB82 WEST 1234 5698 7654 32', iban='GB82WEST12345698765432')

>>> IBANISOCodeField().db_value("DEzz 5001 0517 5407 3249 31")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IBANISOCodeField Value string is not a Valid IBAN-Code ISO-13616:2007 (valid values must be a valid IBAN-Code, must contain a Valid IBAN CheckSum Digit): DEZZ500105175407324931 -> zz.

>>> IBANISOCodeField().db_value("DE00 5001 0517 5407 3249 31")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IBANISOCodeField Value string is not a Valid IBAN-Code ISO-13616:2007 (valid values must have a valid IBAN CheckSum digits): DE00500105175407324931 -> 00.

>>> IBANISOCodeField().db_value("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IBANISOCodeField Value string is not a Valid IBAN-Code ISO-13616:2007 (valid values must not be an Empty String): "".

>>> IBANISOCodeField().db_value("DE00 5001 0517 5407 3249 3100 0000 0000 0000")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IBANISOCodeField Value string is not a Valid IBAN-Code ISO-13616:2007 (valid values must be a valid IBAN-Code ISO-13616 of 34 characters max): DE0050010517540732493100000000000000.

```
</details>


##### IANCodeField
<details>

`peewee_extra_fields.IANCodeField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **IAN Codes** values, International Article Number (AKA European Article Number or EAN or IAN).

Has a hardcoded `max_length = 13` according to Wikipedia.

Notice this is not an ISO Standard, if you work with this codes, any improvement is welcome.

CheckSum for 8 to 13 IAN-Codes only.

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`)

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `str`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import IANCodeField  
>>> IANCodeField().db_value("5901234123457")
'5901234123457'

>>> IANCodeField().db_value("4012345123456")
'4012345123456'

>>> IANCodeField().db_value("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IANCodeField Value string is not a Valid International Article Number (IAN) (valid values must not be an Empty String): "".

>>> IANCodeField().db_value("1234567896765756756")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IANCodeField Value string is not a Valid International Article Number (IAN) (valid values must be a valid IAN of 13 characters max): 1234567896765756756.

>>> IANCodeField().db_value("1234567890")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: IANCodeField Value string is not a Valid International Article Number IAN 8~13 Characters (valid values must have a valid IAN CheckSum int): 1234567890.

```
</details>


##### ColorHexadecimalField
<details>

`peewee_extra_fields.ColorHexadecimalField()`

**Description:** [`FixedCharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Colors on Hexadecimal** values (4 & 7 chars format).
Format is 3 or 6 Hexadecimal characters, eg `"#00ff00"`, `"#be0"`, etc.
Values must start with a `"#"`.
Values must be 4 or 7 characters long.
Has a hardcoded `max_length = 7`.

**Arguments:** None (should take the same `*args` and `**kwargs` as `FixedCharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `FixedCharField`).

**Returns:** `collections.namedtuple`.

**Base Class:** `FixedCharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import ColorHexadecimalField
>>> ColorHexadecimalField().db_value("#f0f0f0")
'#f0f0f0'

>>> ColorHexadecimalField().db_value("#be0")
'#bbee00'

>>> ColorHexadecimalField().db_value("#fe0")
'#ffee00'

>>> ColorHexadecimalField().db_value("#bebebe")
'#bebebe'

>>> ColorHexadecimalField().python_value("#f0f0f0")
Color(hex='#f0f0f0', rgb=RGB(red=240, green=240, blue=240), hls=HLS(h=0.0, l=240.0, s=0.0), hsv=HSV(h=0.0, s=0.0, v=240), yiq=YIQ(y=240.0, i=0.0, q=0.0), css='rgb(240,240,240)', css_prcnt='rgb(94%,94%,94%)')

>>> ColorHexadecimalField().python_value("#ffee00")
Color(hex='#ffee00', rgb=RGB(red=255, green=238, blue=0), hls=HLS(h=0.16, l=127.5, s=-1.01), hsv=HSV(h=0.16, s=1.0, v=255), yiq=YIQ(y=216.92, i=86.75, q=-70.66), css='rgb(255,238,0)', css_prcnt='rgb(100%,93%,0%)')

>>> ColorHexadecimalField().python_value("#ffee00").hex
'#ffee00'

>>> ColorHexadecimalField().python_value("#bebebe")
Color(hex='#bebebe', rgb=RGB(red=190, green=190, blue=190), hls=HLS(h=0.0, l=190.0, s=0.0), hsv=HSV(h=0.0, s=0.0, v=190), yiq=YIQ(y=190.0, i=0.0, q=0.0), css='rgb(190,190,190)', css_prcnt='rgb(74%,74%,74%)')

>>> ColorHexadecimalField().db_value("#bebehh")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: ColorHexadecimalField Value is not an Hexadecimal (values must be Hexadecimals): #bebehh invalid literal for int() with base 16: 'bebehh'

>>> ColorHexadecimalField().db_value("#bebe")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: ColorHexadecimalField Value is 5 Characters long instead of 7 or 4 Characters long (valid values must be exactly 7 or 4 characters): #bebe.

>>> ColorHexadecimalField().db_value("#bebebe0")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: ColorHexadecimalField Value is 8 Characters long instead of 7 or 4 Characters long (valid values must be exactly 7 or 4 characters): #bebebe0.

>>> ColorHexadecimalField().db_value("bebebeb")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: ColorHexadecimalField Value is not a valid RGB Hexadecimal Color value of 7 characters long (valid values must start with '#'): bebebeb.

```
</details>


##### SemVerField
<details>

`peewee_extra_fields.SemVerField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Semantic Versions** values (from 5 to 255 chars format).
Format standard spec is from [https://semver.org](https://semver.org).
Has a hardcoded `max_length = 255` as recommended on semver.org.

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `str`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import SemVerField
>>> SemVerField().db_value("1.0.0")
'1.0.0'

>>> SemVerField().db_value("0.0.1")
'0.0.1'

>>> SemVerField().db_value("v1.0.0")
'v1.0.0'

>>> SemVerField().db_value("1.2.3-alpha.10.beta.0+build.unicorn.rainbow")
'1.2.3-alpha.10.beta.0+build.unicorn.rainbow'

>>> SemVerField().db_value("0.0.0-foo")
'0.0.0-foo'

>>> SemVerField().db_value("2.7.2-foo+bar")
'2.7.2-foo+bar'

>>> SemVerField().db_value("1.2.3-alpha.10.beta.0")
'1.2.3-alpha.10.beta.0'

>>> SemVerField().db_value("99.0.0")
'99.0.0'

>>> SemVerField().db_value("2.7.2+asdf")
'2.7.2+asdf'

>>> SemVerField().db_value("1.2.3-a.b.c.10.d.5")
'1.2.3-a.b.c.10.d.5'

>>> SemVerField().db_value("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: SemVerField Value is not a valid Semantic Version string, from 5 to 255 characters long(valid values must match a Regex "\bv?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[\da-z-]+(?:\.[\da-z-]+)*)?(?:\+[\da-z-]+(?:\.[\da-z-]+)*)?\b"): .

>>> SemVerField().db_value("0a")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: SemVerField Value is not a valid Semantic Version string, from 5 to 255 characters long (valid values must match a Regex "\bv?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[\da-z-]+(?:\.[\da-z-]+)*)?(?:\+[\da-z-]+(?:\.[\da-z-]+)*)?\b"): 0a.

>>> SemVerField().db_value("cat")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: SemVerField Value is not a valid Semantic Version string, from 5 to 255 characters long (valid values must match a Regex "\bv?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[\da-z-]+(?:\.[\da-z-]+)*)?(?:\+[\da-z-]+(?:\.[\da-z-]+)*)?\b"): cat.

```
</details>


##### ARPostalCodeField
<details>

`peewee_extra_fields.ARPostalCodeField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Argentine Postal Codes** (old & new).

This Field has an additional helper method for lazy devs:
`peewee_extra_fields.ARPostalCodeField().get_html_widget(clas: tuple=None, ids: str=None, required: bool=False)`
that will build and return a string with 1 HTML5 widget element fit for purpose for the possible values of the Field,
No CSS, No JS, Nothing Embed, just plain clear text HTML,
you can set the DOM Classes with `class` argument of `tuple` type, you can set the DOM ID with `ids` argument of `str` type,
you can set the DOM "required" with `required` argument of `bool` type, return type is always `str`,
it just returns an string does not affect the internals of the Field.

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `str`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import ARPostalCodeField
>>> ARPostalCodeField().db_value("2804")
'2804'
>>> ARPostalCodeField().db_value("666")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: ARPostalCodeField Value is not a valid Argentine Postal Code (old & new) string of 4 to 8 characters long: 666.

>>> print(ARPostalCodeField().get_html_widget())
<input type="text" name="postal-code"  placeholder="Codigo Postal Argentino" minlength="4" maxlength="8" size="8">

```
</details>


##### ARCUITField
<details>

`peewee_extra_fields.ARCUITField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Argentine CUIT**, also it can extract DNI from CUIT.

This Field has an additional helper method for lazy devs:
`peewee_extra_fields.ARCUITField().get_html_widget(clas: tuple=None, ids: str=None, required: bool=False)`
that will build and return a string with 1 HTML5 widget element fit for purpose for the possible values of the Field,
No CSS, No JS, Nothing Embed, just plain clear text HTML,
you can set the DOM Classes with `class` argument of `tuple` type, you can set the DOM ID with `ids` argument of `str` type,
you can set the DOM "required" with `required` argument of `bool` type, return type is always `str`,
it just returns an string does not affect the internals of the Field.

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `str`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import ARCUITField
>>> ARCUITField().db_value("20-30999666-6")
'20309996666'
>>> ARCUITField().db_value("20309996666")
'20309996666'
>>> ARCUITField().cuit2dni("20-30999666-6")
30999666
>>> ARCUITField().db_value("20-30999-6")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: ARCUITField Value is not a valid Argentine CUIT Code string of 11 to 13 characters long: 20-30999-6.

>>> print(ARCUITField().get_html_widget())
<input type="text" name="cuit" placeholder="CUIT Argentino" minlength="10" maxlength="13" size="13">

```
</details>


##### USZipCodeField
<details>

`peewee_extra_fields.USZipCodeField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **US ZIP Codes** (XXXXX or XXXXX-XXXX).

**Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `str`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import USZipCodeField
>>> USZipCodeField().db_value("20521-9000")
'20521-9000'

>>> USZipCodeField().db_value("99750-0077")
'99750-0077'

>>> USZipCodeField().db_value("12201-7050")
'12201-7050'

>>> USZipCodeField().db_value("")
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>

ValueError: USZipCodeField Value is not a valid USA ZIP Codes (XXXXX or XXXXX-XXXX) string from 5 to 10 characters long (valid values must match a Regex "^\d{5}(?:-\d{4})?$"): "".

>>> USZipCodeField().db_value("1")
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>

ValueError: USZipCodeField Value is not a valid USA ZIP Codes (XXXXX or XXXXX-XXXX) string from 5 to 10 characters long (valid values must match a Regex "^\d{5}(?:-\d{4})?$"): 1.

>>> USZipCodeField().db_value("20521-90000")
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>

ValueError: USZipCodeField Value is not a valid USA ZIP Codes (XXXXX or XXXXX-XXXX) string from 5 to 10 characters long (valid values must match a Regex "^\d{5}(?:-\d{4})?$"): 20521-90000.

```
</details>


##### USSocialSecurityNumberField
<details>

`peewee_extra_fields.USSocialSecurityNumberField()`

**Description:** [`FixedCharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **U.S.A. Social Security Numbers** (XXX-XX-XXXX format).
Has a hardcoded `max_length = 11`.
Returns a `namedtuple` with `ssn`, `area`, `group`, `serial`.

Checks that values conforms to the `XXX-XX-XXXX` format.

Area, Group, Serial must not be all Zeroes.

Group must not be `"666"`.

Must not be in the "promotional block" `987-65-4320` ~ `987-65-4329`.

**Arguments:** None (should take the same `*args` and `**kwargs` as `FixedCharField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `FixedCharField`).

**Returns:** `collections.namedtuple`.

**Base Class:** `FixedCharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import USSocialSecurityNumberField
>>> USSocialSecurityNumberField().db_value("205-21-9000")
'205-21-9000'

>>> USSocialSecurityNumberField().python_value("205-21-9000")
USSocialSecurityNumber(ssn='205-21-9000', area=205, group=21, serial=9000)

>>> USSocialSecurityNumberField().db_value("205-21-90")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: USSocialSecurityNumberField Value is not a valid U.S.A. Social Security Number string (XXX-XX-XXXX format) (valid Social Security Number values be a must match a Regex '^(?P<area>\\d{3})[-\\ ]?(?P<group>\\d{2})[-\\ ]?(?P<sri>\\d{4})$'): 205-21-90 -> None.

In [7]: USSocialSecurityNumberField().db_value("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: USSocialSecurityNumberField Value is not a valid U.S.A. Social Security Number string (XXX-XX-XXXX format) (valid Social Security Number values be a must match a Regex '^(?P<area>\\d{3})[-\\ ]?(?P<group>\\d{2})[-\\ ]?(?P<sri>\\d{4})$'):  -> None.

In [8]: USSocialSecurityNumberField().db_value("1")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: USSocialSecurityNumberField Value is not a valid U.S.A. Social Security Number string (XXX-XX-XXXX format) (valid Social Security Number values be a must match a Regex '^(?P<area>\\d{3})[-\\ ]?(?P<group>\\d{2})[-\\ ]?(?P<sri>\\d{4})$'): 1 -> None.

```
</details>


##### PickledField
<details>

`peewee_extra_fields.PickledField()`

**Description:** Peewee [PickledField](http://docs.peewee-orm.com/en/2.7.0/search.html?q=PickledField) backported from 2.x Versions (literal copy & paste) to work with Peewee 3 and Python 3.
Stores arbitrary python objects, stores values in a pickled `BlobField`.
Internally uses `pickle.loads()` and `pickle.dumps()`.

[`PickledField` is explicitly no longer supported and deprecated by Peewee.](https://github.com/coleifer/peewee/issues/1444#issue-292958082)

This field has been clean out of Legacy Python2 compatibility code that it originally used to have.

**Arguments:** None (should take the same `*args` and `**kwargs` as `BlobField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `BlobField`).

**Returns:** Arbitrary Python objects.

**Base Class:** `BlobField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PickledField
>>> PickledField().db_value("a")
b'\x80\x03X\x01\x00\x00\x00aq\x00.'

>>> PickledField().python_value(b'\x80\x03X\x01\x00\x00\x00aq\x00.')
"a"

```

</details>


##### PasswordField
<details>

`peewee_extra_fields.PasswordField()`

**Description:** Peewee [PasswordField](http://docs.peewee-orm.com/en/2.7.0/peewee/playhouse.html?highlight=PasswordField#PasswordField) backported from 2.x Versions (literal copy & paste) to work with Peewee 3 and Python 3.
`PasswordField` stores a password hash and lets you verify it.
The password is hashed when it is saved to the database and
after reading it from the database you can call:
`check_password(password)` to return a `bool`.

This field requires `bcrypt`, which can be installed by running `pip install bcrypt`.
`peewee_extra_fields` still works Ok without `bcrypt`.

[`PasswordField` is explicitly no longer supported and deprecated by Peewee.](https://github.com/coleifer/peewee/issues/1444#issue-292958082)

This field has been clean out of Legacy Python2 compatibility code that it originally used to have.

This field is to support code already using Peewee 2.x `PasswordField`,
if you are implementing from zero, check `SimplePasswordField` that uses new Python `secrets` from standard lib.

**Arguments:** None (should take the same `*args` and `**kwargs` as `BlobField`).

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `BlobField`).

**Returns:** `bytes`.

**Base Class:** `BlobField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PasswordField
>>> PasswordField().db_value("a")
b'$2b$12$9CMSMQYPkZ5RsWWrZccw7eqGrCQF679BhDA4dz6rG/e70FbQmeG.6'

```

</details>


##### SimplePasswordField
<details>

`peewee_extra_fields.SimplePasswordField()`

**Description:** Peewee [PasswordField](http://docs.peewee-orm.com/en/2.7.0/peewee/playhouse.html?highlight=PasswordField#PasswordField) re-implemented and simplified from 2.x Versions to work with Peewee 3 and Python 3 using new `secrets` and `hashlib` from standard library, without dependencies, dont need `bcrypt`,
internally uses `hashlib.pbkdf2_hmac()` and `secrets.compare_digest()`.
Migration from `PasswordField` to `SimplePasswordField` is recommended when possible.

[`PasswordField` is explicitly no longer supported and deprecated by Peewee.](https://github.com/coleifer/peewee/issues/1444#issue-292958082)

`SimplePasswordField` stores a password hash and lets you verify it.
The password is hashed when it is saved to the database and
after reading it from the database you can call:
`check_password(password)` to return a `bool`.

**Arguments:**
- `salt` Salt for Password hashing, string type, required, use some random string, check `secrets.token_hex()` and `secrets.token_urlsafe()` as sources of random strings.
- `min_length` Minimum Password length, optional, integer type, positive value, defaults to `8`.
- `algorithm` Algorithm for Password hashing, optional, string type, dafaults to `"sha512"`.
- `iterations` Iterations for Password hashing, optional, integer type, positive value, defaults to `100_000`.
- `dklen` Output Hash length, optional, integer type or `None`, positive value, defaults to `None`, automatic and constant length based on `algorithm` is used if set to `None`.

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `CharField`).

**Returns:** `str`.

**Base Class:** `CharField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import SimplePasswordField
>>> SimplePasswordField(salt="abc").db_value("123456789")
'46b071b59b995e1a668e68d2112b829ad04e0d988ac989ba2ecc0e56ad8a72780081381f2b6f38573d294454b569d7f1d3bce9cc08edcec6f68f6584357b72a9'

```

</details>


- [Check an actual working Example copied from official Peewee docs.](https://github.com/juancarlospaco/peewee-extra-fields/blob/master/example.py) Run it executing on the terminal command line: `python example.py`.


# Install:

```
pip install peewee_extra_fields
```


# Requisites:

- [Peewee](http://docs.peewee-orm.com) *(2.x or 3.x Versions)*

**Optional:**

- [BCrypt](https://github.com/pyca/bcrypt) *(Only for PasswordField)*


# Tests

- Pull requests to improve tests are welcome!!!.

```bash
python -m unittest --verbose --locals tests.TestFields
# OR
python -m unittest
# OR
pytest
```

- [Test Templates.](https://gist.github.com/juancarlospaco/040fbe326631e638f2a540fe8c1f2092)


### Why?

This is not designed to replace Validators AKA Schemas. We use and recommend Schemas.

This is to give more context and make Peewee for Humans.

Lets imagine you have a `Charfield` with value `"al"` and the Validator returns `True`.
But whats `"al"`?, the republic of Albania?, the US State of Alabama?, a wrong value?,
some abbreviation?, a short-code?, some other ISO standard?, a name?, a random string?.


But if you have a `CountryISOCodeField` you already know you are working with Countries,
and the field follows the ISO-3166, and the string is a Country Code,
and that the string value will Validate if it respects the Standard ISO-3166, then you see:

```python
CountryISO3166(iso3166_a3='ALB', iso3166_numeric=8, capital='Tirana', continent='Europe', currency_code='ALL', currency_name='Lek', geoname_id=783754, is_developed=True, is_independent=True, languages=['sq', 'el'], name='Albania', name_human='The Republic Of Albania', phone_code='355', timezones=['europe/tirane'], tld='.al')
```

That gives a lot more context, than just an `"al"`. :smile_cat:


### Contributors:

- **Please Star this Repo on Github !**, it helps to show up faster on searchs.
- [Help](https://help.github.com/articles/using-pull-requests) and more [Help](https://help.github.com/articles/fork-a-repo) and Interactive Quick [Git Tutorial](https://try.github.io).
- English is the primary default spoken language, unless explicitly stated otherwise *(eg. Dont send Translation Pull Request)*
- Pull Requests for working passing unittests welcomed.


### Licence:

- GNU GPL Latest Version and GNU LGPL Latest Version and any Licence YOU Request via Bug Report.


### Ethics and Humanism Policy:

- Religions is not allowed. Contributing means you agree with the COC.


### Challenge

<details>

**Contributor:**

- Contributor must be 1 individual person (+18) that self-identify as Girl/Woman.
- Contributor must be living on Argentina, Antartida(AR) or Malvinas Argentinas.
- Contributor must agree with COC, Licences and general project philosophies.
- Contributor must Star, Fork and Pull Request the project on GitHub as usual.
- Contributor must provide 1 complete active valid written C.B.U. number.
- Payment delays 1 week (working days, not include bank delay), for peer reviews.
- Impersonations, fakes, bots, trolls, companies, organizations, Not allowed.

**Contribution:**

- Contribution must pass Ok all Unittests, CI, QA, Prospector, PreCommit, etc.
- Contribution must be 100% Python 3.6+ code, not C/C++/Go/Rust compiled module.
- Contribution must be 100% English language, correct grammar and punctuation.
- Contribution are manually evaluated 1 at a time, else it enters a queue.
- If someone already submitted the same Contribution dont submit the duplicated.
- Obfuscation, autogenerated-code, Code-Golf, overcomplicated, kludge, Not allowed.

**Target:**

Submit 1 of the following items (pick one):

- 1 Pull Request per 1 Contributor with passing Unittests for current Features (Unittests for actual code on the Repo).
- 1 Pull Request per 1 Contributor with 1 new relevant Feature with 1 Unittest (New Feature with at least 1 Unittest).

**Prize:**

- 1000 ARS.

We are investigating changing to Bitcoin prize eventually. If you dont understand the Challenge contact me before proceeding.

</details>
