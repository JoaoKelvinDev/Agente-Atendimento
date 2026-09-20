from sqlalchemy import create_engine

#Create esta recebendo o endereço do config.py
from sqlalchemy.orm import sessionmaker

from agente_atendimento.config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

#pool faz o sqlalchemy testar a conexao,antes de usar