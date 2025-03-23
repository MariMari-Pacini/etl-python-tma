import streamlit as st
import pandas as pd
import plotly.express as px

# Título do dashboard
st.title('Análise de KPIs de Atendimento')

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Envie um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leitura do CSV
    df = pd.read_csv(uploaded_file)

    # Convertendo a coluna Tempo_Medio_Atendimento para timedelta
    df['Tempo_Medio_Atendimento'] = pd.to_timedelta(df['Tempo_Medio_Atendimento'])

    # Cálculos de KPIs
    tempo_medio_atendimento = df['Tempo_Medio_Atendimento'].mean()
    total_chamados = df['Chamado'].count()
    atendimentos_improcedentes = df['Improcedente'].sum()
    atendimentos_com_maior_protocolo = df['Mais_de_um_protocolo'].sum()

    # Convertendo o tempo médio para um formato mais legível (h:mm:ss)
    tempo_medio_formatado = str(tempo_medio_atendimento).split(' ')[-1]

    # Exibição dos dados
    st.write("### Amostra dos Dados")
    st.dataframe(df.head())

    # Exibição dos KPIs lado a lado
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Tempo Médio de Atendimento", value=tempo_medio_formatado)
    with col2:
        st.metric(label="Total de Chamados", value=total_chamados)
    with col3:
        st.metric(label="Atendimentos Improcedentes", value=atendimentos_improcedentes)
    with col4:
        st.metric(label="Atendimentos com Mais de um Protocolo", value=atendimentos_com_maior_protocolo)

    # Gráfico de distribuição de tempo de atendimento
    st.write("### Distribuição do Tempo de Atendimento")
    fig_tempo_atendimento = px.histogram(df, x="Tempo_Medio_Atendimento", nbins=30, title="Distribuição do Tempo de Atendimento")
    st.plotly_chart(fig_tempo_atendimento)

    # Gráfico de quantidade de chamados por assunto
    st.write("### Quantidade de Chamados por Assunto de Atendimento")
    chamados_por_assunto = df.groupby('Assunto_Atendimento').size().reset_index(name='Quantidade')
    fig_chamados_assunto = px.bar(chamados_por_assunto, x='Assunto_Atendimento', y='Quantidade', title="Chamados por Assunto de Atendimento")
    st.plotly_chart(fig_chamados_assunto)

    # Gráfico de barras para atendimentos improcedentes por categoria
    st.write("### Atendimentos Improcedentes por Categoria de Atendimento")
    improcedentes_por_categoria = df.groupby(['Assunto_Atendimento', 'Improcedente']).size().reset_index(name='Quantidade')

    # Gráfico de barras para "Sim" e "Não" (Improcedente)
    fig_improcedentes_categoria = px.bar(improcedentes_por_categoria, 
                                         x='Assunto_Atendimento', 
                                         y='Quantidade', 
                                         color='Improcedente', 
                                         title="Atendimentos Improcedentes por Categoria de Atendimento",
                                         labels={'Improcedente': 'Improcedente (Sim/Não)', 'Quantidade': 'Quantidade'})
    st.plotly_chart(fig_improcedentes_categoria)

    # Análise interativa por categoria (Assunto de Atendimento)
    st.subheader("🔍 Análise Interativa por Assunto de Atendimento")
    assuntos = df['Assunto_Atendimento'].unique().tolist()
    selected_assunto = st.selectbox("Selecione um Assunto para Análise", assuntos)

    # Filtrando os dados com o assunto selecionado
    df_selected_assunto = df[df['Assunto_Atendimento'] == selected_assunto]
    
    # Gráfico de Tempo Médio de Atendimento por ID de Chamado para o Assunto Selecionado
    fig_assunto = px.bar(df_selected_assunto, x='Chamado', y='Tempo_Medio_Atendimento', title=f"Tempo Médio de Atendimento para {selected_assunto}")
    st.plotly_chart(fig_assunto)

else:
    st.write("Por favor, envie um arquivo CSV para análise.")
