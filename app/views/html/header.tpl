<header class="navbar-global">
    <div class="navbar-content">

        <a href="/" class="logo" aria-label="Prisma Cursos - Início">
            <span class="logo-text">PRISMA<br>CURSOS</span>
            <img src="/static/img/logo-prisma.png" alt="Logótipo Prisma Cursos">
        </a>

        <button
            class="menu-toggle"
            type="button"
            aria-label="Abrir menu"
            aria-expanded="false"
            aria-controls="menu-principal">
            &#9776;
        </button>

        <nav aria-label="Navegação principal">
            <ul class="nav-links" id="menu-principal">
                <li>
                    <a href="/"
                       class="{{'active' if get('pagina_ativa') == 'inicio' else ''}}"
                       {{!'aria-current="page"' if get('pagina_ativa') == 'inicio' else ''}}>Início</a>
                </li>
                <li>
                    <a href="/quem-somos"
                       class="{{'active' if get('pagina_ativa') == 'quem-somos' else ''}}"
                       {{!'aria-current="page"' if get('pagina_ativa') == 'quem-somos' else ''}}>Quem somos</a>
                </li>
                <li>
                    <a href="/cursos"
                       class="{{'active' if get('pagina_ativa') == 'cursos' else ''}}"
                       {{!'aria-current="page"' if get('pagina_ativa') == 'cursos' else ''}}>Cursos</a>
                </li>
                <li>
                    <a href="/feedbacks"
                       class="{{'active' if get('pagina_ativa') == 'feedbacks' else ''}}"
                       {{!'aria-current="page"' if get('pagina_ativa') == 'feedbacks' else ''}}>Feedbacks</a>
                </li>
                <li>
                    <a href="/contatos"
                       class="{{'active' if get('pagina_ativa') == 'contatos' else ''}}"
                       {{!'aria-current="page"' if get('pagina_ativa') == 'contatos' else ''}}>Contatos</a>
                </li>
            </ul>
        </nav>

    </div>
</header>
