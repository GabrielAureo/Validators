from src.transfero_validators.validators import CelularValidator

class TestCelular:
    def test_celular_ok(self):
        assert CelularValidator.valida("21964512232")
        assert CelularValidator.valida("42929292929")
        assert CelularValidator.valida("11999111999")
        assert CelularValidator.valida("22912345678")

    def test_celular_invalido(self):
        assert not CelularValidator.valida("964512232")
        assert not CelularValidator.valida("21778787878")
        assert not CelularValidator.valida("12489")
        assert not CelularValidator.valida("0000000000")
        assert not CelularValidator.valida("")
        assert not CelularValidator.valida("21904512232")

