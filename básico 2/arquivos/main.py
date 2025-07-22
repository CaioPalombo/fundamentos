def main():
  escrita = escrever()  
  leitura = ler()
  substuicao = subsituir()
  atualizacao = atualizar()
  acrescimo = acrescentar()
  leitura_linha = ler_linha()
  listar_linhas = iterar_linha_arquivo()


#Funções

def escrever():
  with open('lorem.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('bom dia e boa noite')

def ler():
  with open('lorem.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
    
def subsituir():
  with open('lorem.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('olá, mundo\n')

def atualizar():
  with open('lorem.txt', 'a+', encoding='utf-8') as arquivo:
    print(arquivo.write('teste\n'))

def acrescentar():
  with open('lorem.txt', 'a', encoding='utf-8') as arquivo:
    nova_linha = '\Lorem Ipsum é um texto padrão em latim usado como placeholder para preencher espaços em projetos gráficos e de desenvolvimento, simulando conteúdo real.'
    print(arquivo.write(nova_linha))

def ler_linha():
  with open('lorem.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.readline())

def iterar_linha_arquivo():
  with open('lorem.txt', 'r', encoding='utf-8') as arquivo:
    for i in arquivo:
      print(i)



if __name__ == "__main__":
  main()