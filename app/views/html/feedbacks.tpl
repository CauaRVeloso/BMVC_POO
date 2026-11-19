<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Confira as experiências dos alunos da Prisma Cursos.">

    <title>Feedbacks de alunos | Prisma Cursos</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="/static/css/layout.css">
    <link rel="stylesheet" href="/static/css/feedbacks.css">

    <script src="/static/js/feedbacks.js" defer></script>
    <script src="/static/js/main.js" defer></script>
</head>

<body>
    % include('header.tpl', pagina_ativa=pagina_ativa)

    <main class="secao-feedbacks">
        <div class="container-feedbacks">
            <h1 class="titulo-feedbacks">
                Confira as experiências de quem já fez parte da Prisma Cursos
            </h1>

            <div class="lista-feedbacks" id="container-feedbacks">
                % for indice, depoimento in enumerate(depoimentos):
                <article class="card-feedback" aria-labelledby="feedback-{{indice}}">
                    <img
                        class="foto-aluno"
                        src="{{depoimento.foto}}"
                        alt="Retrato de {{depoimento.nome_aluno}}"
                        width="220"
                        height="220"
                        loading="{{'eager' if indice == 0 else 'lazy'}}"
                        decoding="async"
                    >
                    <div class="conteudo-feedback">
                        <div class="cabecalho-feedback">
                            <h2 class="nome-aluno" id="feedback-{{indice}}">{{depoimento.nome_aluno}} — <span class="curso-verde">{{depoimento.nome_curso}}</span></h2>
                            <span class="estrelas" role="img" aria-label="{{depoimento.nota}} de 5 estrelas">
                                <span aria-hidden="true">{{depoimento.estrelas_texto()}}</span>
                            </span>
                        </div>
                        <blockquote class="texto-feedback">{{depoimento.texto}}</blockquote>
                    </div>
                </article>
                % end
            </div>
        </div>
    </main>

    % include('footer.tpl')
</body>
</html>
