document.addEventListener("DOMContentLoaded", async () => {
    const etapas = document.querySelectorAll(".etapa");

    const overlayExplicacao = document.getElementById(
        "explicacao-overlay"
    );

    const botaoFecharJornada = document.getElementById(
        "fechar-jornada"
    );

    const botaoFecharExplicacao = document.getElementById(
        "fechar-explicacao"
    );

    const botaoVoltar = document.getElementById(
        "voltar-jornada"
    );

    const numeroEtapa = document.getElementById("numero-etapa");
    const tituloEtapa = document.getElementById("titulo-etapa");
    const descricaoEtapa = document.getElementById("descricao-etapa");

    let conteudoEtapas = [];

    const jornadaDataEl = document.getElementById("jornada-data");
    if (jornadaDataEl && jornadaDataEl.textContent.trim()) {
        try {
            conteudoEtapas = JSON.parse(jornadaDataEl.textContent);
        } catch (_erro) {
            conteudoEtapas = [];
        }
    }

    if (conteudoEtapas.length === 0) {
        try {
            const resposta = await fetch("/api/jornada");
            if (resposta.ok) {
                const dados = await resposta.json();
                conteudoEtapas = dados.etapas || [];
            }
        } catch (_erro) {
            conteudoEtapas = [];
        }
    }

    const etapasConcluidas = new Set();

    function abrirExplicacao(indice) {
        const conteudo = conteudoEtapas.find(
            (item) => Number(item.indice) === indice
        ) || conteudoEtapas[indice];

        if (!conteudo) {
            return;
        }

        const totalEtapas = conteudoEtapas.length || 5;
        numeroEtapa.textContent = `Etapa ${indice + 1} de ${totalEtapas}`;
        tituloEtapa.textContent = conteudo.titulo;
        descricaoEtapa.textContent = conteudo.descricao;

        etapasConcluidas.add(indice);

        etapas.forEach((etapa, i) => {
            const concluida = etapasConcluidas.has(i);

            etapa.classList.toggle("selecionada", concluida);

            etapa.setAttribute(
                "aria-pressed",
                String(i === indice)
            );
        });

        overlayExplicacao.inert = false;
        overlayExplicacao.classList.add("aberto");
        overlayExplicacao.setAttribute("aria-hidden", "false");

        botaoFecharExplicacao.focus();
    }

    function fecharExplicacao() {
        if (!overlayExplicacao.classList.contains("aberto")) {
            return;
        }

        overlayExplicacao.classList.remove("aberto");
        overlayExplicacao.setAttribute("aria-hidden", "true");
        overlayExplicacao.inert = true;

        const etapaSelecionada = document.querySelector(
            '.etapa[aria-pressed="true"]'
        );

        if (etapaSelecionada) {
            etapaSelecionada.focus();
        }
    }

    etapas.forEach((etapa) => {
        etapa.addEventListener("click", () => {
            const indice = Number(etapa.dataset.etapa);

            abrirExplicacao(indice);
        });
    });

    botaoFecharExplicacao.addEventListener(
        "click",
        fecharExplicacao
    );

    botaoVoltar.addEventListener(
        "click",
        fecharExplicacao
    );

    overlayExplicacao.addEventListener("click", (evento) => {
        if (evento.target === overlayExplicacao) {
            fecharExplicacao();
        }
    });

    botaoFecharJornada.addEventListener("click", () => {
        window.location.href = "/";
    });

    document.addEventListener("keydown", (evento) => {
        if (evento.key !== "Escape") {
            return;
        }

        if (overlayExplicacao.classList.contains("aberto")) {
            fecharExplicacao();
        } else {
            window.location.href = "/";
        }
    });
});
