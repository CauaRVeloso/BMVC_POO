"""Modelo de Etapa da Jornada de Carreira (Gamificação) do PRISMA CURSOS."""


class EtapaJornada:
    """Representa uma etapa da trilha interativa Jornada de Carreira."""

    def __init__(self, indice, codigo_label, titulo, descricao, icone_fa):
        self.indice = int(indice)
        self.codigo_label = str(codigo_label)
        self.titulo = str(titulo)
        self.descricao = str(descricao)
        self.icone_fa = str(icone_fa)

    def to_dict(self):
        """Converte a etapa para dicionário serializável em JSON."""
        return {
            "indice": self.indice,
            "codigo_label": self.codigo_label,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "icone_fa": self.icone_fa,
        }

    @classmethod
    def from_dict(cls, data):
        """Instancia uma EtapaJornada a partir de um dicionário."""
        return cls(
            indice=data.get("indice", 0),
            codigo_label=data.get("codigo_label", ""),
            titulo=data.get("titulo", ""),
            descricao=data.get("descricao", ""),
            icone_fa=data.get("icone_fa", ""),
        )
