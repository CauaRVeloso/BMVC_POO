<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Descubra sua jornada profissional com a Prisma Cursos.">

    <title>Jornada de Carreira | Prisma Cursos</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap"
        rel="stylesheet"
    >

    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
    >

    <link rel="stylesheet" href="/static/css/gamific.css">

    <script src="/static/js/gamific.js" defer></script>
</head>

<body>

    <main class="jornada-overlay">

        <section class="jornada-modal" aria-labelledby="titulo-jornada">

            <button
                type="button"
                class="fechar-jornada"
                id="fechar-jornada"
                aria-label="Fechar jornada e voltar à página inicial"
            >
                &times;
            </button>

            <h1 id="titulo-jornada">
                Sua jornada, do início ao mercado de trabalho:
                <span>clique e descubra seu caminho!</span>
            </h1>

            <div class="linha-etapas" aria-label="Etapas da jornada">
                % for etapa in etapas:
                <button
                    class="etapa"
                    type="button"
                    data-etapa="{{etapa.indice}}"
                    aria-label="Etapa {{etapa.indice + 1}}: {{etapa.titulo}}"
                    aria-pressed="false"
                >
                    <span class="etapa-icone">
                        <i class="{{etapa.icone_fa}}" aria-hidden="true"></i>
                    </span>
                    <span class="etapa-nome">{{etapa.codigo_label}}</span>
                </button>
                % end
            </div>

            <p class="instrucao">
                Clique nas etapas e descubra o que fazer em cada fase
                da sua jornada profissional.
            </p>

        </section>

    </main>

    <div
        class="explicacao-overlay"
        id="explicacao-overlay"
        aria-hidden="true"
        inert
    >
        <section
            class="explicacao-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="titulo-etapa"
            aria-describedby="descricao-etapa"
        >

            <button
                type="button"
                class="fechar-explicacao"
                id="fechar-explicacao"
                aria-label="Fechar explicação da etapa"
            >
                &times;
            </button>

            <span class="explicacao-numero" id="numero-etapa"></span>

            <h2 id="titulo-etapa"></h2>

            <p id="descricao-etapa"></p>

            <button
                type="button"
                class="botao-voltar"
                id="voltar-jornada"
            >
                Voltar à jornada
            </button>

        </section>
    </div>

    <script id="jornada-data" type="application/json">{{!etapas_json}}</script>
</body>
</html>
