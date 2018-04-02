#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Extra Fields for Peewee ORM. Argentina Fields."""


import re

from peewee import CharField


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

    @staticmethod
    def cuit2dni(value: str) -> int:  # Helper, takes CUIT returns DNI.
        return int(value.replace("-", "")[2:-1])  # Removes the XX- and -X.

    @staticmethod
    def get_html_widget(clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        clas = f'''class="{' '.join(clas)}" ''' if clas else ""
        ids = f'id="{ids}" ' if ids else ""
        r = "required " if required else ""
        return ('<input type="text" name="cuit" placeholder="CUIT Argentino" '
                f'{ids}{clas}{r}minlength="10" maxlength="13" size="13">\n')
