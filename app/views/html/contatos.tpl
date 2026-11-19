<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contatos - Prisma Cursos</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/layout.css">
    <link rel="stylesheet" href="/static/css/contatos.css">

    <script src="/static/js/main.js" defer></script>
</head>
<body>

    % include('header.tpl', pagina_ativa=pagina_ativa)

    <main class="contact-main">
        <section class="contact-left">
            <h1 class="contact-title">Deseja falar conosco?</h1>
            <form class="contact-form" id="formContato" method="post" action="/contatos">
                <input type="text" name="nome" placeholder="Digite seu nome..." required>
                <input type="email" name="email" placeholder="Digite seu email..." required>
                <input type="tel" name="telefone" placeholder="Digite seu telefone..." required>
                <button type="submit" class="btn-enviar">Enviar</button>

                % if mensagem_sucesso:
                <p class="form-feedback sucesso" id="formFeedback" role="status">{{mensagem_sucesso}}</p>
                % elif erro:
                <p class="form-feedback erro" id="formFeedback" role="alert">{{erro}}</p>
                % else:
                <p class="form-feedback" id="formFeedback" role="status" hidden></p>
                % end
            </form>
        </section>

        <section class="contact-right">
            <h1 class="contact-title">Nossos Contatos e<br>Redes sociais</h1>
            <ul class="social-list">
                <li>
                    <img src="/static/icons/WhatsApp.svg" alt="WhatsApp">
                    <span>(61) 9-9636-0110</span>
                </li>
                <li>
                    <img src="/static/icons/Gmail.svg" alt="Email">
                    <span>prismacursos@prisma.edu.br</span>
                </li>
                <li>
                    <img src="/static/icons/Instagram.svg" alt="Instagram">
                    <span>@prismacursosfc</span>
                </li>
            </ul>

            <div class="progress-section">
                <p>Vamos ver até onde você chega!</p>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill"></div>
                </div>
            </div>
        </section>
    </main>

</body>
</html>
