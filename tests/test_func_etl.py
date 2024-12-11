import pandas as pd
from app.etl import transformar

def test_calculo_valor_total_estoque():
    # Dados de entrada
    dados_entrada = pd.DataFrame({
        'quantidade': [10, 5, 0],
        'preco': [2.0, 3.5, 1.0],
        'categoria': ['A', 'B', 'C']
    })
    # Resultado esperado
    resultado_esperado = pd.DataFrame({
        'quantidade': [10, 5, 0],
        'preco': [2.0, 3.5, 1.0],
        'categoria': ['A', 'B', 'C'],
        'valor_total_estoque': [20.0, 17.5, 0.0],
        'categoria_normalizada': ['a', 'b', 'c'],
        'disponibilidade': [True, True, False]
    })

    # Chamar a função
    resultado = transformar(dados_entrada)
    
    # Verificar se o DataFrame gerado é igual ao esperado
    pd.testing.assert_frame_equal(resultado, resultado_esperado)

def test_normalizacao_categoria():
    # Dados de entrada
    dados_entrada = pd.DataFrame({
        'quantidade': [1, 2, 3],
        'preco': [10.0, 20.0, 30.0],
        'categoria': ['Eletronicos', 'MÓVEIS', 'alimentos']
    })
    # Categorias esperadas normalizadas
    categorias_esperadas = ['eletronicos', 'móveis', 'alimentos']

    # Chamar a função
    resultado = transformar(dados_entrada)

    # Verificar se as categorias foram normalizadas corretamente
    assert list(resultado['categoria_normalizada']) == categorias_esperadas

def test_determinacao_disponibilidade():
    # Dados de entrada
    dados_entrada = pd.DataFrame({
        'quantidade': [0, 10, -5],
        'preco': [1.0, 2.0, 3.0],
        'categoria': ['X', 'Y', 'Z']
    })
    # Disponibilidade esperada
    disponibilidade_esperada = [False, True, False]

    # Chamar a função
    resultado = transformar(dados_entrada)

    # Verificar se a disponibilidade corresponde ao esperado
    assert list(resultado['disponibilidade']) == disponibilidade_esperada