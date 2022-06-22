from transfero_validators.validators import CPFValidator

class TestCPF:
    def test_cpf_valid(self):
        assert CPFValidator.valida("95640975091")
        assert CPFValidator.valida("69133081085")
        assert CPFValidator.valida("00891536000")
        assert CPFValidator.valida("245.248.520-93")
        
    
    def test_cpf_invalid(self):
        assert not CPFValidator.valida("11111111111")
        assert not CPFValidator.valida("")
        assert not CPFValidator.valida("99999999999")
        assert not CPFValidator.valida("4564")
        
        