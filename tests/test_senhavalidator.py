from transfero_validators.validators import SenhaValidator

class TestSenha:
    def test_senha_ok(self):
        assert SenhaValidator.valida("sad54@!A")
        assert SenhaValidator.valida("34Paçoca!@!")
        assert SenhaValidator.valida("asAS47!$#")
    
    def test_senha_invalid(self):
        assert not SenhaValidator.valida("123456")
        assert not SenhaValidator.valida("senha")
        assert not SenhaValidator.valida("abcdeq12")
        assert not SenhaValidator.valida("ajdsa!aASD")
        assert not SenhaValidator.valida("minhasenha")