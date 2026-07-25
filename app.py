import streamlit as st

# -------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------
st.set_page_config(
    page_title="PortfolioAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------
# CSS GLOBAL
# -------------------------
st.markdown("""
<style>
/* Remove elementos padrão do Streamlit */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display: none;}

/* Fundo principal */
.stApp {
    background-color: #0A3153;
    background-image: radial-gradient(circle at 20% 50%, rgba(11, 56, 95, 0.4) 0%, transparent 50%),
                      radial-gradient(circle at 80% 20%, rgba(11, 56, 95, 0.3) 0%, transparent 40%);
}

/* Título */
.titulo-principal {
    text-align: center;
    color: #FFFFFF;
    font-size: 2.1rem;
    font-weight: 500;
    margin-top: 1.2rem;
    margin-bottom: 0.3rem;
    letter-spacing: 0.5px;
}

/* Subtítulo */
.subtitulo {
    text-align: center;
    color: #FFFFFF;
    font-size: 1.15rem;
    margin-bottom: 1.8rem;
    opacity: 0.95;
}

/* Container dos cards inferiores (azul 50% transparente) */
.card-azul {
    background-color: rgba(11, 56, 95, 0.5);
    border-radius: 18px;
    padding: 18px 18px 14px 18px;
    margin-bottom: 10px;
}

/* Card branco interno */
.card-branco {
    background-color: #FFFFFF;
    border-radius: 14px;
    padding: 14px 16px;
    min-height: 140px;
}

/* Labels dos cards */
.label-card {
    color: #FFFFFF;
    font-size: 0.95rem;
    font-weight: 500;
    margin-bottom: 8px;
    padding-left: 4px;
}

/* Placeholder e texto interno dos text_area */
.stTextArea textarea {
    color: #8E8E93 !important;
    font-size: 0.95rem !important;
    background-color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
}

.stTextArea textarea::placeholder {
    color: #8E8E93 !important;
    opacity: 0.85;
}

/* Botão Enviar */
div.stButton > button {
    background-color: #FFFFFF;
    color: #0B385F;
    border: none;
    border-radius: 10px;
    padding: 0.45rem 1.4rem;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background-color: #E8F0F8;
    color: #0B385F;
    border: none;
}

/* Rodapé */
.rodape {
    background-color: #D9D9D9;
    color: #081623;
    text-align: center;
    padding: 12px 0;
    font-size: 0.9rem;
    margin-top: 2.5rem;
    border-radius: 0;
    width: 100%;
}

/* Ajustes de espaçamento */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0 !important;
    max-width: 1100px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# TÍTULO
# -------------------------
st.markdown(
    '<h1 class="titulo-principal">PortfolioAI – Transformando currículos em conversas inteligentes.</h1>',
    unsafe_allow_html=True
)

# -------------------------
# IMAGEM CENTRAL (celular)
# -------------------------
col_esq, col_centro, col_dir = st.columns([1.2, 1.6, 1.2])

with col_centro:
    st.image("assets/celular.png", use_container_width=True)

# Espaço pequeno após a imagem
st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

# -------------------------
# ÁREA DE PERGUNTA E RESPOSTA (dois cards)
# -------------------------
col_pergunta, col_resposta = st.columns(2, gap="medium")

# ---- Card da Pergunta ----
with col_pergunta:
    st.markdown('<div class="label-card">Faça sua pergunta</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-azul">', unsafe_allow_html=True)

    pergunta = st.text_area(
        label="pergunta",
        height=130,
        placeholder="Digite aqui sua pergunta que o assistente consultará a base de dados.",
        label_visibility="collapsed",
        key="input_pergunta"
    )

    # Botão alinhado à direita
    btn_col1, btn_col2 = st.columns([3, 1])
    with btn_col2:
        enviar = st.button("Enviar", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---- Card da Resposta ----
with col_resposta:
    st.markdown('<div class="label-card">&nbsp;</div>', unsafe_allow_html=True)  # alinhamento visual

    st.markdown('<div class="card-azul">', unsafe_allow_html=True)

    # Inicializa session_state
    if "resposta" not in st.session_state:
        st.session_state.resposta = ""

    # Lógica de envio
    if enviar and pergunta.strip():
        try:
            from backend.chat import perguntar
            with st.spinner("Consultando a base de conhecimento..."):
                st.session_state.resposta = perguntar(pergunta)
        except Exception as e:
            st.session_state.resposta = (
                "Desculpe, ocorreu um erro ao processar sua pergunta. "
                "Tente novamente ou entre em contato: elissouza@outlook.com.br"
            )
    elif enviar and not pergunta.strip():
        st.session_state.resposta = "Por favor, digite uma pergunta."

    st.text_area(
        label="resposta",
        value=st.session_state.resposta if st.session_state.resposta else "",
        height=160,
        placeholder="A resposta do Portfolio AI aparecerá aqui. Faça sua pergunta",
        label_visibility="collapsed",
        disabled=True,
        key="output_resposta"
    )

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# RODAPÉ
# -------------------------
st.markdown(
    """
    <div class="rodape">
        © PortfolioAI | 2026 | Elisângela de Souza
    </div>
    """,
    unsafe_allow_html=True
)