# 🎓 Desafio de Modelagem Dimensional - Star Schema Professor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dio-star-schema-profe.streamlit.app/)

Este repositório contém a resolução do desafio de modelagem dimensional da formação **Power BI Analyst** da [DIO](https://www.dio.me/). O objetivo foi converter um diagrama relacional de uma universidade em um **Esquema em Estrela (Star Schema)** focado na análise dos professores.

## 🔗 Link para Visualização
Acompanhe o modelo em execução aqui: [https://dio-star-schema-profe.streamlit.app/](https://dio-star-schema-profe.streamlit.app/)

---

## 📌 Estrutura do Modelo Estrela

O foco da análise é o **Professor**. Por isso, a tabela fato centraliza métricas de carga horária e chaves para as dimensões que dão contexto à análise acadêmica.

### 1. Tabela Fato
- **`Fato_Professor`**: Centraliza os IDs das dimensões e a métrica `Carga_Horaria`. Cada linha representa uma disciplina ministrada por um professor em um período específico.

### 2. Tabelas Dimensão
- **`Dim_Professor`**: Dados detalhados do corpo docente (Nome, Titulação, Especialidade).
- **`Dim_Curso`**: Informações sobre os cursos (Nome, Departamento).
- **`Dim_Disciplina`**: Detalhes das matérias (Nome, Créditos).
- **`Dim_Data`**: Dimensão temporal criada para suprir a ausência de datas no modelo original, permitindo análises por **Ano** e **Semestre**.

---

## 🛠️ Decisões Técnicas
- **Exclusão de Alunos**: Conforme os requisitos do desafio, os dados de alunos não foram incluídos para manter o foco estrito na produtividade e alocação dos professores.
- **Implementação com Streamlit**: Optei por utilizar **Python e Streamlit** para demonstrar como a modelagem dimensional facilita a realização de junções (joins) e a geração de relatórios de BI via código.

## 🚀 Tecnologias
- **Python**
- **Pandas** (Para simulação e relacionamento das tabelas)
- **Streamlit** (Para a interface visual do modelo)

---
Desenvolvido por [Seu Nome] durante a Formação Power BI Analyst.
