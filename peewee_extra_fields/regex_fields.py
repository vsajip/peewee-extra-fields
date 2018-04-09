#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Extra Fields for Peewee ORM. Regex based extra Fields live here."""


import re

from peewee import CharField


class _BaseRegexField(CharField):
    regex = None
    min_length = 1
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

            if len(value) < self.min_length:
                raise ValueError((
                    f"{self.__class__.__name__}: Value string is too short!. "
                    f"(valid values must be > {self.min_length} Characters):"
                    f" {len(value)} < {self.min_length} Characters, {value}."
                ))

            if not re.match(self.regex, value):
                raise ValueError((
                    f"{self.__class__.__name__}: Value string is not valid!. "
                    f"(valid values must match a Regex {self.regex}): {value}."
                ))

        return value


class SemVerField(_BaseRegexField):
    """Semantic Versions Field (https://semver.org)."""
    regex = str(
        r"\bv?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[\d"
        r"a-z-]+(?:\.[\da-z-]+)*)?(?:\+[\da-z-]+(?:\.[\da-z-]+)*)?\b")


class HexadecimalField(_BaseRegexField):
    """Hexadecimal String Field,stores arbitrary Hexadecimal string(255 Chars).

    Useful for Promo Codes, Redeem Codes, Invitation Codes, etc etc."""
    regex = r"^(([0-9A-f])|(0x[0-9A-f]))+$"


class ARZipCodeField(_BaseRegexField):
    """Argentine Postal Codes Field (old & new)."""
    min_length = 4
    max_length = 8  # New = 8, Old = 4
    regex = r'^\d{4}$|^[A-HJ-NP-Za-hj-np-z]\d{4}\D{3}$'

    @staticmethod
    def get_html_widget(clas: tuple=None, ids: str=None,
                        required: bool=False) -> str:
        klas = f'''class="{' '.join(clas)}" ''' if clas else ""
        idz = f'id="{ids}" ' if ids else ""
        r = "required " if required else ""
        return str(f'<input type="text" name="postal-code" {idz}{klas}{r} '
                   'placeholder="Codigo Postal Argentino" '
                   'minlength="4" maxlength="8" size="8">\n')


class USZipCodeField(_BaseRegexField):
    """US ZIP Codes Field (XXXXX or XXXXX-XXXX)."""
    min_length = 5
    max_length = 10
    regex = r'^\d{5}(?:-\d{4})?$'


class ATZipCodeField(_BaseRegexField):
    """Austria ZIP Codes Field (4 digits)."""
    min_length = 4
    max_length = 4
    regex = r'^[1-9]{1}\d{3}$'


class AUZipCodeField(_BaseRegexField):
    """Australia ZIP Codes Field (4 digits)."""
    min_length = 4
    max_length = 4
    regex = r'^\d{4}$'


class BEZipCodeField(_BaseRegexField):
    """Belgium ZIP Codes Field (4 digits)."""
    min_length = 4
    max_length = 4
    regex = r'^[1-9]\d{3}$'


class BRZipCodeField(_BaseRegexField):
    """Brazil ZIP Code Field (XXXXX-XXX format)."""
    min_length = 8
    max_length = 10
    regex = r'^\d{5}-\d{3}$'


class CHZipCodeField(_BaseRegexField):
    """Swiss ZIP Code Field (4 digits)."""
    min_length = 4
    max_length = 4
    regex = r'^[1-9]\d{3}$'


class CLRutField(_BaseRegexField):
    """Chile "Rol Unico Tributario" (RUT) Field.

    This is the Chilean national identification number. 'XX.XXX.XXX-X' format.
    More info: https://palena.sii.cl/cvc/dte/ee_empresas_emisoras.html."""
    max_length = 14
    regex = r'^(\d{1,2}\.)?\d{3}\.\d{3}-[\dkK]$'


class CNZipCodeField(_BaseRegexField):
    """China ZIP Code (Mainland, 6 Digit) Field."""
    min_length = 6
    max_length = 6
    regex = r'^\d{6}$'


class CONITField(_BaseRegexField):
    """Colombia NIT Field.

    Numero de IdentificaciOn Tributaria. NIT is of the form XXXXXXXXXX-V.
    The last digit is a check digit. NIT can be used for people and companies.

    http://es.wikipedia.org/wiki/N%C3%BAmero_de_Identificaci%C3%B3n_Tributaria.
    """
    min_length = 5
    max_length = 12
    regex = r'^\d{5,12}-?\d$'


class CUZipCodeField(_BaseRegexField):
    """Cuba ZIP Codes (5 Digits) Field.

    http://mapanet.eu/Postal_Codes/?C=CU."""
    min_length = 5
    max_length = 6
    regex = r'^[1-9]\d{4}$'


class CZZipCodeField(_BaseRegexField):
    """Czech ZIP Code Field (XXXXX or XXX XX)."""
    min_length = 5
    max_length = 6
    regex = r'^\d{5}$|^\d{3} \d{2}$'


class DEZipCodeField(_BaseRegexField):
    """German ZIP Code Field (5 Digits)."""
    min_length = 5
    max_length = 5
    regex = r'^([0]{1}[1-9]{1}|[1-9]{1}[0-9]{1})[0-9]{3}$'


class EEZipCodeField(_BaseRegexField):
    """Estonia ZIP Code Field (5 Digits)."""
    min_length = 5
    max_length = 5
    regex = r'^[1-9]\d{4}$'


class ESZipCodeField(_BaseRegexField):
    """Spain ZIP Code Field (5 Digits).

    Spanish postal code is a five digits string,
    with two first digits between 01 and 52, assigned to provinces code."""
    min_length = 5
    max_length = 5
    regex = r'^(0[1-9]|[1-4][0-9]|5[0-2])\d{3}$'


