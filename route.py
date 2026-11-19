"""Roteador principal e entrypoint do servidor BMVC do PRISMA CURSOS."""

import os
from pathlib import Path
import socket

from bottle import Bottle, redirect, request, response, static_file

from app.controllers.application import Application

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = str(BASE_DIR / "app" / "static")
FALLBACK_PORTS = (8080, 8081, 8082, 8000)


def register_routes(bottle_app, controller):
    """Registra rotas estáticas, HTML e JSON na instância Bottle."""

    @bottle_app.route("/static/<filepath:path>")
    def serve_static(filepath):
        resolved_path = filepath
        candidate = Path(STATIC_DIR) / resolved_path
        if not candidate.exists():
            try:
                utf8_path = resolved_path.encode("latin-1").decode("utf-8")
                if (Path(STATIC_DIR) / utf8_path).exists():
                    resolved_path = utf8_path
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass
        return static_file(resolved_path, root=STATIC_DIR)

    @bottle_app.route("/favicon.ico")
    def favicon():
        return static_file("img/logo-prisma.png", root=STATIC_DIR)

    @bottle_app.route("/")
    @bottle_app.route("/inicio")
    def inicio():
        return controller.render("inicio")

    @bottle_app.route("/quem-somos")
    def quem_somos():
        return controller.render("quem-somos")

    @bottle_app.route("/cursos")
    @bottle_app.route("/vitrine")
    def vitrine():
        categoria = request.query.getunicode("categoria") or None
        return controller.render("vitrine", categoria=categoria)

    @bottle_app.route("/feedbacks")
    def feedbacks():
        return controller.render("feedbacks")

    @bottle_app.route("/contatos", method="GET")
    def contatos():
        return controller.render("contatos")

    @bottle_app.route("/contatos", method="POST")
    def contatos_post():
        nome = request.forms.getunicode("nome")
        email = request.forms.getunicode("email")
        telefone = request.forms.getunicode("telefone")
        try:
            controller.registrar_contato(nome, email, telefone)
        except ValueError as exc:
            response.status = 400
            return controller.render("contatos", erro=str(exc))

        return controller.render(
            "contatos",
            mensagem_sucesso="Mensagem enviada com sucesso!",
        )

    @bottle_app.route("/jornada")
    @bottle_app.route("/gamific")
    def gamific():
        return controller.render("gamific")

    # Redirecionamentos de compatibilidade para URLs antigas do frontend estático
    @bottle_app.route("/index.html")
    @bottle_app.route("/pages/inicio.html")
    def legacy_inicio():
        return redirect("/")

    @bottle_app.route("/pages/quem-somos.html")
    def legacy_quem_somos():
        return redirect("/quem-somos")

    @bottle_app.route("/pages/vitrine.html")
    def legacy_vitrine():
        return redirect("/cursos")

    @bottle_app.route("/pages/feedbacks.html")
    def legacy_feedbacks():
        return redirect("/feedbacks")

    @bottle_app.route("/pages/contatos.html")
    def legacy_contatos():
        return redirect("/contatos")

    @bottle_app.route("/pages/gamific.html")
    def legacy_gamific():
        return redirect("/jornada")

    # Endpoints JSON (API)
    @bottle_app.route("/api/cursos", method="GET")
    def api_cursos():
        categoria = request.query.getunicode("categoria") or None
        return controller.api_cursos(categoria=categoria)

    @bottle_app.route("/api/feedbacks", method="GET")
    def api_feedbacks():
        return controller.api_feedbacks()

    @bottle_app.route("/api/jornada", method="GET")
    def api_jornada():
        return controller.api_jornada()

    @bottle_app.route("/api/contatos", method="GET")
    def api_contatos():
        return controller.api_contatos()

    @bottle_app.route("/api/contatos", method="POST")
    def api_contatos_post():
        payload = request.json
        if isinstance(payload, dict):
            nome = payload.get("nome", "")
            email = payload.get("email", "")
            telefone = payload.get("telefone", "")
        else:
            nome = request.forms.getunicode("nome")
            email = request.forms.getunicode("email")
            telefone = request.forms.getunicode("telefone")

        try:
            contato = controller.registrar_contato(nome, email, telefone)
        except ValueError as exc:
            response.status = 400
            return {"status": "erro", "message": str(exc)}

        response.status = 201
        return {
            "status": "ok",
            "message": "Mensagem enviada com sucesso!",
            "contato": contato.to_dict(),
        }


def create_app(db_dir=None):
    """Cria uma instância isolada da aplicação BMVC (útil para testes)."""
    bottle_app = Bottle()
    controller = Application(db_dir=db_dir)
    register_routes(bottle_app, controller)
    return bottle_app, controller


def _port_is_available(host, port):
    """Verifica se a porta TCP pode ser vinculada pelo servidor."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((host, port))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def resolve_port(host="0.0.0.0"):
    """Resolve a porta do servidor a partir de PORT ou fallback automático."""
    env_port = os.environ.get("PORT")
    if env_port:
        return int(env_port)

    for candidate in FALLBACK_PORTS:
        if _port_is_available(host, candidate):
            return candidate

    return FALLBACK_PORTS[0]


def run_server():
    """Inicia o servidor Bottle para o projeto PRISMA CURSOS BMVC."""
    host = os.environ.get("HOST", "0.0.0.0")
    port = resolve_port(host)
    reloader = os.environ.get("RELOADER", "false").lower() == "true"

    print(
        f"Servidor BMVC PRISMA CURSOS rodando em http://localhost:{port} (bind {host}:{port})",
        flush=True,
    )
    app.run(host=host, port=port, debug=True, reloader=reloader)


ctl = Application()
app = Bottle()
register_routes(app, ctl)


if __name__ == "__main__":
    run_server()
