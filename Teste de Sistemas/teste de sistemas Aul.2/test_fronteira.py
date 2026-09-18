from fronteira import classificar_idade
import pytest

# def test_menor_idade_maior():
#     assert classificar_idade(17) == "Menor de idade"
# def test_maior_de_idade():
#     assert classificar_idade(18) == "Maior de idade"
# def test_idade_18():
#     assert classificar_idade (10) == "Menor de idade"

@pytest.mark.parametrize(
    "idade, resultado_esperado",
    [
        (10, "Menor de idade"),
        (12, "Menor de idade"),
        (13, "Menor de idade"),
        (15, "Menor de idade"),
        (17, "Menor de idade"),
        (9, "Menor de idade"),
    ]
)

def test_classivar_idade (idade , resultado_esperado):
    resultado = classificar_idade(idade)
    assert resultado == resultado_esperado