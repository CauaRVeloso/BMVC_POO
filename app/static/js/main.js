const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

function fecharMenu() {
    if (!menuToggle || !navLinks) return;

    navLinks.classList.remove('active');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', 'Abrir menu');
}

if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
        const menuAberto = navLinks.classList.toggle('active');

        menuToggle.setAttribute('aria-expanded', String(menuAberto));
        menuToggle.setAttribute(
            'aria-label',
            menuAberto ? 'Fechar menu' : 'Abrir menu'
        );
    });

    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', fecharMenu);
    });

    // Fecha o menu se a tela passar para o tamanho de computador.
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            fecharMenu();
        }
    });
}

const formContato = document.getElementById('formContato');
const progressText = document.querySelector('.progress-section p');
const progressFill = document.querySelector('.progress-bar-fill');
const formFeedback = document.getElementById('formFeedback');

const progressStates = [
    { text: "Vamos ver até onde você chega!", width: "25%" },
    { text: "Está indo bem!", width: "50%" },
    { text: "Muito bom!", width: "75%" },
    { text: "Continue! Quase lá...", width: "90%" },
    { text: "Parabéns! Bem-vindo ao seu Futuro!", width: "100%" }
];

function exibirFeedback(mensagem, tipo) {
    if (!formFeedback) return;
    formFeedback.textContent = mensagem;
    formFeedback.className = `form-feedback ${tipo}`;
    formFeedback.hidden = false;
}

if (formContato && progressText && progressFill) {
    const inputs = Array.from(formContato.querySelectorAll('input'));

    function atualizarProgresso() {
        let camposPreenchidos = 0;

        inputs.forEach(input => {
            if (input.value.trim() !== '') {
                camposPreenchidos++;
            }
        });

        const indice = Math.min(
            camposPreenchidos,
            progressStates.length - 1
        );

        progressText.textContent = progressStates[indice].text;
        progressFill.style.width = progressStates[indice].width;
    }

    inputs.forEach((input, index) => {
        input.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();

                atualizarProgresso();

                if (index < inputs.length - 1) {
                    inputs[index + 1].focus();
                } else {
                    const botaoEnviar = formContato.querySelector(
                        'button[type="submit"], button:not([type])'
                    );

                    if (botaoEnviar) {
                        botaoEnviar.focus();
                    }
                }
            }
        });

        input.addEventListener('input', atualizarProgresso);
    });

    formContato.addEventListener('submit', async function(event) {
        event.preventDefault();

        const nomeInput = formContato.querySelector('input[name="nome"]');
        const emailInput = formContato.querySelector('input[name="email"]');
        const telefoneInput = formContato.querySelector('input[name="telefone"]');

        const payload = {
            nome: nomeInput ? nomeInput.value.trim() : '',
            email: emailInput ? emailInput.value.trim() : '',
            telefone: telefoneInput ? telefoneInput.value.trim() : ''
        };

        try {
            const resposta = await fetch('/api/contatos', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            const dados = await resposta.json();

            if (!resposta.ok) {
                exibirFeedback(
                    dados.message || 'Não foi possível enviar sua mensagem.',
                    'erro'
                );
                return;
            }

            progressText.textContent = progressStates[4].text;
            progressFill.style.width = progressStates[4].width;
            exibirFeedback(
                dados.message || 'Mensagem enviada com sucesso!',
                'sucesso'
            );

            setTimeout(() => {
                formContato.reset();
                atualizarProgresso();
            }, 1000);
        } catch (_erro) {
            exibirFeedback('Erro ao conectar com o servidor. Tente novamente.', 'erro');
        }
    });

    atualizarProgresso();
}
