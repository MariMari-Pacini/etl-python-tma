import pandas as pd
import streamlit as st
from validador_dados import PlanilhaAtendimento
from pydantic import ValidationError

def validar_dados(df):
    erros = []
    dados_validados = []

    for index, row in df.iterrows():
        try:
            dados = row.to_dict()
            validado = PlanilhaAtendimento(**dados)
            dados_validados.append(validado)
        except ValidationError as e:
            erros.append(f"Erro na linha {index + 2}: {str(e)}")  # +2 para considerar o header

    return dados_validados, erros


def main():
    st.set_page_config(page_title="Validador de Atendimentos", layout="wide")
    st.title("📋 Validador de Dados de Atendimentos")
    st.write("Faça upload de um arquivo `.csv` para validar os dados")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, sep=",")
            st.success(f"Arquivo carregado com {len(df)} linhas")
            st.write("Visualização dos primeiros registros:")
            st.dataframe(df.head())

            if st.button("🔍 Validar Dados"):
                with st.spinner("Validando..."):
                    dados_validados, erros = validar_dados(df)

                    if erros:
                        st.error("⚠️ Foram encontrados erros:")
                        for erro in erros:
                            st.write(erro)
                    else:
                        st.success("✅ Todos os dados foram validados com sucesso!")

                    st.write(f"Total de registros válidos: {len(dados_validados)}")

                    if dados_validados:
                        df_validado = pd.DataFrame([item.dict() for item in dados_validados])
                        st.dataframe(df_validado)

                        st.download_button(
                            label="📥 Baixar dados validados",
                            data=df_validado.to_csv(index=False, sep=";"),
                            file_name="dados_validados.csv",
                            mime="text/csv"
                        )
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")

if __name__ == "__main__":
    main()