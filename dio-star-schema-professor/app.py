import streamlit as st
import pandas as pd

st.set_page_config(page_title="Star Schema Professor", layout="wide")

st.title("🎓 Modelagem Dimensional: Star Schema (Professor)")
st.markdown("Este projeto demonstra a conversão de um modelo relacional para um **Esquema em Estrela** focado na análise do corpo docente.")

# --- CRIAÇÃO DAS TABELAS (DIMENSÕES) ---
dim_professor = pd.DataFrame({
    'ID_Professor': [1, 2, 3],
    'Nome': ['Ricardo Arona', 'Júlia Costa', 'Paulo Freire'],
    'Titulação': ['Doutor', 'Mestre', 'Doutor']
})

dim_curso = pd.DataFrame({
    'ID_Curso': [10, 20, 30],
    'Nome_Curso': ['Computação', 'Eng. Dados', 'Pedagogia']
})

dim_data = pd.DataFrame({
    'ID_Data': [1, 2],
    'Semestre': ['1º Semestre 2024', '2º Semestre 2024']
})

# --- TABELA FATO (O CENTRO DA ESTRELA) ---
fato_professor = pd.DataFrame({
    'ID_Fato': [101, 102, 103],
    'ID_Professor': [1, 2, 3],
    'ID_Curso': [10, 20, 30],
    'ID_Data': [1, 1, 2],
    'Carga_Horaria': [60, 40, 45] # Métrica
})

# --- INTERFACE ---
st.header("📌 Estrutura do Modelo Estrela")
tab1, tab2 = st.tabs(["📊 Visualização das Tabelas", "🔍 Análise Combinada"])

with tab1:
    st.subheader("Tabela Fato (Métricas)")
    st.dataframe(fato_professor, use_container_width=True)
    
    st.subheader("Dimensões (Atributos)")
    c1, c2, c3 = st.columns(3)
    c1.write("**Professores**"); c1.table(dim_professor)
    c2.write("**Cursos**"); c2.table(dim_curso)
    c3.write("**Calendário**"); c3.table(dim_data)

with tab2:
    st.subheader("Relatório Gerado via Star Schema")
    # Realizando o Join (Relacionamento)
    df_final = fato_professor.merge(dim_professor, on='ID_Professor').merge(dim_curso, on='ID_Curso')
    st.table(df_final[['Nome', 'Nome_Curso', 'Carga_Horaria']])

st.info("**Nota de Entrega:** Os dados de alunos foram excluídos conforme os requisitos do desafio para focar estritamente na análise de produtividade dos professores.")