class GRZipCodeField(_BaseRegexField):
    """Greek ZIP Code Field (5 Digits)."""
    min_length = 5
    max_length = 5
    regex = r'^[12345678]\d{4}$'


class HROIBField(_BaseRegexField):
    """Croatia Personal Identification Number Field, AKA OIB (11 Digits)."""
    min_length = 10
    max_length = 11
    regex = r'^\d{11}$'


class ILZipCodeField(_BaseRegexField):
    """Israel ZIP Code Field."""
    min_length = 7
    max_length = 8
    regex = r'^\d{5}$|^\d{7}$'


class INZipCodeField(_BaseRegexField):
    """India ZIP Code Field (XXXXXX or XXX XXX)."""
    min_length = 6
    max_length = 7
    regex = r'^\d{3}\s?\d{3}$'


class ISIdNumberField(_BaseRegexField):
    """Iceland identification number Field, AKA Kennitala (XXXXXX-XXXX)."""
    min_length = 10
    max_length = 11
    regex = r'^\d{6}(-| )?\d{4}$'


class JPZipCodeField(_BaseRegexField):
    """Japan ZIP Code Field."""
    max_length = 8
    regex = r'^\d{3}-\d{4}$|^\d{7}$'


class MKIdentityCardNumberField(_BaseRegexField):
    """Macedonia ID card number Field (old & new)."""
    min_length = 4
    max_length = 8
    regex = r'(^[A-Z]{1}\d{7}$)|(^\d{4,7}$)'


class MTZipCodeField(_BaseRegexField):
    """Maltese ZIP Code Field (7 digits, first 3 letters, final 4 numbers)."""
    min_length = 7
    max_length = 8
    regex = r'^[A-Z]{3}\ \d{4}$'


class MXZipCodeField(_BaseRegexField):
    """Mexico ZIP Code Field (XXXXX format).

    http://en.wikipedia.org/wiki/List_of_postal_codes_in_Mexico."""
    min_length = 5
    max_length = 6
    regex = r'^(0[1-9]|[1][0-6]|[2-9]\d)(\d{3})$'


class PLNationalIDCardNumberField(_BaseRegexField):
    """Polish National ID Card Number Field (3 letter and 6 digits).

    http://en.wikipedia.org/wiki/Polish_identity_card."""
    min_length = 9
    max_length = 10
    regex = r'^[A-Za-z]{3}\d{6}$'


class PLNIPField(_BaseRegexField):
    """Polish Tax Number Field (NIP).

    The format is XXX-YYY-YY-YY, XXX-YY-YY-YYY or XXXYYYYYYY.
    http://wipos.p.lodz.pl/zylla/ut/nip-rego.html."""
    min_length = 10
    max_length = 15
    regex =  r'^\d{3}-\d{3}-\d{2}-\d{2}$|^\d{3}-\d{2}-\d{2}-\d{3}$|^\d{10}$'


class PLZipCodeField(_BaseRegexField):
    """Polish ZIP Code Field (XX-XXX format)."""
    min_length = 5
    max_length = 6
    regex =  r'^\d{2}-\d{3}$'


class PTZipCodeField(_BaseRegexField):
    """Portuguese ZIP Code Field.

    XYYY-YYY (where X is a digit between 1 and 9, Y is any other digit)."""
    min_length = 7
    max_length = 8
    regex =  r'^[1-9]\d{3}-\d{3}$'


class ROZipCodeField(_BaseRegexField):
    """Romania ZIP Code Field (XXXXXX format)."""
    min_length = 6
    max_length = 6
    regex =  r'^[0-9][0-8][0-9]{4}$'


class ROCIFField(_BaseRegexField):
    """Romania Fiscal Identity Code (CIF).

    https://ro.wikipedia.org/wiki/Cod_de_Identificare_Fiscal%C4%83."""
    min_length = 2
    max_length = 10
    regex =  r'^(RO)?[0-9]{2,10}'


class ROCNPField(_BaseRegexField):
    """Romania Personal Identity Code Field (CNP)."""
    min_length = 12
    max_length = 13
    regex =  r'^[1-9][0-9]{12}'


class RUPassportNumberField(_BaseRegexField):
    """Russian Passport Number Field (Internal or Alien).

    XXXX XXXXXX or XX XXXXXXX, where X is any digit."""
    max_length = 12
    regex =  r'^\d{4} \d{6}$|^\d{2} \d{7}$'


class SEZipCodeField(_BaseRegexField):
    """Swedish ZIP Code Field (5 digits).

    Can optionally be formatted with a space after the third digit (XXX XX)."""
    min_length = 5
    max_length = 6
    regex =  r'^[1-9]\d{2} ?\d{2}$'


class SKZipCodeField(_BaseRegexField):
    """Slovak ZIP Code Field (XXXXX or XXX XX, where X is integer)."""
    min_length = 5
    max_length = 6
    regex = r'^\d{5}$|^\d{3} \d{2}$'


class UAZipCodeField(_BaseRegexField):
    """Ukrainian ZIP Code Field (5 digits,first 2 numbers must not be '00')."""
    min_length = 5
    max_length = 5
    regex = r'^(?!00)\d{5}$'


class UYCIField(_BaseRegexField):
    """Uruguay Cedula de Identidad (X.XXX.XXX-X or XXXXXXX-X or XXXXXXXX)."""
    min_length = 8
    max_length = 12
    regex = r'(?P<num>(\d{6,7}|(\d\.)?\d{3}\.\d{3}))-?(?P<val>\d)'
