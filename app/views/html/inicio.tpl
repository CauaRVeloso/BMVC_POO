<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Explore os cursos da Prisma Cursos e desenvolva novas habilidades.">

    <title>Início | Prisma Cursos</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="/static/css/layout.css">
    <link rel="stylesheet" href="/static/css/inicio.css">

    <script src="/static/js/main.js" defer></script>
</head>
<body>

    % include('header.tpl', pagina_ativa=pagina_ativa)

    <main class="inicio">

        <section class="apresentacao">

            <h1>
                SEU PRÓXIMO NÍVEL COMEÇA
                <span class="destaque">AQUI.</span>
            </h1>

            <p>
                Desenvolva habilidades, amplie horizontes e prepare-se para
                oportunidades do futuro.
            </p>

            <a href="/cursos" class="botao">
                Explore nossos Cursos <span aria-hidden="true">➜</span>
            </a>

        </section>

        <section class="categorias" aria-label="Áreas de conhecimento">

            <a href="/cursos?categoria=Tecnologia" class="categoria">
                <img src="/static/img/tecnologia.png" alt="">
                <span>Tecnologia</span>
            </a>

            <a href="/cursos?categoria=Design%20e%20Criatividade" class="categoria">
                <img src="/static/img/criatividade.png" alt="">
                <span>Design e Criatividade</span>
            </a>

            <a href="/cursos?categoria=Estrat%C3%A9gia" class="categoria">
                <img src="/static/img/estrategia.png" alt="">
                <span>Estratégia</span>
            </a>

            <a href="/cursos?categoria=Gest%C3%A3o" class="categoria">
                <img src="/static/img/gestao.png" alt="">
                <span>Gestão</span>
            </a>

        </section>

        <section class="proposta">

            <h2>
                Seja online ou presencial, a
                <span class="destaque">Prisma Cursos</span> se adapta à sua necessidade.
            </h2>

            <h3>VOCÊ É DIFERENTE</h3>

            <p class="subtitulo">
                Seu aprendizado também deve ser.
            </p>

            <div class="chamadas-acao">

                <div class="chamada">
                    <h4>
                        Descubra <span class="destaque">sua jornada</span><br>
                        conosco:
                    </h4>

                    <a href="/jornada" class="botao">
                        Jornada de carreira
                    </a>
                </div>

                <div class="chamada">
                    <h4>Matricule-se já:</h4>

                    <a href="/contatos" class="botao">
                        Matricule-se
                    </a>
                </div>

            </div>

        </section>

    </main>

    % include('footer.tpl')

</body>
</html>
