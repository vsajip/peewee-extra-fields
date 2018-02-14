#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Extra Fields for Peewee ORM. Regex based extra Fields live here."""


import re

from peewee import CharField


__all__ = ("SemVerField", "ARPostalCodeField", "USZipCodeField")


class _BaseRegexField(CharField):
    regex = None
    max_length = 255

    def db_value(self, value: str) -> str:
        if isinstance(value, str):
            value = value.strip()

            if value == "":
                RuntimeWarning(
                    f"{self.__class__.__name__}: Value is an Empty string!.")

            if len(value) > self.max_length:
                raise ValueError((
                    f"{self.__class__.__name__}: Value string is too long!. "
                    f"(valid values must be < {self.max_length} Characters):"
                    f" {len(value)} > {self.max_length} Characters, {value}."
                    ))

            if not re.match(self.regex, value):
                raise ValueError((
                    f"{self.__class__.__name__}: Value string is not valid!. "
                    f"(valid values must match a Regex {self.regex}): {value}."
                    ))

        return value


class SemVerField(_BaseRegexField):
    """CharField clone only accepts Semantic Versions (https://semver.org)."""
    regex = str(
        r"\bv?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[\d"
        r"a-z-]+(?:\.[\da-z-]+)*)?(?:\+[\da-z-]+(?:\.[\da-z-]+)*)?\b")


class ARPostalCodeField(_BaseRegexField):
    """CharField clone but only accepts Argentine Postal Codes (old & new)."""
    max_length = 8  # New = 8, Old = 4
    regex = r'^\d{4}$|^[A-HJ-NP-Za-hj-np-z]\d{4}\D{3}$'

    @staticmethod
    def get_html_widget(clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""
        r = "required " if required else ""
        return (f'<input type="text" name="postal-code" {ids}{clas}{r} '
                'placeholder="Codigo Postal Argentino" '
                'minlength="4" maxlength="8" size="8">\n')


class USZipCodeField(_BaseRegexField):
    """CharField clone but only accepts US ZIP Codes (XXXXX or XXXXX-XXXX)."""
    max_length = 10
    regex = r'^\d{5}(?:-\d{4})?$'
