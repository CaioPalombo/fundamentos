import os

def main():
   criacao_diretorio = criar_diretorio_mkdir()
   mkdirs = criar_diretorio()
   obtencao_diretorio = obter_diretorio()
   listagem_diretorio = listar_diretorios()
  # alteracao_diretorio = alterar_diretorio()
  # renomeacao_diretorio = renomear_diretorio()
  # remocao_diretorio = remover_diretorio()
  # uniao_diretorio = unir_diretorio()
  #arquivo_subpasta = criar_arquivos_em_subpasta('pasta_04')
  # rmv_arqv_sbpast = remover_arquivos_em_subpasta()

def criar_diretorio_mkdir():
    try:
        dir_criar = os.mkdir('pasta_01')
    except OSError as error:
        print(error)

def criar_diretorio(diretorio):
    dir_criar = os.makedirs(diretorio, exist_ok= True)
    return print(type(dir_criar))

def obter_diretorio():
    dir_obter = os.getcwd()
    print(dir_obter)

def listar_diretorios():
    dir_listar = os.listdir()
    print(f'lista de diretórios: {dir_listar}')


if __name__ == "__main__":
  main()