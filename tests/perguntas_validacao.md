# PortfolioAI – Perguntas de Validação

Este arquivo contém um conjunto de perguntas utilizadas para validar o comportamento do assistente RAG.
O objetivo é verificar se as respostas são **fundamentadas** no conteúdo documental, se o sistema **minimiza alucinações** e se trata adequadamente os casos em que a informação não está disponível.

---

## 1. Perguntas sobre Objetivo e Trajetória Profissional

| ID | Pergunta | Resultado Esperado |
|----|----------|--------------------|
| P01 | Qual o seu objetivo profissional? | Resposta alinhada ao conteúdo do currículo/documentação |
| P02 | Me fale sobre a sua trajetória profissional. | Resumo fundamentado nos documentos |
| P03 | Quais são as suas principais motivações profissionais? | Resposta baseada no conteúdo disponível |
| P04 | O que você busca em uma nova oportunidade? | Resposta fundamentada ou indicação de contato se não houver informação |

---

## 2. Perguntas sobre Projetos

| ID | Pergunta | Resultado Esperado |
|----|----------|--------------------|
| P05 | Quais projetos você já desenvolveu? | Lista ou descrição dos projetos presentes na base |
| P06 | Me conte sobre o projeto PortfolioAI. | Descrição técnica e objetivos do projeto |
| P07 | Qual foi o seu papel no desenvolvimento do PortfolioAI? | Resposta fundamentada no documento de projetos |
| P08 | Quais tecnologias foram utilizadas no PortfolioAI? | Python, LangChain, Groq, FAISS, RAG, Streamlit etc. |
| P09 | O PortfolioAI possui interface web? | Resposta baseada no escopo do MVP (Streamlit Cloud) |

---

## 3. Perguntas sobre Competências e Tecnologias

| ID | Pergunta | Resultado Esperado |
|----|----------|--------------------|
| P10 | Quais são as suas principais competências técnicas? | Lista fundamentada no documento de competências |
| P11 | Você tem experiência com Inteligência Artificial? | Resposta baseada na documentação |
| P12 | Quais ferramentas de IA Generativa você utiliza? | Resposta alinhada ao conteúdo (ex.: LangChain, Groq, Llama) |
| P13 | Você domina Python? | Resposta fundamentada |
| P14 | Tem experiência com RAG (Retrieval-Augmented Generation)? | Resposta positiva e fundamentada no projeto |

---

## 4. Perguntas sobre Experiência e Formação

| ID | Pergunta | Resultado Esperado |
|----|----------|--------------------|
| P15 | Qual a sua formação acadêmica? | Resposta baseada no currículo |
| P16 | Onde você trabalhou anteriormente? | Resposta fundamentada ou indicação de ausência de informação |
| P17 | Há quanto tempo você atua na área de tecnologia? | Resposta baseada nos documentos |
| P18 | Você possui certificações? | Resposta fundamentada ou canal de contato |

---

## 5. Perguntas sobre Contato e Disponibilidade

| ID | Pergunta | Resultado Esperado |
|----|----------|--------------------|
| P19 | Como posso entrar em contato com você? | E-mail e/ou LinkedIn conforme documento de contato |
| P20 | Qual o seu e-mail profissional? | elissouza@outlook.com.br (ou valor presente na base) |
| P21 | Você está aberta a novas oportunidades? | Resposta fundamentada ou indicação de contato |
| P22 | Qual o link do seu LinkedIn? | Link presente na documentação de contato |

---

## 6. Perguntas Fora do Escopo (Teste de Alucinação)

Estas perguntas **não devem** gerar respostas inventadas. O sistema deve informar que a informação não está disponível e oferecer canal de contato.

| ID | Pergunta | Resultado Esperado |
|----|----------|--------------------|
| P23 | Qual a sua idade? | Informação não disponível + canal de contato |
| P24 | Qual o seu salário atual? | Informação não disponível + canal de contato |
| P25 | Você tem filhos? | Informação não disponível + canal de contato |
| P26 | Qual o seu endereço residencial? | Informação não disponível + canal de contato |
| P27 | Me conte uma fofoca sobre você. | Informação não disponível / recusa educada |
| P28 | Qual time de futebol você torce? | Informação não disponível + canal de contato |

---

## 7. Perguntas Ambíguas ou Complexas

| ID | Pergunta | Resultado Esperado |
|----|----------|--------------------|
| P29 | Me explique o PortfolioAI de forma simples. | Explicação clara e fundamentada |
| P30 | Qual a diferença entre o PortfolioAI e um currículo tradicional? | Resposta comparativa baseada na visão do projeto |
| P31 | O sistema pode inventar informações? | Não. Respostas limitadas ao conteúdo documental |
| P32 | Como o PortfolioAI evita alucinações? | Explicação da arquitetura RAG e limitação ao contexto |
| P33 | Posso usar o PortfolioAI para outras pessoas? | Resposta baseada no escopo documentado |

---

## 8. Critérios de Avaliação

Para cada pergunta, avaliar:

| Critério | Descrição | Status |
|----------|-----------|--------|
| Fundamentação | A resposta está baseada no conteúdo dos PDFs? | ☐ |
| Precisão | A informação está correta em relação à documentação? | ☐ |
| Ausência de alucinação | O sistema não inventou dados? | ☐ |
| Tratamento de ausência | Quando não há informação, oferece canal de contato? | ☐ |
| Clareza | A resposta é objetiva e compreensível? | ☐ |
| Tom profissional | A linguagem é adequada para recrutadores e gestores? | ☐ |

---

## 9. Registro de Testes

| Data | Executor | Ambiente | Observações |
|------|----------|----------|-------------|
|      |          | Colab / Local / Streamlit | |
|      |          |          | |
|      |          |          | |

---

## 10. Observações Finais

- As respostas devem ser **exclusivamente** baseadas na base de conhecimento (`knowledge_base/`).
- Em caso de informação ausente, o assistente deve responder de forma elegante e direcionar para o contato.
- Este conjunto de perguntas deve ser reexecutado após qualquer alteração na base de conhecimento ou no prompt do sistema.

---

**PortfolioAI** – Validação de qualidade do assistente RAG  
Versão 1.0 (MVP) | Julho de 2026
