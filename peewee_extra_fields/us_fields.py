#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Extra Fields for Peewee ORM. US Fields."""


import re

from collections import namedtuple

from peewee import FixedCharField


class USSocialSecurityNumberField(FixedCharField):
    """FixedCharField clone but only accepts USA Social Security Numbers."""
    max_length = 11

    def db_value(self, value: str) -> str:
        if isinstance(value, str):

            value = value.strip()

            if len(value) != 11:
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (valid values must be exactly 11 Characters): {value}.""")

            us_social_security_number_regex = re.compile(
                r"^(?P<area>\d{3})[-\ ]?(?P<group>\d{2})[-\ ]?(?P<sri>\d{4})$")
            match = re.match(us_social_security_number_regex, value)

            if not match:
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (valid Social Security Number values be a must match a Regex
                {us_social_security_number_regex}): {value} -> {match}.""")

            area = match.groupdict()['area']
            group =  match.groupdict()['group']
            serial = match.groupdict()['sri']

            if area == '000':
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (valid Area must not be all Zeroes): {value} -> {area}.""")

            if group == '00':
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (valid Group must not be all Zeroes): {value} -> {group}.""")

            if serial == '0000':
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (valid Serial must not be all Zeroes): {value} -> {serial}.""")

            if area == '666':
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (Block '666' will never be allocated): {value} -> {area}.""")

            if area.startswith('9'):
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (Block '9**' is in the 'promotional block' 987-65-4320 through
                987-65-4329, is permanently invalid): {value} -> {area}.""")

            if ((area == '078' and group == '05' and serial == '1120') or
                (area == '219' and group == '09' and serial == '9999')):
                raise ValueError(f"""{self.__class__.__name__} Value is not a
                valid U.S.A. Social Security Number string (XXX-XX-XXXX format)
                (promo & permanently invalid numbers): {value} -> {area}.""")

            return str(f"{area}-{group}-{serial}")

        return value

    def python_value(self, value: str) -> namedtuple:
        if value and isinstance(value, str):
            return namedtuple(
                "USSocialSecurityNumber", "ssn area group serial")(
                    value, int(value[:3]), int(value[4:6]), int(value[7:]))
        return value
