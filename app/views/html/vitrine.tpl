<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vitrine - Prisma Cursos</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="/static/css/layout.css">
    <link rel="stylesheet" href="/static/css/vitrine.css">

    <script src="/static/js/vitrine.js" defer></script>
    <script src="/static/js/main.js" defer></script>
</head>
<body>

    % include('header.tpl', pagina_ativa=pagina_ativa)

    <h1 class="escolha-sua-trilha-container">
        <span class="escolha-sua">Escolha sua trilha de aprendizado</span>
        <span class="aprendizagem">aprendizagem:</span>
    </h1>

    % if categoria_ativa:
    <div class="filtro-categoria">
        <span>Categoria: <strong>{{categoria_ativa}}</strong></span>
        <a href="/cursos">Ver todos os cursos</a>
    </div>
    % end

    <section class="cursos-grid">
        % for curso in cursos:
        <article class="{{curso.classe_css}}">
            <div class="frame-child"></div>
            <img class="{{curso.classe_icone}}" src="/static/img/{{curso.icone}}" alt="{{curso.alt}}">
            <h2>{{curso.titulo}}</h2>
            <p class="aprenda-a-criar">{{curso.descricao}}</p>
        </article>
        % end
    </section>

    % include('footer.tpl')

</body>
</html>
