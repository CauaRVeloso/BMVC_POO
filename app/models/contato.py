"""Modelo de Contato/Matrícula do PRISMA CURSOS."""


class Contato:
    """Representa uma solicitação de contato ou pré-matrícula enviada pelo formulário."""

    def __init__(self, id, nome, email, telefone, criado_em):
        self.id = str(id)
        self.nome = str(nome)
        self.email = str(email)
        self.telefone = str(telefone)
        self.criado_em = str(criado_em)

    def to_dict(self):
        """Converte o contato para dicionário serializável em JSON."""
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "criado_em": self.criado_em,
        }

    @classmethod
    def from_dict(cls, data):
        """Instancia um Contato a partir de um dicionário."""
        return cls(
            id=data.get("id", ""),
            nome=data.get("nome", ""),
            email=data.get("email", ""),
            telefone=data.get("telefone", ""),
            criado_em=data.get("criado_em", ""),
        )
