"""Camada de persistência JSON (DataRecord) no padrão BMVC."""

from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4

from app.models.contato import Contato
from app.models.curso import Curso
from app.models.etapa_jornada import EtapaJornada
from app.models.feedback import Feedback

DB_DIR = Path(__file__).resolve().parent / "db"


class DataRecord:
    """Gerencia leitura e persistência de modelos em arquivos JSON."""

    def __init__(self, filename, model_cls, db_dir=None):
        self._base_dir = Path(db_dir) if db_dir is not None else DB_DIR
        self._file_path = self._base_dir / filename
        self._model_cls = model_cls
        self._models = self.read()

    def read(self):
        """Lê todos os registros do arquivo JSON e instancia os modelos."""
        if not self._file_path.exists():
            return []
        try:
            with self._file_path.open("r", encoding="utf-8") as arquivo:
                raw_items = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            return []

        if not isinstance(raw_items, list):
            return []

        return [self._model_cls.from_dict(item) for item in raw_items]

    def save(self, items=None):
        """Persiste a lista de modelos no arquivo JSON."""
        if items is not None:
            self._models = list(items)
        self._base_dir.mkdir(parents=True, exist_ok=True)
        payload = [item.to_dict() for item in self._models]
        with self._file_path.open("w", encoding="utf-8") as arquivo:
            json.dump(payload, arquivo, ensure_ascii=False, indent=4)

    def get_all(self):
        """Retorna uma cópia atualizada de todos os modelos armazenados."""
        self._models = self.read()
        return list(self._models)

    def add(self, item):
        """Adiciona um novo modelo e salva no arquivo JSON."""
        self._models = self.read()
        self._models.append(item)
        self.save()
        return item


class CursoRecord(DataRecord):
    """Repositório JSON de cursos da vitrine."""

    def __init__(self, db_dir=None):
        super().__init__("cursos.json", Curso, db_dir=db_dir)

    def get_by_categoria(self, categoria):
        """Filtra cursos pela categoria (comparação case-insensitive)."""
        alvo = (categoria or "").strip().casefold()
        if not alvo:
            return self.get_all()
        return [
            curso
            for curso in self.get_all()
            if curso.categoria.strip().casefold() == alvo
        ]


class FeedbackRecord(DataRecord):
    """Repositório JSON de depoimentos de alunos."""

    def __init__(self, db_dir=None):
        super().__init__("feedbacks.json", Feedback, db_dir=db_dir)


class JornadaRecord(DataRecord):
    """Repositório JSON das etapas da Jornada de Carreira."""

    def __init__(self, db_dir=None):
        super().__init__("jornada.json", EtapaJornada, db_dir=db_dir)

    def get_all(self):
        """Retorna as etapas ordenadas por índice crescente."""
        etapas = super().get_all()
        return sorted(etapas, key=lambda etapa: etapa.indice)


class ContatoRecord(DataRecord):
    """Repositório JSON de contatos e pré-matrículas."""

    def __init__(self, db_dir=None):
        super().__init__("contatos.json", Contato, db_dir=db_dir)

    def book(self, nome, email, telefone):
        """Registra um novo contato com ID único e timestamp UTC."""
        contato = Contato(
            id=uuid4().hex[:8],
            nome=nome,
            email=email,
            telefone=telefone,
            criado_em=datetime.now(timezone.utc).isoformat(),
        )
        return self.add(contato)
