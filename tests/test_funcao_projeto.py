from app.funcao import funcao_projeto

def test_funcao_projeto_01():
    saida = funcao_projeto()
    gabarito = "projeto_01"
    assert saida == gabarito