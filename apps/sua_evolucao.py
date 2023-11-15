import streamlit as st
import pandas as pd
from data.create_data import create_pica_pau, create_df_grade_horas, create_df_bacharelado_ciencia_tecnologia, create_df_grade_horas, create_df_bacharelado_ciencia_tecnologia, create_df_eng_gestao, create_df_eng_gestao_plano, create_df_bacharelado_biologia, create_df_bacharelado_biotecnologia, create_df_bacharelado_fisica, create_df_bacharelado_matematica, create_df_bacharelado_neuro, create_df_bacharelado_quimica, create_df_engenharia_aeroespacial, create_df_engenharia_ambiental, create_df_engenharia_energia, create_df_engenharia_materiais 
import base64

def download_button(df_selected):
    # Show a download button
    if not df_selected.empty:
        df_selected = df_selected[df_selected['Escolhas'] == True]
        csv = df_selected.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        # href = f'<a href="data:file/csv;base64,{b64}" download="selected_rows.csv">Download das linhas selecionadas</a>'
        # st.markdown(href, unsafe_allow_html=True)
        # Estilos do botão
                # Função para aplicar estilos por meio de JavaScript
        def set_css_style():
            style = """
                .botao-bonito {
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #FFFFFF; /* Cor de fundo */
                    color: #000000; /* Cor do texto */
                    text-decoration: none; /* Remover sublinhado padrão do link */
                    font-size: 16px;
                    border-radius: 5px;
                    border: none;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    transition: background-color 0.3s, transform 0.2s;
                }

                .botao-bonito:hover {
                    background-color: #d3d3d3; /* Cor de fundo alterada */
                    transform: translateY(-2px); /* Efeito de levantamento */
                    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
                }

                .botao-bonito:active {
                    background-color: #a9a9a9; /* Cor de fundo alterada novamente */
                    transform: translateY(0); /* Reset do efeito de levantamento */
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
            """
            return f"<style>{style}</style>"

        # Aplicar os estilos através de JavaScript
        st.markdown(set_css_style(), unsafe_allow_html=True)

        # Criar o botão utilizando a classe CSS personalizada
        href = f'<a href="data:file/csv;base64,{b64}" download="selected_rows.csv" class="botao-bonito">Download das linhas selecionadas</a>'
        st.markdown(href, unsafe_allow_html=True)

        
def materias(df_materias,df_materias_aprovadas,df_materias_plano=pd.DataFrame()):

    # df_materias_realizadas = df_materias[df_materias['codigo'].isin(df_materias_aprovadas['codigo'])].copy().reset_index(drop=True)
    df_materias_realizadas = df_materias_aprovadas[df_materias_aprovadas['codigo'].isin(df_materias['codigo'])].copy().reset_index(drop=True)

    df_materias_realizadas_graph = df_materias_realizadas.copy()
    df_materias_realizadas_graph["quadrimestre"] = df_materias_realizadas["ano"].astype(str) + "." + df_materias_realizadas["periodo"].astype(str).str.zfill(2)
    df_materias_realizadas_graph = df_materias_realizadas_graph[["quadrimestre", "creditos"]]

    if not df_materias_realizadas_graph.empty:
        tab1, tab2 = st.tabs(["Créditos x Quadrimestres", "Detalhes"])
        tab1.bar_chart(df_materias_realizadas_graph, x="quadrimestre", y="creditos")
        tab2.write(df_materias_realizadas.set_index('codigo'))
    else:
        st.title("Essa não! Você ainda não realizou nenhuma matéria desse pós-BI.")
        st.image(create_pica_pau(), width=700)


    if not df_materias_plano.empty:    
        df_materias_plano["quad"] = df_materias_plano["quad"].astype(str).replace(",", "")
        df_materias_plano         = df_materias_plano[~df_materias_plano["quad"].isin(["2023.01", "2023.02"])]
        df_materias_plano         = df_materias_plano[~df_materias_plano["codigo"].isin(df_materias_aprovadas["codigo"])]
        df_materias_plano         = df_materias_plano.reset_index(drop=True)

        st.write("##### Crie sua própria lista de tarefas")
        st.write("Selecione suas próximas matérias e tenha em mãos o que lhe ajudará na próxima matrícula")
        df_with_checkbox = df_materias_plano.copy()
        df_with_checkbox['Escolhas'] = False
        df_with_checkbox = df_with_checkbox[['Escolhas', 'quad', 'periodo', 'horario', 'dia_sem', 'codigo', 'disciplina']]
        df_selected = st.data_editor(
            df_with_checkbox,
            hide_index=True
        )

        download_button(df_selected)


