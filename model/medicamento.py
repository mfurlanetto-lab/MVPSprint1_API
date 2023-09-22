from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Medicamento (Base):
    __tablename__ = 'medicamento'

    id = Column("medicamento_id", Integer, primary_key=True)
    nome = Column(String(150), unique=True)
    laboratorio = Column(String(100))
    dosagem = Column(String(50))
    # "N" - Não necessita receita; "S" - Receita simples; "C" - Receita controlada
    receita = Column(String(1))
    data_cadastro = Column(DateTime, default=datetime.now())

    def __init__(self, nome: str, laboratorio: str, dosagem: str,
                 receita: int, data_cadastro: Union[DateTime, None] = None):

        self.nome = nome
        self.laboratorio = laboratorio
        self.dosagem = dosagem
        self.receita = receita
        # 0 - Não necessita receita; 1 - Receita simples; 2 - Receita controlada
        # Se a data de cadastro não for informada, será gravada a data atual
        if data_cadastro:
            self.data_cadastro = data_cadastro
