# models.py
# Módulo de modelagem - contém a classe Agendamento, responsável por representar
# um agendamento da barbearia usando Programação Orientada a Objetos (POO).

class Agendamento:
    """Representa um agendamento cadastrado no sistema da barbearia."""

    def __init__(self, cliente, telefone, servico, preco, barbeiro, data, horario,
                 status="Agendado", id=None):
        # Atributos exigidos pela situação de aprendizagem
        self.id = id
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

    def exibir(self):
        """Retorna os dados do agendamento formatados em uma única linha de texto."""
        return (f"[{self.id}] {self.cliente} - {self.servico} com {self.barbeiro} "
                f"em {self.data} às {self.horario} - R$ {self.preco} - Status: {self.status}")

    def converte_tupla(self):
        """
        Converte os dados do objeto em uma tupla, na ordem usada pelas instruções
        INSERT/UPDATE do banco de dados (sem o id, que é gerado automaticamente).
        """
        return (self.cliente, self.telefone, self.servico, self.preco,
                self.barbeiro, self.data, self.horario, self.status)

    @staticmethod
    def reverte_tupla(tupla):
        """
        Recebe uma tupla vinda de uma consulta ao banco de dados, no formato
        (id, cliente, telefone, servico, preco, barbeiro, data, horario, status),
        e retorna um objeto Agendamento correspondente.
        """
        return Agendamento(
            id=tupla[0],
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=tupla[4],
            barbeiro=tupla[5],
            data=tupla[6],
            horario=tupla[7],
            status=tupla[8]
        )
