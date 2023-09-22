from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc

from model import Session, Medicamento

from schemas import *

from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

app.debug = True  # modo de depuração

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
medicamento_tag = Tag(
    name="Medicamento", description="Consultar, incluir e excluir medicamento do cadastro de medicamentos")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/medicamento', tags=[medicamento_tag],
          responses={"200": MedicamentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_medicamento(form: MedicamentoSchema):
    """Cadastra novo medicamento

    Retorna uma representação do medicamento cadastrado.
    """
    medicamento = Medicamento(
        nome=form.nome,
        laboratorio=form.laboratorio,
        dosagem=form.dosagem,
        receita=form.receita
    )

    try:
        session = Session()
        # adicionando medicamento
        session.add(medicamento)
        session.commit()
        return apresenta_medicamento(medicamento), 200

    except IntegrityError as e:
        session.rollback()
        msg = "Medicamento '" + \
            medicamento.nome + "' já existente, verifique!"
        print(str(e))
        return {"mensagem": msg}, 409

    except Exception as e:
        session.rollback()
        msg = "Erro ao gravar o medicamento."
        print(str(e))
        return {"mensagem": msg}, 400


@app.get('/listar_medicamentos', tags=[medicamento_tag],
         responses={"200": ListagemMedicamentosSchema, "404": ErrorSchema})
def listar_medicamentos():
    """Apresenta os medicamentos cadastrados

    Retorna uma lista de medicamentos.
    """
    # Crie uma sessão
    session = Session()

    # Consulta para obter todos os medicamentos por data de validade
    medicamentos = session.query(Medicamento).order_by(
        asc(Medicamento.nome)).all()

    # Feche a sessão
    # session.close()

    if not medicamentos:
        # se não há medicamentos cadastrados
        return {"medicamentos": []}, 200
    else:
        # retorna a representação do medicamento
        return apresenta_medicamentos(medicamentos), 200


@app.delete('/medicamento', tags=[medicamento_tag],
            responses={"200": MedicamentoDelSchema, "404": ErrorSchema})
def del_medicamento(query: MedicamentoBuscaSchema):
    """Deleta um medicamento a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    medicamento_nome = unquote(unquote(query.nome))

    # criando conexão com a base
    session = Session()

    medicamento = session.query(Medicamento).filter(
        Medicamento.nome == medicamento_nome). first()

    # exclui o medicamento
    count = session.query(Medicamento).filter(
        Medicamento.nome == medicamento_nome).delete()

    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mensagem": "Medicamento removido", "nome": medicamento_nome}, 200
    else:
        # se o medicamento não foi encontrado
        return {"mensagem": "Medicamento não existente!"}, 404
