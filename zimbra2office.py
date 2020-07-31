from __future__ import print_function
import os
import pandas as pd
import sys

# Verifica se as variaveis dos diretorios para tratamento dos arquivos cvs foram definidas
csv_input = os.getenv("CSV_INPUT")
csv_output = os.getenv("CSV_OUTPUT")

if not csv_input:
    print("Variavel com o diretorio de origem dos arquivos csv nao foi definida. Ex: CSV_INPUT='/path/to/files/csv/input")
    sys.exit(1)

if not csv_output:
    print("Variavel com o diretorio de destino dos arquivos csv nao foi definida. Ex: CSV_OUTPUT='/path/to/files/csv/output")
    sys.exit(1)


# Verifica se existe os diretorios para tratamento dos arquivos cvs
if not os.path.isdir(csv_input):
    print("Diretorio de origem dos arquivos csv nao existe: {}".format(csv_input))
    sys.exit(1)

# Verifica se existe os diretorios para tratamento dos arquivos cvs
if not os.path.isdir(csv_output):
    print("Diretorio de destino dos arquivos csv nao existe: {}".format(csv_output))
    sys.exit(1)
    
df = pd.read_csv("/tmp/eber.cherulli@funpresp.com.br.csv", na_filter=False)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

#columns = ["email", "fileAs", "firstName", "fullName", "lastName", "middleName"] 
columns = ["firstName","middleName","lastName","company","jobTitle","workPhone","workPhone2","companyPhone","homePhone","homePhone2","mobilePhone","email","email2"]

office = df[columns]

office.to_csv("/tmp/csv/eber.cherulli@funpresp.com.br.csv", index=None)


