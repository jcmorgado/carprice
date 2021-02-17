import pandas as pd
import streamlit as st

@st.cache
def get_data():
    df = pd.read_csv('https://raw.githubusercontent.com/jcmorgado/carprice/master/car.csv', sep=';')
    df = df.drop(columns=['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'])
    df = df[['Marca', 'Nome', 'Modelo', 'Ano', 'Faixa', 'Comb', 'Valor']]
    return df

def main():
    st.write('Preço de **CARROS** baseado em estimativa da Tabela FIP')
    st.sidebar.title("Selecione seu filtro")
    df = get_data()

    for column in df.columns:
        options = pd.Series(["Todos"]).append(df[column], ignore_index=True).unique()
        choice = st.sidebar.selectbox("Selectione o(a) {}:".format(column), options)

        if choice != "Todos":
            #df = df[df[column] == choice].drop(columns=column)
            df = df[df[column] == choice]
    st.write(df)


if __name__ == "__main__":
    main()