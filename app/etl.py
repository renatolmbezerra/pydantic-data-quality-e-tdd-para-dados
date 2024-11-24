import os
from pathlib import Path

import pandas as pd
import pandera as pa
from dotenv import load_dotenv
from sqlalchemy import create_engine

from schema import ProdutoSchema, ProductSchemaKPI

def load_settings():
    """Carrega as configurações a partir de variáveis de ambiente."""
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
    }
    return settings