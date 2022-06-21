from src.validators import EmailValidator


class TestEmail:
    def test_ok_email(self):
        assert EmailValidator.valida("test@test.com")
        assert EmailValidator.valida("test@aaa.br")
        assert EmailValidator.valida("test.p@transfero.com")
        
    def test_invalid_email(self):
        assert not EmailValidator.valida("test@gmail.com@")
        assert not EmailValidator.valida("as")
        assert not EmailValidator.valida("test.com")