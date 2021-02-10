#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Peewee Extra Fields Unittests."""


import os
import shutil
import unittest
from decimal import Decimal
from ipaddress import (IPv4Address, IPv4Network, IPv6Address, IPv6Network,
                       ip_address, ip_network)
from random import randint, choice
from datetime import date, datetime

from peewee import *

from peewee_extra_fields import *


# Random order for tests runs. (Original is: -1 if x<y, 0 if x==y, 1 if x>y).
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: randint(-1, 1)

db = PostgresqlDatabase('travis_ci_test', field_types=FIELD_TYPES)
db.connect()


class TestFields(unittest.TestCase):

    """Peewee Extra Fields Unittests."""

    maxDiff, __slots__ = None, ()

    def test_PositiveIntegerField(self):
        valid_values = (0, 1, 2, 3, 9, 100, 1_000, 2_147_483_647)
        invalid_values = (-1, -2, -3, -9, -100, -1_000, -100_000, -100_000)

        for value in valid_values:
            self.assertEqual(PositiveIntegerField().python_value(value), value)
            self.assertEqual(PositiveIntegerField().db_value(value), value)
            self.assertIsInstance(PositiveIntegerField().python_value(value), int)
            self.assertIsInstance(PositiveIntegerField().db_value(value), int)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                PositiveIntegerField().db_value(value)

    def test_PositiveSmallIntegerField(self):
        valid_values = (0, 1, 2, 3, 9, 100, 1_000, 32_767)
        invalid_values = (-1, -2, -3, -9, -100, -1_000, -100_000, -100_000)

        for value in valid_values:
            self.assertEqual(PositiveSmallIntegerField().python_value(value), value)
            self.assertEqual(PositiveSmallIntegerField().db_value(value), value)
            self.assertIsInstance(PositiveSmallIntegerField().python_value(value), int)
            self.assertIsInstance(PositiveSmallIntegerField().db_value(value), int)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                PositiveSmallIntegerField().db_value(value)

    def test_PositiveBigIntegerField(self):
        valid_values = (0, 1, 2, 3, 9, 100, 1_000, 9_223_372_036_854_775_807)
        invalid_values = (-1, -2, -3, -9, -100, -1_000, -100_000, -100_000)

        for value in valid_values:
            self.assertEqual(PositiveBigIntegerField().python_value(value), value)
            self.assertEqual(PositiveBigIntegerField().db_value(value), value)
            self.assertIsInstance(PositiveBigIntegerField().python_value(value), int)
            self.assertIsInstance(PositiveBigIntegerField().db_value(value), int)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                PositiveBigIntegerField().db_value(value)

    def test_PositiveFloatField(self):
        valid_values = (0.0, 1.0, 2.0, 3.0, 9.123456789, 100.55, 1_000.9999)
        invalid_values = (-1.0, -2.0, -3.0, -9.99, -100.123456789, -1_000.0)

        for value in valid_values:
            self.assertEqual(PositiveFloatField().python_value(value), value)
            self.assertEqual(PositiveFloatField().db_value(value), value)
            self.assertIsInstance(PositiveFloatField().python_value(value), float)
            self.assertIsInstance(PositiveFloatField().db_value(value), float)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                PositiveFloatField().db_value(value)

    def test_PositiveFloatField_round(self):
        valid_values = (0.0, 1.9999, 2.123456789, 3.999, 9.123456789, 100.0909)
        invalid_values = (-1.0, -2.001, -3.01, -9.99, -100.123456789, -1_000.0)

        for value in valid_values:
            round_by = randint(1, 10)
            # print(f"Positive Float   (Rounding by {round_by}): {value}.")
            value_rounded = round(value, round_by)
            self.assertEqual(PositiveFloatField(round_by=round_by).python_value(value_rounded), value_rounded)
            self.assertEqual(PositiveFloatField(round_by=round_by).db_value(value), value_rounded, f"Rounding Positive Floats by {round_by}.")
            self.assertIsInstance(PositiveFloatField(round_by=round_by).python_value(value), float)
            self.assertIsInstance(PositiveFloatField(round_by=round_by).db_value(value), float)

        for value in invalid_values:
            round_by = randint(1, 10)
            with self.assertRaises(ValueError):
                PositiveFloatField(round_by=round_by).db_value(value)

    def test_PositiveDecimalField(self):
        valid_values = (0.0, 1.0, 2.0, 3.0, 9.123456789, 100.55, 1_000.9999)
        invalid_values = (-1.0, -2.0, -3.0, -9.99, -100.123456789, -1_000.0)

        for value in valid_values:
            value = Decimal(str(value))
            self.assertEqual(PositiveDecimalField().python_value(value), value)
            self.assertEqual(PositiveDecimalField().db_value(value), value)
            self.assertIsInstance(PositiveDecimalField().python_value(value), Decimal)
            self.assertIsInstance(PositiveDecimalField().db_value(value), Decimal)

        for value in invalid_values:
            value = Decimal(str(value))
            with self.assertRaises(ValueError):
                PositiveDecimalField().db_value(value)

    def test_PositiveDecimalField_round(self):
        valid_values = (0.0, 1.0, 2.0, 3.0, 9.123456789, 100.55, 1_000.9999)
        invalid_values = (-1.0, -2.0, -3.0, -9.99, -100.123456789, -1_000.0)

        for value in valid_values:
            round_by = randint(1, 10)
            # print(f"Positive Decimal (Rounding by {round_by}): {value}.")
            value_rounded = Decimal(str(value)).quantize(
                Decimal(10) ** -round_by).normalize()
            value = Decimal(str(value))
            self.assertEqual(PositiveDecimalField(round_by=round_by).python_value(value_rounded), value_rounded)
            self.assertEqual(PositiveDecimalField(round_by=round_by).db_value(value), value_rounded)
            self.assertIsInstance(PositiveDecimalField(round_by=round_by).python_value(value), Decimal)
            self.assertIsInstance(PositiveDecimalField(round_by=round_by).db_value(value), Decimal)

        for value in invalid_values:
            round_by = randint(1, 10)
            with self.assertRaises(ValueError):
                PositiveFloatField(round_by=round_by).db_value(value)

    def test_IPAddressField(self):
        valid_values = ("127.0.0.1", "::1", "192.168.0.1", "8.8.8.8")
        invalid_values = ("1", ":1", "10.0.0", "-8.8.8.8", "256.0.0.1")

        for value in valid_values:
            ip_addr = ip_address(value)
            self.assertEqual(IPAddressField().python_value(value), ip_addr)
            self.assertIsInstance(IPAddressField().python_value(value), (IPv4Address, IPv6Address))
            self.assertIsInstance(IPAddressField().db_value(value), int)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                IPAddressField().db_value(value)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                IPAddressField().python_value(value)

    def test_IPNetworkField(self):
        valid_values = ("127.0.0.1/32", "192.0.0.0/10", "8.8.8.0/32")
        invalid_values = ("1/128", ":1/256", "10.0.0/32", "-8.8.8.8/128")

        for value in valid_values:
            ip_net = ip_network(value)
            self.assertEqual(IPNetworkField().python_value(value), ip_net)
            self.assertEqual(IPNetworkField().db_value(value), value)
            self.assertIsInstance(IPNetworkField().python_value(value), (IPv4Network, IPv6Network))
            self.assertIsInstance(IPNetworkField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                IPNetworkField().db_value(value)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                IPNetworkField().python_value(value)

    def test_CharFieldCustom_min_lenght(self):

        for min_lenght in range(1, 100):
            self.assertMultiLineEqual(
                CharFieldCustom(min_lenght=min_lenght).db_value("a" * min_lenght),
                "a" * min_lenght)
            self.assertIsInstance(CharFieldCustom(min_lenght=min_lenght).python_value("a" * min_lenght), str)
            self.assertIsInstance(CharFieldCustom(min_lenght=min_lenght).db_value("a" * min_lenght), str)

        for min_lenght in range(2, 10):
            with self.assertRaises(ValueError):
                CharFieldCustom(min_lenght=min_lenght).db_value("a" * randint(1, min_lenght - 1))

    def test_CharFieldCustom_use_lower(self):
        for min_lenght in range(1, 100):
            self.assertMultiLineEqual(
                CharFieldCustom(use_lower=True).db_value("A" * min_lenght),
                "a" * min_lenght)
            self.assertIsInstance(CharFieldCustom(use_lower=True).python_value("A" * min_lenght), str)
            self.assertIsInstance(CharFieldCustom(use_lower=True).db_value("A" * min_lenght), str)

    def test_CharFieldCustom_force_ascii(self):
        invalid_values = ("a😼", "foo😝", "😺bar", "😎baz🐵")
        valid_values = ("a", "foo", "bar", "baz")         # Replaces by "".
        valid_values_2 = ("a?", "foo?", "?bar", "?baz?")  # Replaces by "?".

        for unicode_value, ascii_value in zip(invalid_values, valid_values):
            self.assertEqual(CharFieldCustom(force_ascii="").db_value(unicode_value), ascii_value)

        for unicode_value, ascii_value in zip(invalid_values, valid_values_2):
            self.assertEqual(CharFieldCustom(force_ascii="?").db_value(unicode_value), ascii_value)

    def test_CharFieldCustom_blacklist(self):
        invalid_values = ("nazi", "shit", "poo", "cunt")

        for bad_word in invalid_values:
            with self.assertRaises(ValueError):
                CharFieldCustom(blacklist=invalid_values).db_value(bad_word)

    def test_CharFieldCustom_whitelist(self):
        valid_values = ("cool", "python", "peewee", "linux", "postgresql")

        for _ in valid_values:
            with self.assertRaises(ValueError):
                CharFieldCustom(whitelist=valid_values).db_value("foo bar baz")

        for _ in valid_values:
            CharFieldCustom(whitelist=valid_values).db_value(choice(valid_values))

    def test_CharFieldCustom_force_slugify(self):
        invalid_values = ("cool python", "peewee orm", "linux os", "postgre sql")
        valid_values = ("cool-python", "peewee-orm", "linux-os", "postgre-sql")

        for raw_value, slug_value in zip(invalid_values, valid_values):
            self.assertEqual(CharFieldCustom(force_slugify=True).db_value(raw_value), slug_value)

    def test_PastDateField(self):
        for i in range(9):
            value = date(year=randint(1800, date.today().year),
                         month=randint(1, 12),
                         day=randint(1, 28))
            self.assertEqual(PastDateField().python_value(value), value)
            self.assertEqual(PastDateField().db_value(value), value)
            self.assertIsInstance(PastDateField().python_value(value), date)
            self.assertIsInstance(PastDateField().db_value(value), date)

        for i in range(9):
            value = date(year=randint(date.today().year + 1, date.today().year + 100),
                         month=randint(1, 12),
                         day=randint(1, 28))
            with self.assertRaises(ValueError):
                PastDateField().db_value(value)

    def test_PastDateTimeField(self):
        for i in range(9):
            value = datetime(year=randint(1800, date.today().year),
                             month=randint(1, 12),
                             day=randint(1, 28),
                             hour=randint(0, 23),
                             minute=randint(0, 59),
                             second=randint(0, 59))
            self.assertEqual(PastDateTimeField().python_value(value), value)
            self.assertEqual(PastDateTimeField().db_value(value), value)
            self.assertIsInstance(PastDateTimeField().python_value(value), datetime)
            self.assertIsInstance(PastDateTimeField().db_value(value), datetime)

        for i in range(9):
            value = datetime(year=randint(date.today().year + 1, date.today().year + 100),
                             month=randint(1, 12),
                             day=randint(1, 28),
                             hour=randint(0, 23),
                             minute=randint(0, 59),
                             second=randint(0, 59))
            with self.assertRaises(ValueError):
                print(value)
                PastDateTimeField().db_value(value)

    def test_LanguageISOCodeField(self):
        valid_values = ("en", "es", "ru", "zu", "pi", "is", "de", "tt", "br")
        invalid_values = ("xx", "bb", "zz", "uu", "px", "42", "cx", "uc", "yyy")

        for value in valid_values:
            self.assertEqual(LanguageISOCodeField().db_value(value), value)
            self.assertIsInstance(LanguageISOCodeField().python_value(value), tuple)  # LanguageISO639(code='es', name='Spanish')
            self.assertIsInstance(LanguageISOCodeField().db_value(value), str)        # "es"
            print(LanguageISOCodeField().python_value(value))

        for value in invalid_values:
            with self.assertRaises(ValueError):
                LanguageISOCodeField().db_value(value)

    def test_CountryISOCodeField(self):
        valid_values = ("ar", "nz", "bo", "pe", "cf", "py", "pe", "ru", "zw")
        invalid_values = ("xx", "1024", "666", "uu", "px", "42", "ox", "yyy")

        for value in valid_values:
            self.assertIsInstance(CountryISOCodeField().db_value(value), int)        # 32


        for value in invalid_values:
            with self.assertRaises(ValueError):
                CountryISOCodeField().db_value(value)

        print(CountryISOCodeField().python_value(32))

    def test_CurrencyISOCodeField(self):
        valid_values = ("usd", "ars", "xau", "xag", "rub", "mxn", "brl")
        invalid_values = ("yomom", "1024", "666", "uu", "42", "ox", "yyy")

        for value in valid_values:
            self.assertIsInstance(CurrencyISOCodeField().db_value(value), int)        # "ars"

        for value in invalid_values:
            with self.assertRaises(ValueError):
                CurrencyISOCodeField().db_value(value)

    def test_ARZipCodeField(self):
        valid_values = ("2804", "1024", "6666", "3421", "4232", "3231", "1215")
        invalid_values = ("yo", " ", "666", "uu", "42", "ox", "yyy")

        for value in valid_values:
            self.assertIsInstance(ARZipCodeField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                ARZipCodeField().db_value(value)

    def test_ARCUITField(self):
        valid_values = ("20-30999666-6", "20309996666", "20-10101010-5")
        invalid_values = ("yo", " ", "666", "uu", "42", "ox", "yyy")

        for value in valid_values:
            self.assertIsInstance(ARCUITField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                ARCUITField().db_value(value)

    def test_SWIFTISOCodeField(self):
        valid_values = ("DEUTDEFF", "NEDSZAJJ", "DABADKKK", "UNCRITMM")
        invalid_values = ("", "1", "abcdefg")

        for value in valid_values:
            self.assertEqual(SWIFTISOCodeField().python_value(value).swift, value)
            self.assertEqual(SWIFTISOCodeField().db_value(value), value)
            self.assertIsInstance(SWIFTISOCodeField().python_value(value), tuple)
            self.assertIsInstance(SWIFTISOCodeField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                SWIFTISOCodeField().db_value(value)

    def test_IBANISOCodeField(self):
        valid_values = ("DE44 5001 0517 5407 3249 31",
                        "GR16 0110 1250 0000 0001 2300 695",
                        "GB29 NWBK 6016 1331 9268 19",
                        "SA03 8000 0000 6080 1016 7519",
                        "CH93 0076 2011 6238 5295 7",
                        "GB82 WEST 1234 5698 7654 32")
        invalid_values = ("", "1", "abcdefg",
                          "DEzz 5001 0517 5407 3249 31",
                          "DE00 5001 0517 5407 3249 31",
                          "xx44 5001 0517 5407 3249 31")

        for value in valid_values:
            self.assertEqual(IBANISOCodeField().python_value(value).iban_pretty, value)
            self.assertEqual(IBANISOCodeField().db_value(value),
                             value.strip().replace(' ', '').replace('-', '').upper())
            self.assertIsInstance(IBANISOCodeField().python_value(value), tuple)
            self.assertIsInstance(IBANISOCodeField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                IBANISOCodeField().db_value(value)

    def test_IANCodeField(self):  # TODO Add more testing Values.
        valid_values = ("5901234123457", "4012345123456")  # From Wikipedia.
        invalid_values = ("", "1234567896765756756", "1234567890")

        for value in valid_values:
            self.assertEqual(IANCodeField().python_value(value), value)
            self.assertEqual(IANCodeField().db_value(value), value)
            self.assertIsInstance(IANCodeField().python_value(value), str)
            self.assertIsInstance(IANCodeField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                IANCodeField().db_value(value)

    def test_USZipCodeField(self):  # TODO Add more testing Values.
        valid_values = ("20521-9000", "99750-0077", "12201-7050")
        invalid_values = ("", "1", "20521-90000")

        for value in valid_values:
            self.assertEqual(USZipCodeField().python_value(value), value)
            self.assertEqual(USZipCodeField().db_value(value), value)
            self.assertIsInstance(USZipCodeField().python_value(value), str)
            self.assertIsInstance(USZipCodeField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                USZipCodeField().db_value(value)

    def test_USSocialSecurityNumberField(self):  # TODO Add more testing Values
        valid_values = ("205-21-9000", "205-21-9000", "205-21-9000", "205-50-3434")
        invalid_values = ("", "1", "abc", "205-21-900", "05-21-9000", "205-2-9000")

        for value in valid_values:
            self.assertEqual(USSocialSecurityNumberField().python_value(value).ssn, value)
            self.assertEqual(USSocialSecurityNumberField().db_value(value), value)
            self.assertIsInstance(USSocialSecurityNumberField().python_value(value), tuple)
            self.assertIsInstance(USSocialSecurityNumberField().db_value(value), str)

        for value in invalid_values:
            with self.assertRaises(ValueError):
                USSocialSecurityNumberField().db_value(value)

    def test_ColorHexadecimalField(self):
        valid_values = ("#bebebe", "#f0f0f0", "#000000", "#ffffff")
        invalid_values = ("", "1", "abc", "#0000gg", "#00h", "#-1f0f0")

        for value in valid_values:
            self.assertIsInstance(ColorHexadecimalField().python_value(value), tuple)
            self.assertIsInstance(ColorHexadecimalField().db_value(value), str)
            print(ColorHexadecimalField().python_value(value))

        for value in invalid_values:
            with self.assertRaises(ValueError):
                ColorHexadecimalField().db_value(value)

    def test_SemVerField(self):
        valid_values = (
            '0.0.0', '0.10.0', 'v1.0.0', '0.0.0-foo', '1.2.3-4', '2.7.2+asdf',
            '1.2.3-a.b.c.10.d.5', '2.7.2-foo+bar', '1.2.3-alpha.10.beta.0',
            '1.2.3-alpha.10.beta.0+build.unicorn.rainbow', '0.0.1', '99.0.0',
        )
        invalid_values = ("", "1", "abc", "0a", "#0", "-1f0", "cat", "42", "%")

        for value in valid_values:
            self.assertEqual(SemVerField().python_value(value), value)
            self.assertEqual(SemVerField().db_value(value), value)
            self.assertIsInstance(SemVerField().python_value(value), str)
            self.assertIsInstance(SemVerField().db_value(value), str)
            print(SemVerField().python_value(value))

        for value in invalid_values:
            with self.assertRaises(ValueError):
                SemVerField().db_value(value)

    def test_MoneyField(self):
        class Salary(Model):
            dollars = MoneyField()
            class Meta:
                database = db

        db.create_tables([Salary])
        invoice = Salary.create(dollars=1_024.75)
        invoice.save()
        salary = Salary.select()[0]
        self.assertEqual(salary.dollars, '$1,024.75')
        self.assertIsInstance(salary.dollars, str)
        invoice.delete_instance()

    def test_XMLField(self):
        class SVGImage(Model):
            data = XMLField()
            class Meta:
                database = db

        db.create_tables([SVGImage])
        vector_img = SVGImage.create(data="<svg><text>foo</text></svg>")
        vector_img.save()
        svg_img = SVGImage.select()[0]
        self.assertEqual(svg_img.data, "<svg><text>foo</text></svg>")
        self.assertIsInstance(svg_img.data, str)
        vector_img.delete_instance()

    def test_File_write_path_file(self):
        folder_for_files = "unit_test\\"

        class File(Model):
            data = FileField(folder_for_files=folder_for_files)
            class Meta:
                database = db

        db.create_tables([File])
        file = File.create(data="setup.py")
        file = File.get(id=file.id)
        self.assertIsInstance(file.data.bytecode, bytes)
        self.assertEqual(file.data.file_path, os.path.join(folder_for_files, "setup.py"))
        shutil.rmtree(folder_for_files)
        file.delete_instance()

    def test_text_fields_with_validators(self):
        class TestTextField(Model):
            text_with_string = TextField(validators=["test", "test1"])
            text_with_callable = TextField(validators=[self._is_exact_number])

            class Meta:
                database = db

        db.create_tables([TestTextField])

        record = TestTextField.create(text_with_string="test", text_with_callable=4)


        for field_name, value in [["text_with_string", "test_"], ["text_with_callable", 5]]:
            self._check_validate_field(record, field_name, value)

        record.delete_instance()

    @staticmethod
    def _check_validate_field(record, field_name, value):
        try:
            setattr(record, field_name, value)
            record.save()
            result = "Not exceptions"
        except exceptions.ValidationError:  # Attempt to fail
            result = "exceptions"

        assert "exceptions" == result

    @staticmethod
    def _is_exact_number(value):
        return 0 == value % 2



if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
