from contextlib import nullcontext as does_not_raise
import pytest
from src.transfero_validators.validators import CelularValidator
from .exceptions.custom_test_exception import CustomTestException

class TestCelular:
    @pytest.mark.parametrize(
    "value,exception,expectation",
        [
            ("21964512232", CustomTestException(), does_not_raise()),
            ("42929292929", CustomTestException(), does_not_raise()),
            ("11999111999", CustomTestException(), does_not_raise()),
            ("22912345678", CustomTestException(), does_not_raise()),
        ],
    )
    def test_celular_ok(self, value, exception, expectation):
        with expectation:
            CelularValidator.valida(value=value, exception=exception)

    @pytest.mark.parametrize(
    "value,exception,expectation",
        [
            ("964512232", CustomTestException(), pytest.raises(CustomTestException)),
            ("21778787878", CustomTestException(), pytest.raises(CustomTestException)),
            ("12489", CustomTestException(), pytest.raises(CustomTestException)),
            ("0000000000", CustomTestException(), pytest.raises(CustomTestException)),
            ("", CustomTestException(), pytest.raises(CustomTestException)),
            ("21904512232", CustomTestException(), pytest.raises(CustomTestException))
        ],
    )
    def test_celular_invalido(self, value, exception, expectation):
        with expectation:
            CelularValidator.valida(value=value, exception=exception)

