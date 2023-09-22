from pydantic import BaseModel
from typing import Optional, List
from model.medicamento import Medicamento


class MedicamentoSchema(BaseModel):
    """ Define como um novo medicamento a ser inserido deve ser representado
    """
    nome: str = "Sorine"
    laboratorio: Optional[str] = "Aché"
    dosagem: Optional[str] = "3mg"
    receita: Optional[str] = "N"


class MedicamentoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do medicamento.
    """
    nome: str = "Teste"


class ListagemMedicamentosSchema(BaseModel):
    """ Define como uma listagem de medicamentos será retornada.
    """
    medicamentos: List[MedicamentoSchema]


class MedicamentoViewSchema(BaseModel):
    """ Define como um medicamento será retornado: medicamento + estoque.
    """
    id: int = 1
    nome: str = "Sorine"
    laboratorio: str = "Aché"
    dosagem: str = "3mg"
    receita: int = 0


class MedicamentoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    nome: str


def apresenta_medicamento(medicamento: Medicamento):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return {
        "id": medicamento.id,
        "nome": medicamento.nome,
        "laboratorio": medicamento.laboratorio,
        "dosagem": medicamento.dosagem,
        "receita": medicamento.receita,
    }


def apresenta_medicamentos(medicamentos: List[Medicamento]):
    """ Retorna uma representação de medicamentos cadastrados seguindo o schema definido em
        MedicamentoViewSchema.
    """
    result = []
    for medicamento in medicamentos:
        result.append({
            "nome": medicamento.nome,
            "laboratorio": medicamento.laboratorio,
            "dosagem": medicamento.dosagem,
            "receita": medicamento.receita,
        })

    return {"medicamentos": result}
