function normalizarNota(nota) {
    const valor = Number(nota);

    if (!Number.isFinite(valor)) {
        return 0;
    }

    return Math.max(
        0,
        Math.min(5, Math.round(valor))
    );
}

function criarEstrelas(nota) {
    const notaValida = normalizarNota(nota);

    const estrelas = document.createElement("span");

    estrelas.className = "estrelas";
    estrelas.setAttribute("role", "img");

    estrelas.setAttribute(
        "aria-label",
        notaValida + " de 5 estrelas"
    );

    const simbolos = document.createElement("span");

    simbolos.setAttribute("aria-hidden", "true");

    simbolos.textContent =
        "★".repeat(notaValida) +
        "☆".repeat(5 - notaValida);

    estrelas.appendChild(simbolos);

    return estrelas;
}

function criarCardFeedback(depoimento, indice) {
    const nomeAluno = depoimento.nomeAluno || depoimento.nome_aluno || "";
    const nomeCurso = depoimento.nomeCurso || depoimento.nome_curso || "";

    const card = document.createElement("article");
    card.className = "card-feedback";

    const idTitulo = "feedback-" + indice;

    card.setAttribute(
        "aria-labelledby",
        idTitulo
    );

    const foto = document.createElement("img");

    foto.className = "foto-aluno";
    foto.src = depoimento.foto;
    foto.alt = "Retrato de " + nomeAluno;
    foto.width = 220;
    foto.height = 220;
    foto.loading = indice === 0 ? "eager" : "lazy";
    foto.decoding = "async";

    const conteudo = document.createElement("div");
    conteudo.className = "conteudo-feedback";

    const cabecalho = document.createElement("div");
    cabecalho.className = "cabecalho-feedback";

    const titulo = document.createElement("h2");

    titulo.className = "nome-aluno";
    titulo.id = idTitulo;
    titulo.append(nomeAluno + " — ");

    const curso = document.createElement("span");

    curso.className = "curso-verde";
    curso.textContent = nomeCurso;

    titulo.appendChild(curso);

    const texto = document.createElement("blockquote");

    texto.className = "texto-feedback";
    texto.textContent = depoimento.texto;

    cabecalho.append(
        titulo,
        criarEstrelas(depoimento.nota)
    );

    conteudo.append(
        cabecalho,
        texto
    );

    card.append(
        foto,
        conteudo
    );

    return card;
}

async function carregarFeedbacks() {
    const container = document.getElementById(
        "container-feedbacks"
    );

    if (!container) {
        return;
    }

    try {
        const resposta = await fetch("/api/feedbacks");
        if (!resposta.ok) {
            return;
        }

        const dados = await resposta.json();
        const depoimentos = dados.feedbacks || [];
        if (depoimentos.length === 0) {
            return;
        }

        const fragmento = document.createDocumentFragment();

        depoimentos.forEach((depoimento, indice) => {
            fragmento.appendChild(
                criarCardFeedback(depoimento, indice)
            );
        });

        container.replaceChildren(fragmento);
    } catch (_erro) {
        // Mantém o conteúdo pré-renderizado pelo servidor caso a requisição falhe.
    }
}

document.addEventListener("DOMContentLoaded", carregarFeedbacks);
