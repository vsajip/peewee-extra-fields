#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Extra Fields for Peewee ORM."""


import re
from collections import namedtuple
from datetime import date, datetime
from decimal import Decimal
from ipaddress import IPv4Address, IPv4Network, ip_address, ip_network
from json import loads
from pathlib import Path
from types import MappingProxyType as frozendict

from peewee import (CharField, DateField, DateTimeField, DecimalField,
                    FixedCharField, FloatField, IntegerField,
                    SmallIntegerField, BigIntegerField)


__version__ = "1.5.0"
__license__ = "GPLv3+ LGPLv3+"
__author__ = "Juan Carlos"
__email__ = "juancarlospaco@gmail.com"
__contact__ = "https://t.me/juancarlospaco"
__maintainer__ = "Juan Carlos"
__url__ = "https://github.com/juancarlospaco/peewee-extra-fields"
__all__ = ('ARCUITField', 'ARPostalCodeField', 'CSVField',
           'CharFieldCustom', 'CountryISOCodeField', 'CurrencyISOCodeField',
           'IPAddressField', 'IPNetworkField', 'LanguageISOCodeField',
           'PastDateField', 'PastDateTimeField', 'PositiveDecimalField',
           'PositiveFloatField', 'PositiveIntegerField',
           'PositiveSmallIntegerField', 'PositiveBigIntegerField')


##############################################################################


ISO639_1: dict = frozendict(loads(
    (Path(__file__).parent / "languages-data.json").read_bytes()))

ISO4217: dict = frozendict(loads(
    (Path(__file__).parent / "currency-data.json").read_bytes()))

ISO3166: dict = frozendict(loads(
    (Path(__file__).parent / "country-data.json").read_bytes()))

INT2COUNTRY: dict = frozendict(loads(
    (Path(__file__).parent / "int2country.json").read_bytes()))

INT2CURRENCY: dict = frozendict(loads(
    (Path(__file__).parent / "int2currency.json").read_bytes()))


##############################################################################


class PositiveSmallIntegerField(SmallIntegerField):
    """SmallIntegerField clone but only accepts Positive values (>= 0)."""

    # https://www.postgresql.org/docs/current/static/datatype-numeric.html
    min = 0
    max = 32_767

    def db_value(self, value):
        if value and isinstance(value, int):
            if value < self.min or value > self.max:
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                Positive Integer (valid values must be Positive Integers
                between {self.min} and {self.max}): {value}.""")
        return value


class PositiveIntegerField(IntegerField):
    """IntegerField clone but only accepts Positive values (>= 0)."""

    # https://www.postgresql.org/docs/current/static/datatype-numeric.html
    min = 0
    max = 2_147_483_647

    def db_value(self, value):
        if value and isinstance(value, int):
            if value < self.min or value > self.max:
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                Positive Integer (valid values must be Positive Integers
                between {self.min} and {self.max}): {value}.""")
        return value


