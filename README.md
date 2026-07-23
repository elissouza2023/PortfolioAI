<div align="center">

# PortfolioAI – Assistente Inteligente de Portfólio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00A36C?style=for-the-badge&logo=groq&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-000000?style=for-the-badge&logo=faiss&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-orange?style=for-the-badge)

**Versão:** 1.0 (MVP)  
**Data:** Julho de 2026

![GitHub repo size](https://img.shields.io/github/repo-size/seuusuario/PortfolioAI)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

<br>

O **PortfolioAI** é um assistente inteligente baseado em **RAG (Retrieval-Augmented Generation)** que transforma seu currículo e portfólio profissional em uma experiência conversacional inteligente.

---

## 📋 Visão do Projeto

Ao invés de navegar por diversos documentos estáticos, recrutadores, gestores, professores e visitantes podem realizar **perguntas em linguagem natural** e obter respostas precisas baseadas exclusivamente na sua documentação oficial.

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

---

## 📁 Estrutura do Projeto (em elaboração)

```bash
PortfolioAI/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── código Python
│
├── notebooks/
│   └── PortfolioAI_RAG.ipynb
│
├── docs/
│   ├── Arquitetura da Solução - PortfolioAI.pdf
│   ├── Especificação de Requisitos de Software - PortfolioAI.pdf
│   ├── Guia Mestre da Documentação - PortfolioAI.pdf
│   ├── Mapa da Experiência do Usuário  - PortfolioAI.pdf
│   ├── PortfolioAI Vision - PortfolioAI.pdf
│   ├── Product Backlog - PortfolioAI.pdf
│   ├── PROJECT CHARTER - Projeto PortfolioAI.pdf
│   │
│   └── diagrams/
│       ├── arquitetura.png
│       ├── fluxo_rag.png
│       └── jornada_usuario.png
│
├── knowledge_base/
│   ├── curriculo.pdf
│   ├── projetos.pdf
│   ├── competencias.pdf
│   ├── faq.pdf
│   └── contato.pdf
│
├── vector_store/
│   └── FAISS/
│
└── tests/
    └── perguntas_validacao.md

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

---

## ✨ Funcionalidades do MVP

### ✅ Incluído
- Assistente RAG completo
- Base de conhecimento em PDF
- Busca semântica com embeddings
- Respostas fundamentadas
- Tratamento elegante para perguntas sem resposta

### ❌ Fora do Escopo
- Memória de conversação
- Interface web
- Integração com LinkedIn
- Suporte multilíngue

---

## 📈 Critérios de Sucesso
- Respostas corretas e fundamentadas
- Uso efetivo de recuperação semântica
- Baixa taxa de alucinações
- Excelente documentação

---

## 📄 Documentação Completa
- Project Charter
- Arquitetura da Solução
- Mapa de Experiência do Usuário

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



