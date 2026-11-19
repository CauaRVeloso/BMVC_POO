"""Modelo de Curso para a vitrine do PRISMA CURSOS."""


class Curso:
    """Representa um curso ofertado na vitrine."""

    def __init__(
        self,
        id,
        titulo,
        descricao,
        categoria,
        classe_css,
        icone,
        classe_icone,
        alt,
    ):
        self.id = str(id)
        self.titulo = str(titulo)
        self.descricao = str(descricao)
        self.categoria = str(categoria)
        self.classe_css = str(classe_css)
        self.icone = str(icone)
        self.classe_icone = str(classe_icone)
        self.alt = str(alt)

    def to_dict(self):
        """Converte o curso para um dicionário serializável em JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "classe_css": self.classe_css,
            "icone": self.icone,
            "classe_icone": self.classe_icone,
            "alt": self.alt,
        }

    @classmethod
    def from_dict(cls, data):
        """Instancia um Curso a partir de um dicionário."""
        return cls(
            id=data.get("id", ""),
            titulo=data.get("titulo", ""),
            descricao=data.get("descricao", ""),
            categoria=data.get("categoria", ""),
            classe_css=data.get("classe_css", "rectangle-parent"),
            icone=data.get("icone", ""),
            classe_icone=data.get("classe_icone", ""),
            alt=data.get("alt", ""),
        )
