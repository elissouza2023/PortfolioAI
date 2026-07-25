import streamlit as st
import base64

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
# FUNÇÃO PARA CARREGAR IMAGEM EM BASE64
# -------------------------
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    fundo_base64 = get_base64_of_bin_file("assets/fundo.png")
    fundo_css = f'url("data:image/png;base64,{fundo_base64}")'
except Exception:
    fundo_css = "none"

# -------------------------
# CSS GLOBAL
# -------------------------
st.markdown(f"""
<style>
/* Remove elementos padrão do Streamlit */
#MainMenu {{visibility: hidden;}}
header {{visibility: hidden;}}
footer {{visibility: hidden;}}
.stDeployButton {{display: none;}}

/* Fundo principal */
.stApp {{
    background-color: #0A3153;
    background-image: {fundo_css};
    background-size: cover;
    background-position: center top;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Título */
.titulo-principal {{
    text-align: center;
    color: #FFFFFF !important;
    font-size: 1.55rem;
    font-weight: 500;
    margin-top: 0.8rem;
    margin-bottom: 0.15rem;
    letter-spacing: 0.3px;
    line-height: 1.35;
    text-shadow: 0 2px 6px rgba(0,0,0,0.45);
}}

/* Labels */
.label-card {{
    color: #FFFFFF;
    font-size: 0.92rem;
    font-weight: 500;
    margin-bottom: 10px;
    padding-left: 4px;
}}

/* ===== CARD AZUL (container) + CARD BRANCO (textarea) ===== */
div[data-testid="stTextArea"] {{
    background-color: rgba(11, 56, 95, 0.55) !important;
    border-radius: 18px !important;
    padding: 16px 16px 12px 16px !important;
    margin-bottom: 0 !important;
    backdrop-filter: blur(6px);
}}

/* O textarea em si (card branco) */
.stTextArea textarea {{
    color: #8E8E93 !important;
    font-size: 0.93rem !important;
    background-color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px !important;
}}

.stTextArea textarea::placeholder {{
    color: #8E8E93 !important;
    opacity: 0.85;
}}

/* Botão Enviar (agora dentro do card) */
div.stButton > button {{
    background-color: #FFFFFF !important;
    color: #0B385F !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.4rem 1.4rem !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.18);
    margin-top: 8px !important;
}}

div.stButton > button:hover {{
    background-color: #E8F0F8 !important;
    color: #0B385F !important;
}}

/* Rodapé fixo */
.rodape {{
    background-color: #D9D9D9;
    color: #081623;
    text-align: center;
    padding: 12px 0;
    font-size: 0.88rem;
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 999;
    box-shadow: 0 -2px 8px rgba(0,0,0,0.15);
}}

/* Espaçamento geral */
.block-container {{
    padding-top: 0.6rem !important;
    padding-bottom: 70px !important;
    max-width: 1050px;
}}
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
col_esq, col_centro, col_dir = st.columns([1.3, 1.4, 1.3])

with col_centro:
    st.image("assets/celular.png", use_container_width=True)

st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

# -------------------------
# ÁREA DE PERGUNTA E RESPOSTA
# -------------------------
col_pergunta, col_resposta = st.columns(2, gap="large")

# =========================================================
# CARD DA PERGUNTA
# =========================================================
with col_pergunta:
    st.markdown('<div class="label-card">Faça sua pergunta</div>', unsafe_allow_html=True)

    # Text area (card azul + branco)
    pergunta = st.text_area(
        label="pergunta",
        height=145,
        placeholder="Digite aqui sua pergunta que o assistente consultará a base de dados.",
        label_visibility="collapsed",
        key="input_pergunta"
    )

    # Botão DENTRO do card azul (alinhado à direita)
    btn_col1, btn_col2 = st.columns([3, 1])
    with btn_col2:
        enviar = st.button("Enviar", use_container_width=True)

# =========================================================
# CARD DA RESPOSTA
# =========================================================
with col_resposta:
    st.markdown('<div class="label-card">&nbsp;</div>', unsafe_allow_html=True)

    if "resposta" not in st.session_state:
        st.session_state.resposta = ""

    if enviar and pergunta.strip():
        try:
            from backend.chat import perguntar
            with st.spinner("Consultando a base de conhecimento..."):
                st.session_state.resposta = perguntar(pergunta)
        except Exception:
            st.session_state.resposta = (
                "Desculpe, não encontrei resposta a sua pergunta. "
                "Tente novamente ou entre em contato: elissouza@outlook.com.br"
            )
    elif enviar and not pergunta.strip():
        st.session_state.resposta = "Por favor, digite uma pergunta."

    st.text_area(
        label="resposta",
        value=st.session_state.resposta if st.session_state.resposta else "",
        height=185,
        placeholder="A resposta do Portfolio AI aparecerá aqui. Faça sua pergunta",
        label_visibility="collapsed",
        disabled=True,
        key="output_resposta"
    )

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