class PositiveBigIntegerField(BigIntegerField):
    """BigIntegerField clone but only accepts Positive values (>= 0)."""

    # https://www.postgresql.org/docs/current/static/datatype-numeric.html
    min = 0
    max = 9_223_372_036_854_775_807

    def db_value(self, value):
        if value and isinstance(value, int):
            if value < self.min or value > self.max:
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                Positive Integer (valid values must be Positive Integers
                between {self.min} and {self.max}): {value}.""")
        return value


class PositiveFloatField(FloatField):
    """FloatField clone but only accepts Positive values (>= 0).

    Optionally it can round Floats using Pythons round() with round_by arg."""

    def __init__(self, round_by: int=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(round_by, int) and round_by <= 0:  # round_by is 0.
            raise ValueError(f"""{self.__class__.__name__} 'round_by' argument
            is not a Non-Zero Positive Integer number
            (valid values must be Integers > 0): {round_by}.""")
        if round_by and isinstance(round_by, int) and round_by > 0:
            self.round_by = int(round_by)
        else:
            self.round_by = None

    def db_value(self, value):

        if value and value < 0:
            raise ValueError(f"""{self.__class__.__name__} Value is not a
            Positive Float (valid values must be Floats >=0): {value}.""")

        if value and self.round_by:
            value = round(value, self.round_by)

        return value


class PositiveDecimalField(DecimalField):
    """DecimalField clone but only accepts Positive values (>= 0).

    Optionally it can round Decimal using Decimal().quantize().normalize()."""

    def __init__(self, round_by: int=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(round_by, int) and round_by <= 0:  # round_by is 0.
            raise ValueError(f"""{self.__class__.__name__} 'round_by' argument
            is not a Non-Zero Positive Integer numbers
            (valid values must be Integers > 0): {round_by}.""")
        if round_by and isinstance(round_by, int) and round_by > 0:
            self.round_by = int(round_by)
        else:
            self.round_by = None

    def db_value(self, value):

        if value and value < 0:
            raise ValueError(f"""{self.__class__.__name__} Value is not a
            Positive Decimal (valid values must be Decimals >=0): {value}.""")

        if value and self.round_by:
            value = Decimal(value).quantize(
                Decimal(10) ** -self.round_by).normalize()

        return value


class IPAddressField(CharField):
    """CharField clone but only accepts IP Address values, returns ip_address.

    Inspired by:
    docs.djangoproject.com/en/1.11/ref/models/fields/#genericipaddressfield and
    https://devdocs.io/python~3.6/library/ipaddress."""

    def db_value(self, value: str) -> str:
        if value and isinstance(value, str):
            try:
                ip_address(value)
            except Exception as error:
                raise ValueError(f"""{self.__class__.__name__} Value string is
                not a Valid IP v4 or v6 Address (valid values must be a valid
                {ip_address} {IPv4Address}): {value} --> {error}.""")
            else:
                return value  # is a valid IPv4Address or IPv6Address.
        return value          # is None.

    def python_value(self, value: str) -> IPv4Address:
        return ip_address(value) if value else value


class IPNetworkField(CharField):
    """CharField clone but only accepts IP Network values, returns ip_network.

    Inspired by:
    docs.djangoproject.com/en/1.11/ref/models/fields/#genericipaddressfield and
    https://devdocs.io/python~3.6/library/ipaddress."""

    def db_value(self, value: str) -> str:
        if value and isinstance(value, str):
            try:
                ip_network(value)
            except Exception as error:
                raise ValueError(f"""{self.__class__.__name__} Value string is
                not a Valid IP v4 or v6 Network (valid values must be a valid
                {ip_network} {IPv4Network}): {value} --> {error}.""")
            else:
                return value  # is a valid IPv4Network or IPv6Network.
        return value          # is None.

    def python_value(self, value: str) -> IPv4Network:
        return ip_network(value) if value else value


