<div align="center">

# PortfolioAI – Assistente Inteligente de Portfólio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00A36C?style=for-the-badge&logo=groq&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-000000?style=for-the-badge&logo=faiss&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-orange?style=for-the-badge)

**Versão:** 1.0 (MVP)  
**Data:** Julho de 2026

</div>

<br>

O **PortfolioAI** é um assistente inteligente baseado em **RAG (Retrieval-Augmented Generation)** que transforma o currículo e o portfólio profissional em uma experiência conversacional inteligente.

---

## 📋 Visão do Projeto

Ao invés de navegar por diversos documentos estáticos, recrutadores, gestores, professores e visitantes podem realizar **perguntas em linguagem natural** e obter respostas precisas baseadas exclusivamente na documentação oficial.

---

## 🎯 Objetivos

### Objetivo Geral
Desenvolver um agente inteligente capaz de responder perguntas sobre a trajetória profissional utilizando IA Generativa e arquitetura RAG.

### Objetivos Específicos
- Implementar uma arquitetura baseada em RAG
- Criar uma base de conhecimento estruturada em PDFs
- Permitir consultas em linguagem natural
- Minimizar alucinações limitando respostas ao conteúdo documental
- Fornecer canal de contato quando a informação não estiver disponível
- Disponibilizar interface web interativa

---

## 📁 Estrutura do Projeto

```bash
PortfolioAI/
├── app.py                      # Interface Streamlit
├── requirements.txt
├── .gitignore
├── README.md
│
├── backend/
│   └── chat.py                 # Lógica do RAG
│
├── assets/
│   ├── celular.png
│   └── fundo.png
│
├── knowledge_base/             # Base de conhecimento (PDFs)
│
├── vector_store/               # Índice FAISS
│   ├── index.faiss
│   └── index.pkl
│
├── notebooks/
│   └── PortfolioAI_RAG.ipynb   # Desenvolvimento e testes do RAG
│
└── docs/                       # Documentação do projeto
```



---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.10+
- Conta no Groq (para acesso ao Llama)

### 1. Clone o repositório
git clone 
cd PortfolioAI


### 2. Instale as dependências
pip install -r requirements.txt


### 3. Execute o notebook
Abra o `notebooks/PortfolioAI_RAG.ipynb` no Google Colab ou no Jupyter Notebook.



### 4. Configure a chave da Groq
Crie o arquivo .streamlit/secrets.toml na raiz do projeto:
GROQ_API_KEY = "sua_chave_aqui"


### 5. Execute a aplicação
streamlit run app.py

---

## ✨ Funcionalidades do MVP

✅ Incluído

- Interface web interativa (Streamlit)
= Assistente RAG completo
- Base de conhecimento em PDF
- Busca semântica com embeddings (FAISS + sentence-transformers)
- Respostas fundamentadas e em primeira pessoa
- Tratamento elegante para perguntas sem resposta
- Design responsivo e personalizado

---

### ❌ Fora do Escopo
- Memória de conversação
- Interface web
- Integração com LinkedIn
- Suporte multilíngue
- Autenticação de usuários
  
---

## 📈 Critérios de Sucesso
- Respostas corretas e fundamentadas
- Uso efetivo de recuperação semântica
- Baixa taxa de alucinações
- Interface intuitiva e profissional
- Documentação completaão

---

## 📄 Documentação Completa

- Project Charter
- Arquitetura da Solução
- Mapa de Experiência do Usuário
- Product Backlog
- Especificação de Requisitos

  
---

## 🔮 Visão de Futuro
- Interface web interativa
- Memória conversacional
- Múltiplos idiomas
- Integrações externas

---

## 👤 Contato
Elisângela de Souza  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com)  
E-mail: elissouza@outlook.com.br

---

Feito com ❤️ utilizando Python, LangChain e RAG



