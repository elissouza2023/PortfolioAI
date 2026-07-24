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

# Remove menu padrão
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

</style>
""", unsafe_allow_html=True)

# Fundo azul

st.markdown("""
<style>

.stApp{

background-color:#0A3153;

}

</style>
""", unsafe_allow_html=True)

# Título

st.markdown("""
<h1 style="
text-align:center;
color:white;
font-size:36px;
margin-top:15px;
">

PortfolioAI

</h1>

""", unsafe_allow_html=True)

# Subtítulo

st.markdown("""

<p style="
text-align:center;
font-size:20px;
color:white;
margin-bottom:40px;
">

Transformando currículos em conversas inteligentes.

</p>

""", unsafe_allow_html=True)

# Layout

col1,col2,col3 = st.columns([1,2,1])

# Imagem

with col2:

    st.image(
        "assets/celular.png",
        width=350
    )
    
# container

with col2:

    st.image("assets/celular.png", width=350)

    pergunta = st.text_area(
        "Insira sua pergunta",
        height=90
    )

    if st.button("Enviar"):

        resposta = "Resposta do PortfolioAI aparecerá aqui."

    else:

        resposta = ""

    st.text_area(
        "Resposta",
        value=resposta,
        height=220
    )
    
    resposta = "Resposta do PortfolioAI aparecerá aqui."
    
    from backend.chat import perguntar

resposta = perguntar(pergunta)

# rodapé

st.markdown("""

<br><br><br>

<hr>

<p style="text-align:center;color:lightgray">

© PortfolioAI | 2026 | Elisângela de Souza

</p>

""", unsafe_allow_html=True)