def app():
    st.title('Sua evolução')

    materias_ja_desenvolvidas = ["", "Engenharia de Gestão","Bacharelado de Biotecnologia"]

    uploaded_file = st.file_uploader(label="Colete o arquivo do seu portal do aluno em formato json e suba aqui.")
    
    if uploaded_file is not None:
        # Can be used wherevern a "file-like" object is accepted:
        
        df_ficha = pd.read_json(uploaded_file)
        df_ficha["ano"] = df_ficha["ano"].astype(str).replace(",", "")
        df_ficha.sort_values(by=["ano","periodo"], inplace=True)
        df_bacharelado_ciencia_tecnologia = create_df_bacharelado_ciencia_tecnologia()
        
        df_grade_horas = create_df_grade_horas()
        grade_soma_creditos_total = df_grade_horas[df_grade_horas["categoria"] == "Carga horária total do curso"]["creditos"].sum()
        
        df_materias_aprovadas = df_ficha[df_ficha["situacao"] == "Aprovado"].copy()

        ficha_soma_creditos_total = df_materias_aprovadas['creditos'].sum()
        
        diferenca = grade_soma_creditos_total - ficha_soma_creditos_total
        
        percentual_progresso = round((ficha_soma_creditos_total / grade_soma_creditos_total), 3)
        
        df_visao_historica = df_ficha[["ano", "periodo", "creditos"]].copy()
        df_visao_historica = df_visao_historica.groupby(by=["ano", "periodo"], as_index=False).sum()
        df_visao_historica["quadrimestre"] = df_visao_historica["ano"].astype(str) + "." + df_visao_historica["periodo"].astype(str).str.zfill(2)
        df_visao_historica = df_visao_historica[["quadrimestre", "creditos"]]
        
        df_materias_faltantes = df_bacharelado_ciencia_tecnologia[~df_bacharelado_ciencia_tecnologia['codigo'].isin(df_materias_aprovadas['codigo'])].copy()

        ficha_conceitoxcreditos = 0
        dict_conceitos = {
            "A": 4,
            "B": 3,
            "C": 2,
            "D": 1,
            "F": 0,
            "O": 0
        }

        # Mapear os valores de "conceito" para os valores numéricos correspondentes
        df_ficha['conceito_num'] = df_ficha['conceito'].map(dict_conceitos)

        # Calcular a média ponderada
        cr = round((df_ficha['creditos'] * df_ficha['conceito_num']).sum() / df_ficha['creditos'].sum(), 3)
        
        st.write("### Bacharelado em Ciência e Tecnologia")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Coeficiente de progressão (CP)", percentual_progresso)
        col2.metric("Coeficiente de Rendimento (CR)", cr)
        col3.metric("Total de créditos realizados", ficha_soma_creditos_total)
        col4.metric("Quantos créditos faltam", diferenca)

   
        tab1, tab2, tab3 = st.tabs(["Créditos x Quadrimestres", "Detalhes", "Matérias que ainda podem ser realizadas"])
        tab1.bar_chart(df_visao_historica, x="quadrimestre", y="creditos")
        tab2.dataframe(df_ficha.set_index('codigo'))
        tab3.write(df_materias_faltantes.set_index('codigo'))
        
        st.write("### Análise Pós-BI")

        option = st.selectbox(
            '',
            (
                "",
                "Engenharia de Gestão",
                "Bacharelado de Biotecnologia",
                "Bacharelado de Ciência da Computação"#,
                # "Bacharelado de Ciências Biológicas",
                # "Bacharelado de Física",
                # "Bacharelado de Matemática",
                # "Bacharelado de Química",
                # "Bacharelado de Neurociência",
                # "Engenharia de Ambiental e Urbana",
                # "Engenharia de Energia",
                # "Engenharia de Informação",
                # "Engenharia de Instrumentação Automação e Robótica",
                # "Engenharia de Materiais",
                # "Engenharia de Aeroespacial",
                # "Engenharia de Biomédica"
            ))
        

        if option in materias_ja_desenvolvidas:
            if option == "Engenharia de Gestão":
                materias(create_df_eng_gestao(),df_materias_aprovadas,create_df_eng_gestao_plano())
            elif option == "Bacharelado de Biotecnologia":
                materias(create_df_bacharelado_biotecnologia(),df_materias_aprovadas)
            elif option == "Bacharelado de Ciência da Computação":
                materias(create_df_bacharelado_biotecnologia(),df_materias_aprovadas)
        else:
            st.write("Em desenvolvimento")


    
