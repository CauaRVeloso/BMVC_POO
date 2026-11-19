"""Testes automatizados da aplicação PRISMA CURSOS em arquitetura BMVC."""

import json
from pathlib import Path
import shutil
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
from wsgiref.simple_server import WSGIRequestHandler, make_server

import pytest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import route

DB_SEED_DIR = ROOT_DIR / "app" / "controllers" / "db"


class _QuietHandler(WSGIRequestHandler):
    def log_message(self, format, *args):  # noqa: A002
        return


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


@pytest.fixture()
def bmvc_server(tmp_path):
    """Sobe uma instância real do servidor BMVC em porta efêmera com banco isolado."""
    for json_file in DB_SEED_DIR.glob("*.json"):
        shutil.copy2(json_file, tmp_path / json_file.name)
    (tmp_path / "contatos.json").write_text("[]", encoding="utf-8")

    bottle_app, _ctl = route.create_app(db_dir=tmp_path)
    server = make_server("127.0.0.1", 0, bottle_app, handler_class=_QuietHandler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        yield f"http://127.0.0.1:{port}", tmp_path
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def _request(url, method="GET", data=None, headers=None, follow_redirects=True):
    req = urllib.request.Request(
        url,
        data=data,
        headers=headers or {},
        method=method,
    )
    opener = (
        urllib.request.build_opener()
        if follow_redirects
        else urllib.request.build_opener(_NoRedirectHandler())
    )
    try:
        with opener.open(req) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as err:
        return err.code, dict(err.headers), err.read()


def test_html_routes_return_200_and_expected_content(bmvc_server):
    base_url, _ = bmvc_server
    expected_pages = [
        ("/", "SEU PRÓXIMO NÍVEL COMEÇA"),
        ("/inicio", "Prisma Cursos"),
        ("/quem-somos", "Transforme conhecimento em"),
        ("/cursos", "Web design"),
        ("/vitrine", "POO em Java"),
        ("/feedbacks", "Marina Becker"),
        ("/contatos", "Deseja falar conosco?"),
        ("/jornada", "Sua jornada, do início ao mercado de trabalho"),
        ("/gamific", "1-Matrícula"),
    ]

    for path, marker in expected_pages:
        status, headers, body = _request(f"{base_url}{path}")
        html = body.decode("utf-8")
        assert status == 200, f"Falha em {path}"
        assert "text/html" in headers.get("Content-Type", "")
        assert marker in html


def test_vitrine_category_filter_html(bmvc_server):
    base_url, _ = bmvc_server
    query = urllib.parse.urlencode({"categoria": "Tecnologia"})
    status, _headers, body = _request(f"{base_url}/cursos?{query}")
    html = body.decode("utf-8")

    assert status == 200
    assert "POO em Java" in html
    assert "Análise de Dados" in html
    assert "I.A" in html
    assert "Web design" not in html
    assert "Ver todos os cursos" in html


def test_legacy_redirects(bmvc_server):
    base_url, _ = bmvc_server
    redirects = [
        ("/index.html", "/"),
        ("/pages/inicio.html", "/"),
        ("/pages/quem-somos.html", "/quem-somos"),
        ("/pages/vitrine.html", "/cursos"),
        ("/pages/feedbacks.html", "/feedbacks"),
        ("/pages/contatos.html", "/contatos"),
        ("/pages/gamific.html", "/jornada"),
    ]

    for old_path, target_path in redirects:
        status, headers, _body = _request(
            f"{base_url}{old_path}",
            follow_redirects=False,
        )
        assert status in (302, 303), f"Esperado redirect para {old_path}"
        assert headers.get("Location", "").endswith(target_path)


def test_static_assets_including_spaces_and_utf8(bmvc_server):
    base_url, _ = bmvc_server
    static_paths = [
        "/static/css/layout.css",
        "/static/js/main.js",
        "/static/icons/WhatsApp.svg",
        "/static/img/logo-prisma.png",
        "/static/img/imagem%20quem%20somos.png",
        "/static/img/jos%C3%A9.png",
    ]

    for asset in static_paths:
        status, _headers, body = _request(f"{base_url}{asset}")
        assert status == 200, f"Static asset falhou: {asset}"
        assert len(body) > 0


def test_api_get_endpoints(bmvc_server):
    base_url, _ = bmvc_server

    status, _headers, body = _request(f"{base_url}/api/cursos")
    assert status == 200
    cursos_data = json.loads(body.decode("utf-8"))
    assert len(cursos_data["cursos"]) == 9

    query = urllib.parse.urlencode({"categoria": "Gestão"})
    status, _headers, body = _request(f"{base_url}/api/cursos?{query}")
    assert status == 200
    gestao_data = json.loads(body.decode("utf-8"))
    titulos = {curso["titulo"] for curso in gestao_data["cursos"]}
    assert titulos == {"CEO", "Gestão Financeira"}

    status, _headers, body = _request(f"{base_url}/api/feedbacks")
    assert status == 200
    feedbacks_data = json.loads(body.decode("utf-8"))
    assert len(feedbacks_data["feedbacks"]) == 9
    assert feedbacks_data["feedbacks"][6]["foto"] == "/static/img/josé.png"

    status, _headers, body = _request(f"{base_url}/api/jornada")
    assert status == 200
    jornada_data = json.loads(body.decode("utf-8"))
    assert len(jornada_data["etapas"]) == 5
    assert [etapa["indice"] for etapa in jornada_data["etapas"]] == [0, 1, 2, 3, 4]


def test_api_contatos_validation_and_persistence(bmvc_server):
    base_url, tmp_db = bmvc_server

    invalid_payload = json.dumps({"nome": "João", "email": "", "telefone": ""}).encode("utf-8")
    status, _headers, body = _request(
        f"{base_url}/api/contatos",
        method="POST",
        data=invalid_payload,
        headers={"Content-Type": "application/json"},
    )
    assert status == 400
    assert json.loads(body.decode("utf-8"))["status"] == "erro"

    valid_payload = json.dumps(
        {
            "nome": "João da Conceição",
            "email": "joao@prisma.edu.br",
            "telefone": "(61) 99999-0000",
        },
        ensure_ascii=False,
    ).encode("utf-8")
    status, _headers, body = _request(
        f"{base_url}/api/contatos",
        method="POST",
        data=valid_payload,
        headers={"Content-Type": "application/json"},
    )
    assert status == 201
    created = json.loads(body.decode("utf-8"))
    assert created["status"] == "ok"
    assert created["contato"]["nome"] == "João da Conceição"

    status, _headers, body = _request(f"{base_url}/api/contatos")
    assert status == 200
    listed = json.loads(body.decode("utf-8"))["contatos"]
    assert len(listed) == 1
    assert listed[0]["nome"] == "João da Conceição"

    saved_json = json.loads((tmp_db / "contatos.json").read_text(encoding="utf-8"))
    assert len(saved_json) == 1
    assert saved_json[0]["email"] == "joao@prisma.edu.br"


def test_html_form_post_contatos(bmvc_server):
    base_url, tmp_db = bmvc_server

    empty_form = urllib.parse.urlencode({"nome": "", "email": "", "telefone": ""}).encode("utf-8")
    status, _headers, body = _request(
        f"{base_url}/contatos",
        method="POST",
        data=empty_form,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert status == 400
    assert "Por favor, preencha nome, e-mail e telefone." in body.decode("utf-8")

    valid_form = urllib.parse.urlencode(
        {
            "nome": "María José",
            "email": "maria@prisma.edu.br",
            "telefone": "(61) 98888-1234",
        }
    ).encode("utf-8")
    status, _headers, body = _request(
        f"{base_url}/contatos",
        method="POST",
        data=valid_form,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert status == 200
    assert "Mensagem enviada com sucesso!" in body.decode("utf-8")

    saved_json = json.loads((tmp_db / "contatos.json").read_text(encoding="utf-8"))
    assert len(saved_json) == 1
    assert saved_json[0]["nome"] == "María José"


def test_default_route_app_smoke():
    assert route.ctl.render("inicio")
    assert len(route.ctl.api_cursos()["cursos"]) == 9
    assert len(route.ctl.api_feedbacks()["feedbacks"]) == 9
    assert len(route.ctl.api_jornada()["etapas"]) == 5
