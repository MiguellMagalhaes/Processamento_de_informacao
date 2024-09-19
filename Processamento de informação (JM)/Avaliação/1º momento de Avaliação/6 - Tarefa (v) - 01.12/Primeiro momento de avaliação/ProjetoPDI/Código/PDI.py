#Importar bibliotecas necessárias
import pandas as pd
import mysql.connector
import os


output = "C:/Users/migue/OneDrive/Ambiente de Trabalho/ProjetoPDI/Output/Output.xml"
sheet = 'Habilitacoes1415'
# Obtém o valor da pesquisa na configuração
#search_column=config['SEARCH_COLUMN']
# Obtém o nome do diretório na configuração
directory_name = "C:/Users/migue/OneDrive/Imagens/Dataset"
#sheet_name = config['SHEET_NAME']
ROW1 = 'IDDOcente'
ROW2 = 'Nome_docente'
ROW3 = 'Estab'
ROW4 = 'Estab_Nome'
ROW5 = 'UO'
ROW6 = 'UO_Nome1'
ROW7 = 'Grau_nome'
ROW8 = 'CodigoCurso'
ROW9 = 'NomeCurso'
ROW10 = 'OutroCurso'
ROW11 = 'CodigoEspecialidade'
ROW12 = 'NomeEspecialidade'
ROW13 = 'OutraEspecialidade'

# Função para exibir os nomes de todas as tabelas em um arquivo Excel
def mostrar_paginas_excel(input_file):
    # Carregue o arquivo Excel
    xls = pd.ExcelFile(input_file)
    # Obtenha os nomes de todas as tabelas
    sheet_names = xls.sheet_names  # Obtém todos os nomes das tabelas
    # Imprima os nomes de todas as tabelas
    for i, sheet in enumerate(sheet_names, start=1):
        print(f"{i}. {sheet}")
    # Retorna os nomes de todas as tabelas
    return sheet_names

# Função para exibir os nomes de todas as colunas em uma tabela de um arquivo Excel
def mostrar_colunas_excel(input_file, sheet_name):
    # Carregar a tabela do arquivo Excel
    df = pd.read_excel(input_file, sheet_name, engine='openpyxl')
    # Obtém os nomes de todas as colunas
    columns = df.columns.tolist()  # Obtém todos os nomes de colunas
    # Imprimir os nomes de todas as colunas
    for i, column in enumerate(columns, start=1):
        print(f"{i}. {column}")
    # Retorna os nomes de todas as colunas
    return columns

# Função para ler um ficheiro Excel e escrevê-lo para um ficheiro XML
def ler_escrever(input_file, sheet_name):  # Add search_column as a parameter
    # Carregar a folha do ficheiro Excel
    df = pd.read_excel(input_file, sheet_name, engine='openpyxl')

    # Substituir espaços e caracteres especiais nos nomes das colunas - tabela proposta por Gabriel Fernando
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('\W', '')
    df.columns = df.columns.str.replace('/', '')
    df.columns = df.columns.str.replace('(', '')
    df.columns = df.columns.str.replace(')', '')
    df.columns = df.columns.str.replace('á', 'a')
    df.columns = df.columns.str.replace('à', 'a')
    df.columns = df.columns.str.replace('ç', 'c')
    df.columns = df.columns.str.replace('ã', 'a')
    df.columns = df.columns.str.replace('í', 'i')
    df.columns = df.columns.str.replace('ì', 'i')
    df.columns = df.columns.str.replace('é', 'e')
    df.columns = df.columns.str.replace('è', 'e')
    df.columns = df.columns.str.replace('ê', 'e')
    df.columns = df.columns.str.replace('%', 'Percentagem')
    df.columns = df.columns.str.replace('ó', 'o')
    df.columns = df.columns.str.replace(',', '')
    ###
    # Se não for especificada coluna ou valor de pesquisa, escrever todos os dados no ficheiro XML

    df.to_xml(output, root_name='Data', row_name='Row')
    print(f"Todos os dados foram guardados em {output}.")

        # Configuração da base de dados
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'database': 'dcw'
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("connection made 1")
    for index, Row in df.iterrows():
        dados = [Row.get(col) if pd.notna(Row.get(col)) else None for col in [ROW1, ROW2, ROW3, ROW4, ROW5, ROW6, ROW7, ROW8, ROW9, ROW10, ROW11, ROW12, ROW13]]
        query = "INSERT INTO habilitacoesnaofinal (IDDOcente, Nome_docente, Estab, Estab_Nome, UO, UO_Nome1, Grau_nome, CodigoCurso, NomeCurso, OutroCurso, CodigoEspecialidade, NomeEspecialidade, OutraEspecialidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        print("connection made 2")
        valores = tuple(dados)
        print("connection made 3")
        cursor.execute(query, valores)
        print("connection made 4")
        conn.commit()
        print("connection 5 commited")
    conn.close()
    print("connection closed")


# Função para mostrar os nomes de todos os ficheiros num diretório
def mostrar_diretorio(directory_name):
    try:
        # Obter os nomes de todos os ficheiros no diretório
        files = sorted(os.listdir(directory_name))  # Ordenar os ficheiros
        # Imprimir os nomes de todos os ficheiros
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        # Retornar os nomes de todos os ficheiros
        return files
    except FileNotFoundError:
        # Se o diretório não for encontrado, imprimir uma mensagem
        print(" Diretorio nao encontrado")
        return []

# Ciclo principal
while True:
    # Imprimir o menu
    print(" 1 - Escolha um arquivo: ")
    # Obter a escolha do utilizador
    choice = input(" Introduza a sua escolha: ")

    # Se o utilizador escolher começar a ler e escrever para o ficheiro
    if choice == '1':
        # Mostrar os nomes de todos os ficheiros no diretório
        files = mostrar_diretorio(directory_name)
        # Obter a escolha do utilizador para o ficheiro
        file_choice = int(input("Introduza o número do ficheiro que deseja selecionar: "))
        # Se a escolha do utilizador for válida
        if 1 <= file_choice <= len(files):
            # Obter o caminho do ficheiro escolhido
            input_file = os.path.join(directory_name, files[file_choice - 1])
            print(f"Selecionou{input_file}")
            # Mostrar os nomes de todas as folhas no ficheiro escolhido
            sheet_names = mostrar_paginas_excel(input_file)
            # Obter a escolha do utilizador para a folha
            sheet_choice = int(input("Introduza o número da folha que deseja selecionar: "))
            # Se a escolha do utilizador for válida
            if 1 <= sheet_choice <= len(sheet_names):
                # Obter o nome da folha escolhidaet
                sheet_name = sheet_names[sheet_choice - 1]
                print(f"Selecionou {sheet_name}")
                
                ler_escrever(input_file, sheet_name)# Chamar a função ler_e_escrever com o ficheiro, folha e coluna selecionados
            else:
                # Se a escolha do utilizador não for válida, imprimir uma mensagem
                print("Escolha de folha inválida. Por favor, introduza um número entre 1 e {}.".format(len(sheet_names)))
        else:
            # Se a escolha do utilizador não for válida, imprimir uma mensagem
            print("Escolha de ficheiro inválida. Por favor, introduza um número entre 1 e {}.".format(len(files)))
    else:
        print("Escolha de ficheiro inválida. Por favor, introduza um número entre 1")