class PastDateTimeField(DateTimeField):
    """DateTimeField clone but dont allow Dates and Times on the Future.

    Past is Ok, Present is Ok, Future is Not Ok.
    Most of times you need DateTimes on Past,eg. Bday cant be in the Future."""

    def db_value(self, value):
        # developer.mozilla.org/en/docs/Web/HTML/Element/input/datetime-local
        if value and isinstance(value, str):
            if datetime.strptime(r'%Y-%m-%dT%H:%M', value) > datetime.utcnow():
                raise ValueError(f"""{self.__class__.__name__} Dates & Times
                Value is not in the Past (valid values must be in the Past):
                {value} > {datetime.utcnow().isoformat()}.""")
        if value and isinstance(value, datetime):
            if value > datetime.utcnow():
                raise ValueError(f"""{self.__class__.__name__} Dates & Times
                Value is not in the Past (valid values must be in the Past):
                {value} > {datetime.utcnow().isoformat()}.""")
        return value

    def get_html_widget(self, clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""
        r = "required " if required else ""
        return (f'<input type="datetime-local" name="datetime" {ids}{clas}{r}'
                f'''max="{datetime.utcnow().strftime('%Y-%m-%dT%H:%M')}">\n''')


class PastDateField(DateField):
    """DateField clone but dont allow Dates on the Future.

    Past is Ok, Present is Ok, Future is Not Ok.
    Most of times you need Dates on the Past,eg. Bday cant be in the Future."""

    def db_value(self, value):  # check if its valid for date()
        if value and isinstance(value, str):
            # http:developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date
            if datetime.strptime(value, r'%Y-%m-%d').date() > date.today():
                raise ValueError(f"""{self.__class__.__name__} Dates Value is
                not in the Past (valid values must be in the Past or Present):
                {value} > {date.today()}.""")
        if value and isinstance(value, date):
            if value > date.today():
                raise ValueError(f"""{self.__class__.__name__} Dates Value is
                not in the Past (valid values must be in the Past or Present):
                {value} > {date.today()}.""")
        return value

    def get_html_widget(self, clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""
        r = "required " if required else ""
        return (f'<input type="date" name="date" {ids}{clas}{r} '
                f'max="{date.today()}">\n')


class LanguageISOCodeField(FixedCharField):
    """FixedCharField clone only accepts Language ISO Code values.

    Returns 1 namedtuple with 2-chars code str and human-friendly name str.
    I cant find an ISO-Numeric standard mapping to optimize this to SmallInt."""
    max_length = 2

    def db_value(self, value: str) -> str:
        if value and isinstance(value, str):
            value = value.lower().strip()

            if len(value) != 2:
                raise ValueError(f"""{self.__class__.__name__} Value is
                {len(value)} Characters long instead of 2 Characters long
                (valid values must be ISO-639_1 Language Codes): {value}.""")

            if len(value) == 2 and value not in ISO639_1:
                raise ValueError(f"""{self.__class__.__name__} Value is not an
                ISO-639_1 Standard Language Code of 2 Characters long
                (valid values must be ISO-639_1 Language Codes): {value}.""")

        return value

    def python_value(self, value: str) -> namedtuple:
        if value and isinstance(value, str):
            lang = ISO639_1.get(value).get  # OPTIMIZATION
            return namedtuple("LanguageISO639", "code name name_native")(
                value, lang("name").title(), lang("name_native").title())

        return value

    def get_html_widget(self, clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""

        r = 'required="required" ' if required else ""
        html_widget = (f'<select name="language" {ids}{clas}{r}>\n'
                       '    <option selected disabled value=""></option>\n')

        for lang in ISO639_1.items():
                html_widget += (
                    f'    <option value="{lang[0]}">({lang[0].upper()}) '
                    f'{lang[1]["name"].title()} ({lang[1]["name_native"]})'
                    '</option>\n')
        else:
            html_widget += '</select>\n'
            return html_widget


class CountryISOCodeField(SmallIntegerField):
    """SmallIntegerField clone only accepts Country ISO Code string values.

    It converts the 2-Characters Country ISO Code to integer Country ISO Code,
    saves to Database the SmallInt, when reading from Database, reverts back,
    small integer Country ISO Code to 2-Characters string Country ISO Code.

    Returns 1 namedtuple with iso3166_a3, iso3166_numeric, capital, continent,
    currency_code, currency_name, geoname_id, is_developed, is_independent,
    languages, name, name_human, phone_code, timezones and tld.

    This always stores only small positive Integer numbers of 3 digits max,
    that maps 1-to-1 to 2-Characters string Country Codes, according to ISO.

    Small integer is always faster than varchar or text in every aspect.
    """

    def db_value(self, value: str) -> int:
        if value and isinstance(value, str):
            value = value.lower().strip()

            if len(value) != 2:
                raise ValueError(f"""{self.__class__.__name__} Value is
                {len(value)} Characters long instead of 2 Characters long
                (valid values must be ISO-3166 Country Codes): {value}.""")

            if len(value) == 2 and value not in ISO3166:
                raise ValueError(f"""{self.__class__.__name__} Value is not an
                ISO-3166 Standard Country Code of 2 Characters long
                (valid values must be ISO-3166 Country Codes): {value}.""")

            if len(value) == 2 and value in ISO3166:  # str -> int.
                value = int(ISO3166.get(value).get("iso3166_numeric"))

        return value

    def python_value(self, value: int) -> namedtuple:
        if value and isinstance(value, int):
            value = INT2COUNTRY[str(value)]  # int -> str.
            country = ISO3166[value].get  # OPTIMIZATION

            return namedtuple(
                "CountryISO3166",
                ("iso3166_a3 iso3166_numeric capital continent currency_code "
                 "currency_name geoname_id is_developed is_independent "
                 "languages name name_human phone_code timezones tld")
                )(
                country("iso3166_a3").upper(),
                country("iso3166_numeric"),
                country("capital").title(),
                country("continent").title(),
                country("currency_code").upper(),
                country("currency_name").title(),
                country("geoname_id"),
                country("is_developed"),
                country("is_independent"),
                country("languages"),
                country("name").title(),
                country("name_human").title(),
                country("phone_code"),
                country("timezones"),
                country("tld"),
            )

        return value

    def get_html_widget(self, clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""

        r = 'required="required" ' if required else ""
        html_widget = (f'<select name="country" {ids}{clas}{r}>\n'
                       '    <option selected disabled value=""></option>\n')

        for c in ISO3166.items():
            html_widget += (
                f'    <option value="{c[0]}" data-iso3166numeric="'
                f'''{str(str(c[1]["iso3166_numeric"]) + '"').ljust(4)} '''
                f'data-iso3166a3="{c[1]["iso3166_a3"]}">({c[0].upper()}) '
                f'{c[1]["name"].title()}</option>\n')
        else:
            html_widget += '</select>\n'
            return html_widget


class CurrencyISOCodeField(SmallIntegerField):
    """SmallIntegerField clone only accepts Currency ISO Code values.

    It converts 3-Characters Currency ISO Code to integer Currency ISO Code,
    saves to Database the SmallInt, when reading from Database, reverts back,
    small integer Currency ISO Code to 3-Characters string Currency ISO Code.

    Returns 1 namedtuple with code, name, iso4217_numeric.

    This always stores only small positive Integer numbers of 3 digits max,
    that maps 1-to-1 to 3-Characters string Currency Codes, according to ISO.

    Small integer is always faster than varchar or text in every aspect.
    """

    def db_value(self, value: str) -> int:
        if value and isinstance(value, str):
            value = value.lower().strip()

            if len(value) != 3:
                raise ValueError(f"""{self.__class__.__name__} Value is
                {len(value)} Characters long instead of 3 Characters long
                (valid values must be ISO-4217 Currency Codes): {value}.""")

            if len(value) == 3 and value not in ISO4217:
                raise ValueError(f"""{self.__class__.__name__} Value is not an
                ISO-4217 Standard Currency Code of 3 Characters long
                (valid values must be ISO-4217 Currency Codes): {value}.""")

            if len(value) == 3 and value in ISO4217:  # str -> int.
                value = int(ISO4217.get(value).get("iso4217_numeric"))

        return value

    def python_value(self, value: int) -> namedtuple:
        if value and isinstance(value, int):
            value = INT2CURRENCY.get(str(value))  # int -> str.

            return namedtuple("CurrencyISO4217", "code name iso4217_numeric")(
                value,
                ISO4217.get(value).get("name").title(),
                ISO4217.get(value).get("iso4217_numeric")
            )

        return value

    def get_html_widget(self, clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""
        not_bill_money = ("che", "chw", "clf", "cou", "mxv", "usn", "uss",
                          "xag", "xau", "xba", "xbb", "xbc", "xbd", "xdr",
                          "xpd", "xpt", "xsu", "xts", "xua", "xxx", "uyi")

        r = 'required="required" ' if required else ""
        html_widget = (f'<select name="currency" {ids}{clas}{r}>\n'
                       '    <option selected disabled value=""></option>\n')

        for mon in ISO4217.items():
            if mon[0] not in not_bill_money:
                html_widget += (
                    f'    <option value="{mon[0]}" data-iso4217numeric="'
                    f'''{str(str(mon[1]["iso4217_numeric"]) + '"').ljust(4)}>'''
                    f'({mon[0].upper()}) {mon[1]["name"].title()}'
                    '</option>\n')
        else:
            html_widget += '</select>\n'
            return html_widget


class CharFieldCustom(CharField):
    """CharField clone but has additional options, min_len,blacklist,etc."""
    # TODO improve blacklist/whitelist matching somehow?, how?.  Better Name?.
    def __init__(self, min_lenght: int=None, use_lower: bool=False,
                 blacklist: tuple=None, whitelist: tuple=None,
                 force_ascii: str=None, force_slugify: bool=False,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.blacklist = tuple(sorted(set(blacklist))) if blacklist else None
        self.whitelist = tuple(sorted(set(whitelist))) if whitelist else None
        self.min_lenght = int(min_lenght) if min_lenght else None
        self.force_ascii = force_ascii
        self.force_slugify = force_slugify
        self.use_lower = use_lower

    def db_value(self, value):

        if value and self.use_lower:
            value = value.lower()

        if value and self.min_lenght and not len(value) >= self.min_lenght:
            raise ValueError(
                (f"{self} Value string is too short (valid values must be a "
                 f"string of {self.min_lenght} characters or more): {value}."))

        if value and self.blacklist and value.lower() in self.blacklist:
            raise ValueError(f"{self} Value string is black-listed: {value}.")

        if value and self.whitelist and value.lower() not in self.whitelist:
            raise ValueError((f"{self} Value string requires at least 1 "
                              "white-listed value present: {value}."))

        if value and self.force_ascii is not None:
            value = re.sub(r"[^\x00-\x7F]+", self.force_ascii,
                           value, flags=re.IGNORECASE)

        if value and self.force_slugify:
            value = re.sub(r'[^a-z0-9_\-]+', '-', value, flags=re.IGNORECASE)

        return value


class CSVField(CharField):
    """CharField clone but only accepts CSV string values (comma separated).

    Does not accepts CSV Headers. Has options for separator, set, sorted.
    Set and Sorted options may alter original order, use with caution.

    Inspired by CommaSeparatedIntegerField from Django."""
    # TODO Use other DB Type?, Array?, How?.
    def __init__(self, separator: str=",", use_set: bool=False,
                 use_sorted: bool=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.separator_character = str(separator)
        self.use_set = bool(use_set)
        self.use_sorted = bool(use_sorted)

    def db_value(self, value: str) -> str:
        if value and isinstance(value, str):
            value = value.split(self.separator_character)  # str -> list

            if self.use_set:           # list -> set
                value = set(value)     # Lost of Order!.

            if self.use_sorted:        # list -> list
                value = sorted(value)  # Lost of Order?.

            value = self.separator_character.join(value)
        return value

    def python_value(self, value: str) -> tuple:
        return tuple(value.split(self.separator_character) if value else [])


##############################################################################


class ARPostalCodeField(CharField):
    """CharField clone but only accepts Argentine Postal Codes (old & new)."""
    max_length = 8  # New = 8, Old = 4

    def db_value(self, value: str) -> str:
        if value and isinstance(value, str):
            postal_code_regex = r'^\d{4}$|^[A-HJ-NP-Za-hj-np-z]\d{4}\D{3}$'
            if not re.match(postal_code_regex, value) or len(value) < 4:
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid Argentine Postal Code (old or new) string from 4 to 8
                characters long (valid values must match a Regex
                {postal_code_regex}): {value}.""")

        return value

    def get_html_widget(self, clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""
        r = "required " if required else ""
        return (f'<input type="text" name="postal-code" {ids}{clas}{r} '
                'placeholder="Codigo Postal Argentino" '
                'minlength="4" maxlength="8" size="8">\n')


class ARCUITField(CharField):
    """CharField clone but only accepts Argentine CUIT, also extracts DNI."""
    max_length = 14  # 11 Digits + 2 Hyphens.

    def db_value(self, value: str) -> str:
        if value and isinstance(value, str):
            cuit_code_regex = r'^\d{2}-?\d{8}-?\d$'
            if not re.match(cuit_code_regex, value) or len(value) < 10:
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid Argentine CUIT Code string of 11 to 13 characters long
                (valid values must match Regex {cuit_code_regex}): {value}.""")
            value = value.replace("-", "")

        return value

    def cuit2dni(self, value: str) -> int:  # Helper, takes CUIT returns DNI.
        return int(value.replace("-", "")[2:-1])  # Removes the XX- and -X.

    def get_html_widget(self, clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""
        r = "required " if required else ""
        return ('<input type="text" name="cuit" placeholder="CUIT Argentino" '
                f'{ids}{clas}{r}minlength="10" maxlength="13" size="13">\n')


# Most Wanted Fields:
# - GeometryField
# - PointField
# - LineStringField
# - PolygonField
# - MultiPointField
# - MultiLineStringField
# - MultiPolygonField
# - GeometryCollectionField
# - RasterField
