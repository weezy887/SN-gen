# Projekt: Seriennummergenerator \ Modul: Serialnumbergenerator
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""Serialnumbergenerator module"""

from io import UnsupportedOperation
from random import randrange
from string import ascii_letters, digits
from encodings import utf_8
import json


class SerialnumberGenerator():
    """Base glass for serialnumbergenerators."""

    def __init__(self, sn_type: str) -> None:
        self.keys = {}
        self.path_to_save = ''
        self.type = sn_type

    def generate_serialnumber(self) -> None:
        """Generates a Serialnumber based on type.
        Takes quantity, rows and row_length as Argmuments"""

        def generate_letter() -> str:
            """returns a random letter."""
            rnd_nmb = randrange(len(ascii_letters) - 1)
            return ascii_letters[rnd_nmb]

        def generate_digit() -> str:
            """returns a random digit."""
            rnd_nmb = randrange((len(digits)) - 1)
            return digits[rnd_nmb]

        def generate_string(sn_type: str, count: int, rows: int, row_length: int, tmp_list: list) -> list:
            """
            Generates Serialnumbers based on type.
            Returns created serialnumbers as list.
            """
            key = ''
            for i in range(rows * row_length):
                key += generate_letter() if sn_type == 'letter' else generate_digit()

            tmp_list.append(key)
            if count <= 1:
                return tmp_list
            else:
                return generate_string(sn_type, (count - 1), rows, row_length, tmp_list)

        # user input
        key_count = int(input("quantity: "))
        key_rows = int(input("rows: "))
        row_length = int(input("rowlength: "))

        tmp_list = []
        end_list = generate_string(
            self.type, key_count, key_rows, row_length, tmp_list)
        for key in end_list:
            self.keys[key] = True

    def validate_serialnumber(self) -> None:
        """Takes a SN as an argument and checks if it is valid."""
        validate_serialnumber = input("serialnumber to validate: ")
        with open('keys.json', 'r', encoding=utf_8) as file:
            data = json.load(file)
            try:
                if data[validate_serialnumber]:
                    print("key is valid!")
                else:
                    print("key is not valid")
            except KeyError:
                print("key not found!")

    def save_serialnumber(self) -> None:
        """writes existing keys to a json file."""
        with open('keys.json', 'a', encoding="utf-8") as file:
            try:
                data = json.load(file)
                new_data = dict(data.items() + self.keys.items())
                json.dump(new_data, file, indent=4)
            except UnsupportedOperation:
                json.dump(self.keys, file, indent=4)