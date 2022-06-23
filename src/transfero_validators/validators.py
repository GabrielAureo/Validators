from abc import ABC, abstractmethod
from typing import Generic, TypeVar
import re


T = TypeVar("T")
class AbstractValidator(ABC, Generic[T]):
    @abstractmethod
    def valida(value : T, exception : Exception = None) -> bool:
        pass

class StringVaziaValidator(AbstractValidator[str]):
    def valida(value: T, exception: Exception = None) -> bool:
        if(value == ""):
            raise exception

class EmailValidator(AbstractValidator[str]):
    def valida(value: str, exception: Exception = None) -> bool:
        StringVaziaValidator.valida(value, exception=exception)
        if bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value)):
            raise exception

class CPFValidator(AbstractValidator[str]):
    def valida(value: str, exception: Exception = None) -> bool:
        StringVaziaValidator.valida(value, exception=exception)
        numeros = [int(digit) for digit in value if digit.isdigit()]

        if len(numeros) != 11:
            raise exception

        if len(set(numeros)) == 1:
            raise exception

        # Validação do primeiro dígito verificador:
        soma_dos_produtos = sum(a*b for a, b in zip(numeros[0:9], range(10, 1, -1)))
        digito_esperado = (soma_dos_produtos * 10 % 11) % 10
        if numeros[9] != digito_esperado:
            raise exception

        # Validação do segundo dígito verificador:
        soma_dos_produtos = sum(a*b for a, b in zip(numeros[0:10], range(11, 1, -1)))
        digito_esperado = (soma_dos_produtos * 10 % 11) % 10
        if numeros[10] != digito_esperado:
            raise exception

class CelularValidator(AbstractValidator[str]):
    def valida(value: str, exception: Exception = None):
        StringVaziaValidator.valida(value, exception=exception)
        if bool(re.match('^[1-9]{2}9[1-9][0-9]{3}[0-9]{4}$', value)):
            raise exception

class SenhaValidator(AbstractValidator[str]):
    def valida(value : str, exception: Exception = None):
        StringVaziaValidator.valida(value, exception=exception)
        special_sym = ['$', '@', '#', '%']

        if (len(value) < 6 or len(value) > 20)\
        or not any(char.isdigit() for char in value)\
        or not any(char.isupper() for char in value)\
        or not any(char.islower() for char in value)\
        or not any(char in special_sym for char in value):
            raise exception


