from __future__ import print_function
import glob
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
    

def convertFile(file):
    if os.path.isfile(file):
        filename = os.path.basename(file)
        print("Convertendo o arquivo: {}".format(filename))
    import ipdb
    #ipdb.set_trace()
    df = pd.read_csv(file, na_filter=False)

    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)

    columns = ["firstName","middleName","lastName","company","jobTitle","workPhone","workPhone2","companyPhone","homePhone","homePhone2","mobilePhone","email","email2"]

    office = df[columns]

    office.to_csv(os.path.join(csv_output,filename), index=None)
    print("Arquivo convertido com sucesso: {}".format(os.path.join(csv_output,filename)))

os.chdir(csv_input)
for file in glob.glob(os.path.join(csv_input,"*.csv")):
    convertFile(file)
