# PRISMA_CURSOS_G4 — Arquitetura BMVC (Bottle MVC)

Aplicação web do **Prisma Cursos** reestruturada na arquitetura **BMVC** (`bmvc_start_from_this`) utilizando **Python + Bottle**, mantendo integralmente o frontend original do projeto e separando responsabilidades em Models, DataRecord (persistência JSON), Controllers e Views (`.tpl`).

## Estrutura do Projeto

```text
PRISMA_CURSOS_G4/
├── route.py                        # Roteador Bottle e ponto de entrada principal
├── startserver.py                  # Wrapper alternativo de inicialização
├── requirements.txt                # Dependências Python (bottle)
├── Dockerfile                      # Container BMVC (porta 8080)
├── app/
│   ├── models/                     # Entidades POO: Curso, Feedback, Contato, EtapaJornada
│   ├── controllers/
│   │   ├── application.py          # Controlador principal (Application)
│   │   ├── datarecord.py           # Camada DataRecord e repositórios JSON
│   │   └── db/                     # Bases JSON (cursos, feedbacks, jornada, contatos)
│   ├── views/html/                 # Templates Bottle (.tpl) das páginas e parciais
│   └── static/                     # CSS, JS, imagens e ícones
└── tests/
    └── test_bmvc.py                # Testes automatizados da aplicação BMVC
```

## Rotas Disponíveis

### Páginas HTML
- `GET /` ou `/inicio` — Página inicial
- `GET /quem-somos` — Página institucional Quem Somos
- `GET /cursos` ou `/vitrine` (com filtro opcional `?categoria=...`) — Vitrine de cursos
- `GET /feedbacks` — Depoimentos dos alunos
- `GET /contatos` e `POST /contatos` — Contatos e formulário de matrícula
- `GET /jornada` ou `/gamific` — Experiência interativa Jornada de Carreira

### API JSON
- `GET /api/cursos` (filtro opcional `?categoria=...`)
- `GET /api/feedbacks`
- `GET /api/jornada`
- `GET /api/contatos`
- `POST /api/contatos`

## Como Executar

### Localmente com Python
```bash
python3 route.py
# ou
python3 startserver.py
```

Variáveis de ambiente opcionais:
- `HOST` (padrão: `0.0.0.0`)
- `PORT` (padrão: tenta `8080` e faz fallback automático para `8081`, `8082`, `8000` caso ocupada)
- `RELOADER` (`true`/`false`, padrão: `false`)

### Com Docker
```bash
docker build -t bmvci .
docker run -d -p 8080:8080 -v $(pwd):/bmeta bmvci
```

### Executar Testes
```bash
pytest -v
```
