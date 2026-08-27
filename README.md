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

## Exemplos

Pergunta: Qual o seu objetivo profissional?
Resposta:  Meu objetivo profissional é desenvolver soluções inteligentes, centradas nas pessoas e orientadas pela inovação, utilizando tecnologia e Inteligência Artificial. Busco criar soluções inovadoras que gerem melhores resultados e contribuam para o crescimento e evolução das organizações e das pessoas.

### Objetivos Específicos
- Implementar uma arquitetura baseada em RAG
- Criar uma base de conhecimento estruturada em PDFs
- Permitir consultas em linguagem natural
- Minimizar alucinações limitando respostas ao conteúdo documental
- Fornecer canal de contato quando a informação não estiver disponível

---

## 📁 Estrutura do Projeto 
```bash
PortfolioAI/
│
├── README.md
├── requirements.txt
├── .gitignore
├── evidenciastreamlit.mp4
├── evidenciaOCI.mp4
│
├── src/
│   └── código Python
│
├── notebooks/
│   └── PortfolioAI_RAG.ipynb
│
├── docs/
│   ├── Guia_Mestre_Documentacao - PortfolioAI.pdf
│   ├── Project_Charter  - PortfolioAI.pdf
│   ├── Product_Vision - PortfolioAI.pdf
│   ├── Requisitos_SRS - PortfolioAI.pdf
│   ├── Arquitetura_da_Solucao - PortfolioAI.pdf
│   ├── Product_Backlog - PortfolioAI.pdf
│   ├── Mapa_Experiencia_Usuario - PortfolioAI.pdf
│   │
│   └── diagrams/
│       ├── arquitetura.png
│       ├── fluxo_rag.png
│       └── jornada_usuario.png
│
├── knowledge_base/
│   ├── curriculo.pdf
│   ├── projetos.pdf
│   ├── competencias_comportamentais.pdf
│   ├── competencias_tecnicas.pdf
│   ├── desenvolvimento_profissional_continuo.pdf
│   ├── formacao_academica.pdf
│   ├── perfil_profissional,pdf
│   ├── faq.pdf
│   └── trajetoria_profissional.pdf
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

✅ Incluído
- Assistente RAG completo
- Base de conhecimento em PDF
- Busca semântica com embeddings
- Respostas fundamentadas
- Tratamento elegante para perguntas sem resposta
- Interface Web responsiva
- Infraestrutura segura com protocolo HTTPS/SSL
- Gestão de domínio com DuckDNS (mascaramento de IP e persistência)

❌ Fora do Escopo
- Memória de conversação
- Integração com LinkedIn
- Multilingue
  
---

## 📈 Critérios de Sucesso
- Respostas corretas e fundamentadas
- Uso efetivo de recuperação semântica
- Baixa taxa de alucinações
- Excelente documentação

---

## 🛡️ Infraestrutura e Segurança
O PortfolioAI foi desenhado com foco em segurança de rede e disponibilidade:
- **Protocolo de Segurança:** Implementação de HTTPS para garantir a criptografia de ponta a ponta na comunicação.
- **Obfuscação de IP:** Utilização de Dynamic DNS (DuckDNS) para mascarar o IP real da instância, melhorando a segurança contra varreduras externas.
- **Camadas de Proteção:** Configuração de diretrizes de acesso e segurança na OCI para proteger o ambiente de execução contra acessos indevidos.

---

## 📄 Documentação Completa
- Project Charter
- Arquitetura da Solução
- Mapa de Experiência do Usuário

---
## 🚀 Deploy

- Streamlit Cloud : https://portfolioai-app.streamlit.app/

---

## 🎥 Demonstração do Projeto - Streamlit Cloud

[<video src="https://github.com/user-attachments/assets/controls width="100%"></video>](https://github.com/user-attachments/assets/00f81119-fb3c-4311-b53c-8430dfe24e14)

- OBS: Foi utilizado conta Oracle Cloud Free Tier podendo apresentar algumas limitações de uso após o prazo de teste.
---

- Oracle Cloud Infrastructure (OCI) : https://portifolioai.duckdns.org
  
---
## 🎥 Demonstração do Projeto - Oracle Cloud Infrastructure



[https://github.com/user-attachments/assets/e6963e44-0402-4ff6-928f-b728333c4206](https://github.com/user-attachments/assets/78bc1242-f06a-4613-b65a-cab3fb71c51e)


---
## 👤 Contato
Elisângela de Souza  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com)  
E-mail: elissouza@outlook.com.br

---

"O PortfolioAI não foi criado para responder perguntas. Foi criado para dar voz à trajetória profissional de uma pessoa por meio da Inteligência Artificial."




