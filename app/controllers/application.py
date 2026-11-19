"""Controlador principal (Application) no padrão BMVC."""

import json
from pathlib import Path

from bottle import TEMPLATE_PATH, template

from app.controllers.datarecord import (
    ContatoRecord,
    CursoRecord,
    FeedbackRecord,
    JornadaRecord,
)

VIEWS_DIR = str(Path(__file__).resolve().parent.parent / "views" / "html")

if VIEWS_DIR not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, VIEWS_DIR)


class Application:
    """Controlador central responsável por orquestrar models, repositórios e views."""

    def __init__(self, db_dir=None):
        self._cursos = CursoRecord(db_dir=db_dir)
        self._feedbacks = FeedbackRecord(db_dir=db_dir)
        self._contatos = ContatoRecord(db_dir=db_dir)
        self._jornada = JornadaRecord(db_dir=db_dir)

        self.pages = {
            "inicio": self.inicio,
            "quem-somos": self.quem_somos,
            "vitrine": self.vitrine,
            "cursos": self.vitrine,
            "feedbacks": self.feedbacks,
            "contatos": self.contatos,
            "gamific": self.gamific,
            "jornada": self.gamific,
        }

    def render(self, page, **kwargs):
        """Despacha a renderização para o método correspondente à página solicitada."""
        handler = self.pages.get(page, self.inicio)
        return handler(**kwargs)

    def inicio(self):
        """Renderiza a página inicial."""
        return template("inicio", pagina_ativa="inicio")

    def quem_somos(self):
        """Renderiza a página institucional Quem Somos."""
        return template("quem-somos", pagina_ativa="quem-somos")

    def vitrine(self, categoria=None):
        """Renderiza a vitrine de cursos com filtro opcional por categoria."""
        categoria_limpa = (categoria or "").strip() or None
        if categoria_limpa:
            cursos = self._cursos.get_by_categoria(categoria_limpa)
        else:
            cursos = self._cursos.get_all()

        return template(
            "vitrine",
            cursos=cursos,
            categoria_ativa=categoria_limpa,
            pagina_ativa="cursos",
        )

    def feedbacks(self):
        """Renderiza a página de depoimentos dos alunos."""
        depoimentos = self._feedbacks.get_all()
        return template(
            "feedbacks",
            depoimentos=depoimentos,
            pagina_ativa="feedbacks",
        )

    def contatos(self, mensagem_sucesso=None, erro=None):
        """Renderiza a página de contatos e formulário de matrícula."""
        return template(
            "contatos",
            pagina_ativa="contatos",
            mensagem_sucesso=mensagem_sucesso,
            erro=erro,
        )

    def registrar_contato(self, nome, email, telefone):
        """Valida os campos obrigatórios e persiste um novo contato."""
        nome_limpo = (nome or "").strip()
        email_limpo = (email or "").strip()
        telefone_limpo = (telefone or "").strip()

        if not nome_limpo or not email_limpo or not telefone_limpo:
            raise ValueError("Por favor, preencha nome, e-mail e telefone.")

        return self._contatos.book(nome_limpo, email_limpo, telefone_limpo)

    def gamific(self):
        """Renderiza a experiência interativa Jornada de Carreira."""
        etapas = self._jornada.get_all()
        etapas_json = json.dumps(
            [etapa.to_dict() for etapa in etapas],
            ensure_ascii=False,
        ).replace("</", "<\\/")
        return template(
            "gamific",
            etapas=etapas,
            etapas_json=etapas_json,
        )

    def api_cursos(self, categoria=None):
        """Retorna os cursos serializados para resposta JSON."""
        categoria_limpa = (categoria or "").strip() or None
        if categoria_limpa:
            cursos = self._cursos.get_by_categoria(categoria_limpa)
        else:
            cursos = self._cursos.get_all()
        return {"cursos": [curso.to_dict() for curso in cursos]}

    def api_feedbacks(self):
        """Retorna os feedbacks serializados para resposta JSON."""
        return {
            "feedbacks": [
                feedback.to_dict() for feedback in self._feedbacks.get_all()
            ]
        }

    def api_jornada(self):
        """Retorna as etapas da jornada serializadas para resposta JSON."""
        return {
            "etapas": [etapa.to_dict() for etapa in self._jornada.get_all()]
        }

    def api_contatos(self):
        """Retorna os contatos registrados serializados para resposta JSON."""
        return {
            "contatos": [
                contato.to_dict() for contato in self._contatos.get_all()
            ]
        }
