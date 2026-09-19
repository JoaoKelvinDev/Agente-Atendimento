from sqlalchemy import text

from agente_atendimento.db.session import engine


def test_conexao_com_banco():
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT 1")).scalar()

        assert resultado == 1