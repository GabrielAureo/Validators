from abc import ABC, abstractmethod
from typing import Generic, TypeVar
import re


T = TypeVar("T")
class AbstractValidator(ABC, Generic[T]):
    @abstractmethod
    def valida(value : T) -> bool:
        pass

class EmailValidator(AbstractValidator[str]):
    def valida(value: str) -> bool:
        return bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value))

class CPFValidator(AbstractValidator[str]):
    def valida(value: str) -> bool:

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

class CelularValidator(AbstractValidator[str]):
    def valida(value: str) -> bool:
        return bool(re.match('^[1-9]{2}9[1-9][0-9]{3}[0-9]{4}$', value))

class SenhaValidator(AbstractValidator[str]):
    def valida(value : str) -> bool:
        special_sym = ['$', '@', '#', '%']

        if (len(value) < 6 or len(value) > 20)\
        or not any(char.isdigit() for char in value)\
        or not any(char.isupper() for char in value)\
        or not any(char.islower() for char in value)\
        or not any(char in special_sym for char in value):
            return False
        
        return True


