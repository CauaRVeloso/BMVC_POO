"""Modelo de Feedback (depoimento de aluno) do PRISMA CURSOS."""


class Feedback:
    """Representa um depoimento de aluno sobre um curso."""

    def __init__(self, id, nome_aluno, nome_curso, nota, texto, foto):
        self.id = str(id)
        self.nome_aluno = str(nome_aluno)
        self.nome_curso = str(nome_curso)
        self.nota = self._normalizar_nota(nota)
        self.texto = str(texto)
        self.foto = str(foto)

    @staticmethod
    def _normalizar_nota(nota):
        """Garante que a nota fique entre 0 e 5."""
        try:
            valor = round(float(nota))
        except (TypeError, ValueError):
            return 0
        return max(0, min(5, int(valor)))

    def estrelas_texto(self):
        """Retorna representação visual das estrelas (★ e ☆)."""
        return ("★" * self.nota) + ("☆" * (5 - self.nota))

    def to_dict(self):
        """Converte o feedback para dicionário compatível com API e frontend."""
        return {
            "id": self.id,
            "nome_aluno": self.nome_aluno,
            "nome_curso": self.nome_curso,
            "nomeAluno": self.nome_aluno,
            "nomeCurso": self.nome_curso,
            "nota": self.nota,
            "texto": self.texto,
            "foto": self.foto,
        }

    @classmethod
    def from_dict(cls, data):
        """Instancia um Feedback aceitando chaves em snake_case ou camelCase."""
        return cls(
            id=data.get("id", ""),
            nome_aluno=data.get("nome_aluno") or data.get("nomeAluno", ""),
            nome_curso=data.get("nome_curso") or data.get("nomeCurso", ""),
            nota=data.get("nota", 5),
            texto=data.get("texto", ""),
            foto=data.get("foto", ""),
        )
