import pandera as pa
from pandera.typing import DataFrame, Series


class ProdutoSchema(pa.DataFrameSchema):
    """
    Especificação do schema para validação de DataFrames de produtos.
    """
    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=5.0, le=120.0)
    categoria: Series[str]

    class Config:
        coerce = True  # Converte os tipos automaticamente
        strict = True  # Bloqueia colunas extras