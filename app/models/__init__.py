"""Modelos de domínio da aplicação PRISMA CURSOS."""

from app.models.contato import Contato
from app.models.curso import Curso
from app.models.etapa_jornada import EtapaJornada
from app.models.feedback import Feedback

__all__ = ["Curso", "Feedback", "Contato", "EtapaJornada"]
