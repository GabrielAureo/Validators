from abc import ABC, abstractmethod
from typing import Generic, TypeVar
import re


T = TypeVar("T")
class Validator(ABC, Generic[T]):
    @abstractmethod
    def valida(value : T) -> bool:
        pass

class EmailValidator(Validator[str]):
    def valida(value: str) -> bool:
        return bool(re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', value))

class CPFValidator(Validator[str]):
    def valida(value: str) -> bool:
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', value):
            return False

        numbers = [int(digit) for digit in value if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

class CelularValidator(Validator[str]):
    def valida(value: str) -> bool:
        return bool(re.match('^[1-9]{2}9[1-9][0-9]{3}[0-9]{4}$', value))

class SenhaValidator(Validator[str]):
    def valida(value : str) -> bool:
        special_sym = ['$', '@', '#', '%']


        if (len(value) < 6 or len(value) > 20)\
        and not any(char.isdigit() for char in value)\
        and not any(char.isupper() for char in value)\
        and not any(char.islower() for char in value)\
        and not any(char in special_sym for char in value):
            return False


