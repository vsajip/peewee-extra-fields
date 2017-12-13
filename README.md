# peewee-extra-fields

[Extra additional Fields](http://docs.peewee-orm.com/en/latest/peewee/models.html#creating-a-custom-field) for [Peewee ORM.](http://docs.peewee-orm.com)

CSVField, CharFieldCustom, CountryISOCodeField, CurrencyISOCodeField, IPAddressField, IPNetworkField, LanguageISOCodeField, PastDateField, PastDateTimeField, PositiveDecimalField, PositiveFloatField, PositiveIntegerField and more.

We want to be a hub for all custom Fields. If your created a Custom Peewee Field feel free to [Send Pull Requests!!!.](https://github.com/juancarlospaco/peewee-extra-fields/compare)

![screenshot](https://source.unsplash.com/IClZBVw5W5A/800x400 "Illustrative Photo by https://unsplash.com/@toddquackenbush")

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg)](http://opensource.org/licenses/GPL-3.0)
[![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg)](http://opensource.org/licenses/LGPL-3.0)
[![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg)](http://python.org)


# Documentation

##### PositiveIntegerField
<details>

`peewee_extra_fields.PositiveIntegerField()`

**Description:** [`IntegerField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Positive** values (>= 0).

**Arguments:** None (should take the same `*args` and `**kwargs` as `IntegerField`)

**Keyword Arguments:** None (should take the same `*args` and `**kwargs` as `IntegerField`).

**Returns:** `int`.

**Base Class:** `IntegerField`.

**Type:** `<class 'type'>`.

**Source Code file:** https://github.com/juancarlospaco/peewee-extra-fields/blob/master/peewee_extra_fields.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from peewee_extra_fields import PositiveIntegerField
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

```
</details>


##### PastDateTimeField
<details>

`peewee_extra_fields.PastDateTimeField()`

**Description:** [`DateTimeField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts dates **Not on the Future** values.
Past is Ok, Present is Ok, Future is Not Ok.
Most of times you need DateTimes on the Past, eg. your Birthday cant be in the Future.

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

```
</details>



##### LanguageISOCodeField
<details>

`peewee_extra_fields.LanguageISOCodeField()`

**Description:** [`FixedCharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Language ISO Code** values (ISO-639_1).
Uses hardcoded `max_length = 2`.

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
>>> LanguageISOCodeField().db_value("not valid")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: LanguageISOCodeField Value is 9 Characters long instead of 2 Characters long (valid values must be ISO-639_1 Language Codes): not valid.

>>> LanguageISOCodeField().db_value("xx")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ValueError: LanguageISOCodeField Value is not an ISO-639_1 Standard Language Code of 2 Characters long (valid values must be ISO-639_1 Language Codes): xx.

>>> LanguageISOCodeField().python_value("es")
LanguageISO639(code='es', name='Spanish')
>>> LanguageISOCodeField().python_value("en")
LanguageISO639(code='en', name='English')
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

```
</details>


##### ARPostalCodeField
<details>

`peewee_extra_fields.ARPostalCodeField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Argentine Postal Codes** (old & new).

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

```
</details>


##### ARCUITField
<details>

`peewee_extra_fields.ARCUITField()`

**Description:** [`CharField`](http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table) subclass but only accepts **Argentine CUIT**, also it can extract DNI from CUIT.

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

```
</details>

- [Check an actual working Example copied from official Peewee docs.](https://github.com/juancarlospaco/peewee-extra-fields/blob/master/example.py)


# Requisites:

- [Peewee](http://docs.peewee-orm.com)


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


### Contributors:

- **Please Star this Repo on Github !**, it helps to show up faster on searchs.
- [Help](https://help.github.com/articles/using-pull-requests) and more [Help](https://help.github.com/articles/fork-a-repo) and Interactive Quick [Git Tutorial](https://try.github.io).
- English is the primary default spoken language, unless explicitly stated otherwise *(eg. Dont send Translation Pull Request)*
- Pull Requests for working passing unittests welcomed.


### Licence:

- GNU GPL Latest Version and GNU LGPL Latest Version and any Licence YOU Request via Bug Report.


### Ethics and Humanism Policy:

- Religions is not allowed. Contributing means you agree with the COC.
