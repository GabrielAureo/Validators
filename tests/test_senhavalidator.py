import pytest
from src.transfero_validators.validators import SenhaValidator
from contextlib import nullcontext as does_not_raise

from .exceptions.custom_test_exception import CustomTestException


class TestSenha:
    @pytest.mark.parametrize(
        "value,exception,expectation",
        [
            ("sad54@!A", CustomTestException(), does_not_raise()),
            ("34Paçoca!@!", CustomTestException(), does_not_raise()),
            ("asAS47!$#", CustomTestException(), does_not_raise())
        ],
    )
    def test_senha_ok(self, value, exception, expectation):
        with expectation:
            SenhaValidator.valida(value=value, exception=exception)

    @pytest.mark.parametrize(
        "value,exception,expectation",
        [
            ("123456", CustomTestException(),  pytest.raises(CustomTestException)),
            ("senha", CustomTestException(),  pytest.raises(CustomTestException)),
            ("abcdeq12", CustomTestException(),
             pytest.raises(CustomTestException)),
            ("ajdsa!aASD", CustomTestException(),
             pytest.raises(CustomTestException)),
            ("minhasenha", CustomTestException(),
             pytest.raises(CustomTestException)),
        ],
    )
    def test_senha_invalid(self, value, exception, expectation):
        with expectation:
            SenhaValidator.valida(value=value, exception=exception)
