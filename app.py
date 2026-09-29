# app.py
# Aplicação Flask do sistema de agendamentos da Barbearia Navalha de Ouro.
# Define as rotas do sistema e conecta os templates Jinja2 aos dados do banco.

from flask import Flask, render_template
from agendamentos import listar_agendamentos, buscar_agendamento, listar_por_status

app = Flask(__name__)

NOME_BARBEARIA = "Barbearia Navalha de Ouro"


@app.route("/")
def index():
    """Rota inicial: exibe o nome da barbearia e o número de agendamentos."""
    agendamentos = listar_agendamentos()
    return render_template("index.html", nome_barbearia=NOME_BARBEARIA, agendamentos=agendamentos)


@app.route("/agendamentos")
def agendamentos_view():
    """Exibe a tabela com todos os agendamentos cadastrados."""
    agendamentos = listar_agendamentos()
    return render_template(
        "agendamentos.html",
        nome_barbearia=NOME_BARBEARIA,
        agendamentos=agendamentos,
        status_atual=None
    )


@app.route("/agendamentos/status/<status>")
def agendamentos_por_status(status):
    """Exibe apenas os agendamentos que possuem o status informado na URL."""
    agendamentos = listar_por_status(status)
    return render_template(
        "agendamentos.html",
        nome_barbearia=NOME_BARBEARIA,
        agendamentos=agendamentos,
        status_atual=status
    )


@app.route("/agendamento/<int:id>")
def detalhe(id):
    """Exibe todos os dados de um agendamento específico."""
    agendamento = buscar_agendamento(id)
    return render_template("detalhe.html", nome_barbearia=NOME_BARBEARIA, agendamento=agendamento)


if __name__ == "__main__":
    # debug=True facilita o desenvolvimento, exibindo erros detalhados no navegador
    app.run(debug=True)
