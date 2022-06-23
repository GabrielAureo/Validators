import pytest
from src.transfero_validators.validators import CPFValidator
from contextlib import nullcontext as does_not_raise

from .exceptions.custom_test_exception import CustomTestException

class TestCPF:
    @pytest.mark.parametrize(
    "value,exception,expectation",
        [
            ("95640975091", CustomTestException(), does_not_raise()),
            ("69133081085", CustomTestException(), does_not_raise()),
            ("00891536000", CustomTestException(), does_not_raise()),
            ("245.248.520-93", CustomTestException(), does_not_raise()),
        ],
    )
    def test_cpf_valid(self,value,exception,expectation):
        with expectation:
            CPFValidator.valida(value=value, exception=exception)
        
    @pytest.mark.parametrize(
        "value,exception,expectation",
        [
            ("11111111111", CustomTestException(), pytest.raises(CustomTestException)),
            ("", CustomTestException(), pytest.raises(CustomTestException)),
            ("99999999999", CustomTestException(), pytest.raises(CustomTestException)),
            ("246.248.520-93", CustomTestException(), pytest.raises(CustomTestException)),
            ("palavra", CustomTestException(), pytest.raises(CustomTestException)),
            ("48587864598645796564", CustomTestException(), pytest.raises(CustomTestException)),
            ("4564", CustomTestException(), pytest.raises(CustomTestException)),
        ],
    )
    def test_cpf_invalid(self,value,exception,expectation):
        with expectation:
            CPFValidator.valida(value=value,exception=exception)
        
        