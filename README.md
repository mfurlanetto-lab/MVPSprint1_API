# Minha API - Cadastro de Medicamentos

Este pequeno projeto será entregue para avaliação do curso Engenharia de Sofware - Sprint 1. 

Trata-se de um cadastro simples de medicamentos, que permite a manutenção das informações Nome, Laboratório, Dosagem e Tipo de Receita, através das operações de consulta, alteração, inclusão e exclusão.

Foram criados dois repositórios: api e do front-end.

As soluções utilizadas foram: Flask, SqlAlchemy, SQLite e a documentação OpenAPI.

---
## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

Após clonar o repositório do GIT, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
