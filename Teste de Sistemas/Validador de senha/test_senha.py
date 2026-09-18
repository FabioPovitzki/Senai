from senha import validar_senha

import pytest

def validar_senha(senha):
    if len(senha) >= 8:
        return True
    return False

@pytest.mark.parametrize(
    "senha, resultado_esperado",
    [
        ("12345678", True),     # Exatamente 8 caracteres (Fronteira válida)
        ("123456789", True),    # Mais de 8 caracteres (Válida)
        ("senhaforte", True),   # Palavra longa (Válida)
        ("1234567", False),     # 7 caracteres (Fronteira inválida - abaixo do limite)
        ("abc", False),         # Senha muito curta (Inválida)
        ("", False),            # Senha vazia (Inválida)
    ]
)
def test_validar_senha(senha, resultado_esperado):
    assert validar_senha(senha) == resultado_esperado