import pytest
from src.transfero_validators.validators import EmailValidator
from .exceptions.custom_test_exception import CustomTestException
from contextlib import nullcontext as does_not_raise


class TestEmail:
    @pytest.mark.parametrize(
        "value,exception,expectation",
        [
            ("test@test.com", CustomTestException(), does_not_raise()),
            ("est@aaa.br", CustomTestException(), does_not_raise()),
            ("test@transfero.academy.com",
             CustomTestException(), does_not_raise()),
            ("usuario@gmail.com", CustomTestException(), does_not_raise()),
        ],
    )
    def test_ok_email(self, value, exception, expectation):
        with expectation:
            EmailValidator.valida(value=value, exception=exception)

    @pytest.mark.parametrize(
        "value,exception,expectation",
        [
            ("", CustomTestException(), pytest.raises(CustomTestException)),
            ("test.com", CustomTestException(), pytest.raises(CustomTestException)),
            ("test@email.com@",
             CustomTestException(), pytest.raises(CustomTestException)),
            ("test", CustomTestException(), pytest.raises(CustomTestException)),
        ],
    )
    def test_invalid_email(self, value, exception, expectation):
        with expectation:
            EmailValidator.valida(value=value, exception=exception)
