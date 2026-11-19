document.documentElement.classList.add('js-ativo');

const PASTA_IMAGENS = '/static/img/';

function criarCard(curso) {
    const card = document.createElement('article');
    card.className = curso.classe_css || curso.classe || 'rectangle-parent';

    const faixa = document.createElement('div');
    faixa.className = 'frame-child';

    const img = document.createElement('img');
    img.className = curso.classe_icone || curso.classeIcone || '';
    img.src = PASTA_IMAGENS + curso.icone;
    img.alt = curso.alt || curso.titulo;

    const titulo = document.createElement('h2');
    titulo.textContent = curso.titulo;

    const descricao = document.createElement('p');
    descricao.className = 'aprenda-a-criar';
    descricao.textContent = curso.descricao;

    card.append(faixa, img, titulo, descricao);
    return card;
}

function inicializarAnimacoesEImagens(grade) {
    const cards = grade.querySelectorAll(':scope > *');

    if ('IntersectionObserver' in window) {
        const observador = new IntersectionObserver((entradas) => {
            entradas.forEach((entrada) => {
                if (!entrada.isIntersecting) return;

                const card = entrada.target;
                card.classList.add('visivel');
                setTimeout(() => { card.style.transitionDelay = ''; }, 800);
                observador.unobserve(card);
            });
        }, { threshold: 0.15 });

        cards.forEach((card, indice) => {
            card.style.transitionDelay = `${(indice % 3) * 120}ms`;
            observador.observe(card);
        });
    } else {
        cards.forEach((card) => card.classList.add('visivel'));
    }

    grade.querySelectorAll('img').forEach((img) => {
        const avisar = () => {
            console.warn('Imagem não encontrada:', img.getAttribute('src'));
            img.style.display = 'none';
        };

        if (img.complete && img.naturalWidth === 0) {
            avisar();
        } else {
            img.addEventListener('error', avisar);
        }
    });
}

document.addEventListener('DOMContentLoaded', async () => {
    const grade = document.querySelector('.cursos-grid');
    if (!grade) {
        console.warn('Elemento .cursos-grid não encontrado no HTML.');
        return;
    }

    if (grade.children.length === 0) {
        try {
            const params = new URLSearchParams(window.location.search);
            const categoria = params.get('categoria');
            const url = categoria
                ? `/api/cursos?categoria=${encodeURIComponent(categoria)}`
                : '/api/cursos';
            const resposta = await fetch(url);
            if (resposta.ok) {
                const dados = await resposta.json();
                (dados.cursos || []).forEach((curso) => grade.appendChild(criarCard(curso)));
            }
        } catch (erro) {
            console.warn('Falha ao buscar cursos na API:', erro);
        }
    }

    inicializarAnimacoesEImagens(grade);
});
