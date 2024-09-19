import os
import pandas as pd
import mysql.connector
import xmltodict

def criar_conexao_mysql():
    # Configurações de conexão com o MySQL (phpMyAdmin)
    conexao = mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="6bRxFl/8PVOL)Sfh",
        database="trabalho_processamento_dados"
    )
    return conexao

def criar_tabela(cursor, nome_tabela, df):
    # Verificar se a tabela já existe
    cursor.execute(f"SHOW TABLES LIKE '{nome_tabela}'")
    tabela_existe = cursor.fetchone()

    if not tabela_existe:
        # Se a tabela não existe, criar a tabela
        criar_query = f"CREATE TABLE {nome_tabela} ({', '.join([f'{col} VARCHAR(255)' for col in df.columns])})"
        cursor.execute(criar_query)

def importar_excel_para_mysql(caminho_excel, conexao, nome_tabela):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_excel)

    # Conectar ao MySQL (phpMyAdmin)
    cursor = conexao.cursor()

    # Verificar se a tabela existe, se não, criar a tabela
    criar_tabela(cursor, nome_tabela, df)

    # Verificação sobre as linhas do DataFrame e inserir dados no MySQL
    for _, linha in df.iterrows():
        # Remover colunas não nomeadas (Unnamed)
        linha = linha.dropna()

        # Se todas as colunas são NaN, pule esta linha
        if linha.isna().all():
            continue

        # Construir a consulta SQL dinamicamente
        colunas_sql = ', '.join(linha.index)
        valores_sql = ', '.join(['%s'] * len(linha))
        query = f"INSERT INTO {nome_tabela} ({colunas_sql}) VALUES ({valores_sql})"

        valores = tuple(linha)
        cursor.execute(query, valores)

    # Confirmar as alterações e fechar a conexão
    conexao.commit()
    cursor.close()

def exportar_excel_para_xml(caminho_excel, caminho_xml):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_excel)

    # Converter o DataFrame para um dicionário
    data_dict = df.to_dict(orient='records')

    # Converter o dicionário para XML usando xmltodict
    xml_data = xmltodict.unparse({"root": {"row": data_dict}}, pretty=True)

    # Salvar o XML no arquivo especificado
    with open(caminho_xml, "w") as xml_file:
        xml_file.write(xml_data)

def escolher_arquivo_excel(pasta_excel):
    # Listar todos os arquivos Excel na pasta
    arquivos_excel = [arquivo for arquivo in os.listdir(pasta_excel) if arquivo.endswith(".xlsx")]

    # Mostrar os arquivos disponíveis
    print("Arquivos Excel disponíveis:")
    for i, arquivo in enumerate(arquivos_excel, 1):
        print(f"{i}. {arquivo}")

    # Obter a escolha do usuário
    escolha = int(input("Escolha o número do arquivo Excel: "))
    caminho_completo = os.path.join(pasta_excel, arquivos_excel[escolha - 1])

    return caminho_completo

if __name__ == "__main__":
    # Pasta contendo os arquivos Excel
    pasta_excel = "C:\\Users\\migue\\OneDrive\\Ambiente de Trabalho\\Tarefa 4\\Dataset"

    # Criar conexão MySQL
    conexao_mysql = criar_conexao_mysql()

    # Escolher arquivo Excel
    caminho_excel_escolhido = escolher_arquivo_excel(pasta_excel)

    # Nome da tabela no MySQL (pode ser personalizado)
    nome_tabela = "PDI"

    # Importar dados do Excel para MySQL
    importar_excel_para_mysql(caminho_excel_escolhido, conexao_mysql, nome_tabela)
    print("Dados importados para o MySQL com sucesso!")

    # Exportar dados do Excel para XML
    caminho_xml = "C:\\Users\\migue\\OneDrive\\Ambiente de Trabalho\\Tarefa 4\\Output\\Output.xml"
    exportar_excel_para_xml(caminho_excel_escolhido, caminho_xml)
    print(f"Dados exportados para {caminho_xml}")

    # Fechar a conexão MySQL
    conexao_mysql.close()
