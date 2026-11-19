<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Conheça a história e os diferenciais da Prisma Cursos.">
    <title>Quem somos | Prisma Cursos</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/layout.css">
    <link rel="stylesheet" href="/static/css/quem-somos.css">

    <script src="/static/js/main.js" defer></script>
</head>
<body>

    % include('header.tpl', pagina_ativa=pagina_ativa)

    <main class="corpo_de_texto">
        <div class="logo_prisma">
            <img src="/static/img/logo-prisma.png" alt="Logótipo Prisma Cursos" class="logo_centralizada">
        </div>

        <h1 class="texto_inicial">Transforme conhecimento em <span class="destaque">possibilidades.</span></h1>

        <div class="texto_central">
            <p>O <span class="destaque">futuro começa</span> com o que você aprende <span class="destaque">hoje.</span></p>
            <p>
            No <span class="destaque">Prisma Cursos</span>, você desenvolve as habilidades necessárias para crescer
            profissionalmente, explorar novas oportunidades e <span class="destaque">se destacar</span> em um
            mercado em constante transformação.</p>
        </div>

        <div class="imagem_robo">
            <img src="/static/img/imagem%20quem%20somos.png" alt="imagem de robo quem somos" class="imagem_centralizada">
        </div>

        <div class="explicacao">
            <p>De <span class="destaque">Web Design, Photoshop e UX Design a Inteligência Artificial, Programação
            Orientada a Objetos em Java e Análise de Dados</span>, você encontra
            conhecimentos práticos para transformar suas ideias em resultados. Além
            disso, desenvolva sua capacidade de tomar decisões estratégicas e gerenciar
            recursos financeiros com mais confiança.</p>
            <p>Aprenda no seu ritmo. Desenvolva seu <span class="destaque">potencial</span>. Construa seu <span class="destaque">futuro.</span>
            No <span class="destaque">Prisma Cursos</span>, cada aprendizado é uma nova perspectiva para enxergar
            oportunidades e <span class="destaque">ir além.</span></p>
        </div>
    </main>

    % include('footer.tpl')

</body>
</html>
