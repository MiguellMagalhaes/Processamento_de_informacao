import pandas as pd

#Localização da pasta
input ='Dataset\DGEEC_DSEE_DEES_2017_ListasRebides_1415.xlsx'
output = 'Output\output.xml'
sheet_name = 'CarreiraAtividades1415'

df = pd.read_excel(input, sheet_name, engine='openpyxl')

df.to_xml(output, root_name='Dataset', row_name='Dados')
print(f"All data has been save to {output}.")