# backend/chat.py
import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# -------------------------------------------------
# Caminhos
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_PATH = BASE_DIR / "knowledge_base"
VECTOR_PATH = BASE_DIR / "vector_store"

# -------------------------------------------------
# Embeddings (mesmo modelo do Colab)
# -------------------------------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------------------------------
# Carrega ou cria o Vector Store
# -------------------------------------------------
def get_vector_store():
    index_faiss = VECTOR_PATH / "index.faiss"
    index_pkl = VECTOR_PATH / "index.pkl"

    if index_faiss.exists() and index_pkl.exists():
        # Carrega o índice já criado no Colab
        vector_store = FAISS.load_local(
            str(VECTOR_PATH),
            embeddings,
            allow_dangerous_deserialization=True
        )
        print("✅ Vector Store carregado do disco.")
    else:
        # Se não existir, cria a partir dos PDFs
        print("⚠️  Vector Store não encontrado. Criando a partir dos PDFs...")
        VECTOR_PATH.mkdir(parents=True, exist_ok=True)

        loader = PyPDFDirectoryLoader(str(KNOWLEDGE_PATH))
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=900,
            chunk_overlap=150,
            separators=["\n\n", "\n", ".", "!", "?", " "]
        )
        texts = text_splitter.split_documents(documents)

        vector_store = FAISS.from_documents(texts, embeddings)
        vector_store.save_local(str(VECTOR_PATH))
        print("✅ Vector Store criado e salvo.")

    return vector_store

# -------------------------------------------------
# LLM + Prompt + Chain
# -------------------------------------------------
def get_rag_chain():
    # API Key (prioriza variável de ambiente ou Streamlit secrets)
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GROQ_API_KEY")
        except Exception:
            pass

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY não encontrada. "
            "Configure a variável de ambiente ou o arquivo .streamlit/secrets.toml"
        )

    os.environ["GROQ_API_KEY"] = api_key

    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.2,
        max_tokens=1200
    )

    system_prompt = """
Você é o PortfolioAI.
Seu objetivo é responder perguntas sobre Elisângela de Souza.

REGRAS IMPORTANTES:
• Utilize EXCLUSIVAMENTE as informações presentes no contexto.
• Nunca invente experiências.
• Nunca complete informações por conta própria.
• Caso não exista resposta no contexto, diga exatamente:
"Não encontrei essa informação na minha base de conhecimento.
Caso deseje mais detalhes, recomendo entrar em contato diretamente com Elisângela."

• Sempre escreva de forma profissional, porém em primeira pessoa, como em uma entrevista.
  Exemplo: "Sou uma profissional..."
• Mantenha raciocínio fluido, linguagem clara e tom entusiasmado.
• Sempre responda em português.
• Quando possível organize a resposta em tópicos.

Contexto:
{context}
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 6})

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain

# -------------------------------------------------
# Cache da chain (importante para performance no Streamlit)
# -------------------------------------------------
_rag_chain = None

def _get_chain():
    global _rag_chain
    if _rag_chain is None:
        _rag_chain = get_rag_chain()
    return _rag_chain

# -------------------------------------------------
# Função principal usada pelo app.py
# -------------------------------------------------
def perguntar(pergunta: str) -> str:
    """
    Recebe a pergunta do usuário e retorna a resposta do PortfolioAI.
    """
    if not pergunta or not pergunta.strip():
        return "Por favor, digite uma pergunta."

    try:
        chain = _get_chain()
        resultado = chain.invoke({"input": pergunta.strip()})
        return resultado["answer"]
    except Exception as e:
        return (
            "Desculpe, ocorreu um erro ao processar sua pergunta. "
            "Tente novamente ou entre em contato: elissouza@outlook.com.br"
        )