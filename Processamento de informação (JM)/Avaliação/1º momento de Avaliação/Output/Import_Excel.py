import pandas as pd

#Localização da pasta
input ='C\Users\migue\OneDrive - ISGAYA\Faculdade\IPSGAYA\Licenciatura - Engenharia Informática\2º Ano\1º Semestre\Processamento de informação\Avaliação\1º momento de Avaliação\DatasetDGEEC_DSEE_DEES_2017_ListasRebides_1415.xlsx'
output = 'Output\Untitled-1.xml'
sheet_name = 'CarreiraAtividades1415'

df = pd.read_excel(input, sheet_name, engine='openpyxl')

df.to_xml(output, root_name='Dataset', row_name='Dados')
print(f"All data has been save to {output}.")