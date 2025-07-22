paises = []
paises_europa = [] # criação de lista vazia
paises_africa = list() # criação de lista vazia
print(paises_europa, type(paises_europa), paises_africa)
paises_europa = ['espanha', 'frança', 'itália', 'holanda'] 
paises_africa = ['africa do sul', 'moçambique', 'camarões', 'marrocos', 'camarões']



def main():
  # criar_elementos_lista = metodo_len_e_append()
  # extend = metodo_extend()
  # indice_elemento = metodo_index()
  # inserir_elemento = metodo_insert()
  # remover_elemento = metodo_remove()
  # remove_pelo_indice = metodo_pop()
  # deletar_keyword = keyword_del()
  # contar = metodo_count()
  # copiar = metodo_copy()
  # clear = metodo_clear()
  # ordenar = metodo_sort()
  reverter = metodo_reverse()
  atualizar_posicao = atualiza_posicao()
  procurar = procurar_item_na_lista()



def metodo_len_e_append():
  """metodo_len_e_append(
  lista.append('elemento')
  len(lista)
  """
  paises_europa.append('alemanha') # Inserir elemento no final de uma lista
  paises_africa.append('egito')
  paises_africa.append('angola')
  paises_europa.append('portugal')
  # print(len(paises_europa)) # indica a quantidade de elementos da lista
  # print(f'A quantidade de países dessa lista é: {len(paises_africa)}')
  # print(f'Os países africanos dessa lista são: {paises_africa}')
  # paises.append(paises_europa)
  # paises.append(paises_africa)
  # print(paises)




def metodo_extend():
  """
  lista_1.extend(lista_2)
  adiciona elementos de lista, tupla e conjuntos 
  """
  paises.extend(paises_europa)
  paises.extend(paises_africa)
  print(paises)
  paises_1 = paises_europa + paises_africa 
  print(paises_1)
  # paises_europa += paises_africa 
  # print(paises_europa)


def metodo_index():
  """
  lista.index(elemento, inicio, fim)
  elemento - procurado
  inicio - indice inical de procura
  fim - indice final de procura
  - quando passamos o ultimo elemento de uma lista para o metodo index, sabemos a quantidade de elementos da lista >>> lista.index(lista[-1])
  """
  print(f'O {paises_europa.index(paises_europa[-1])} elemento da lista de países europeus é: {paises_europa[-1]}')
  indice = paises_europa.index('espanha')
  print(indice)
  indice_2 = paises_europa.index('frança', 0, 4) # delimitando o inicio e fim da procura
  print(indice_2)


def metodo_insert():
  """
  lista.insert(indice, elemento)
  - insere um elemento em um índice especificado 
  """
  print(paises_europa)
  paises_europa.insert(1, 'romenia')
  print(paises_europa)


def metodo_remove():
  """
  lista.remove(elemento)
  - remove apenas o primeiro elemento correspondente 
  """
  print(paises_africa)
  paises_africa.remove('camarões')
  print(paises_africa)


def metodo_pop():
  """
  lista.pop(indice)
  - remove elemento a partir do índice fornecido e retorna o item que foi removido
  """
  print(paises_europa)
  elemento_removido = paises_europa.pop(0)
  print(elemento_removido)
  print(paises_europa)


def keyword_del():
  """
  del lista[indice]
  - exclui um elemento a partir de um determinado índice
  - remove fatias de uma lista
  """
  print(paises_africa)
  del paises_africa[2]
  print(paises_africa)
  del paises_africa[1:]
  print(paises_africa)


def metodo_clear():
  """
  lista.clear()
  - remove todos os itens de uma lista 
  """
  print(paises_africa)
  clear_paises_africa = paises_africa.clear()
  print(clear_paises_africa)


def metodo_count():
  """
  lista.count(elemento)
  - retorna o nº de vezes que o elemento aparece na lista
  """
  print(paises_africa)
  n_vezes = paises_africa.count('camarões')
  print(n_vezes)


def metodo_copy():
  """
  nova_lista = lista.copy()
  - copia a lista original e os novos elementos colocados na nova lista não são acrescidos na lista original
  """
  paises_europa_novo = paises_europa
  paises_europa_novo.append('grécia')
  print(paises_europa_novo)
  print(paises_europa)
  paises_europa_novo = paises_europa.copy()
  print(paises_europa_novo)
  paises_europa_novo.append('grécia')
  print(paises_europa_novo)


def metodo_sort():
  """
  lista.sort()
  - classifica os elementos da lista em ordem crescente ou decrescente
  - muda a lista diretamente 
  sorted()
  - não muda a lista, simplesmente ordena
  """
  print(paises_europa)
  paises_europa.sort()
  print(paises_europa)
  paises_europa.sort(reverse = True)
  print(paises_europa)
  print(paises_europa[0])
  ordem_reversa = sorted(paises_europa, reverse = True)
  print(ordem_reversa)
  print(paises_europa[0])


def metodo_reverse():
  """
  lista.reverse()
  - inverte os elementos da lista
  """
  print(paises_africa)
  paises_africa.reverse()
  print(paises_africa)
  # reversão de lista por operador de fatiamento
  lista_reversa = paises_africa[::-1]
  print(lista_reversa)
  # função reversed() para acessar elementos individuais de uma lista
  for elemento in reversed(paises_africa):
    print(elemento)



def atualiza_posicao():
  """
  atualiza elemento de determinada posição
  """
  print(paises_europa)
  paises_europa[-1] = 'frança'
  print(paises_europa)
 

def procurar_item_na_lista(): 
  """
  retorna True ou False na procura de determinado elemento na lista
  """
  print(paises_africa)
  procura = 'brasil' in paises_africa
  print(procura) 















if __name__ == "__main__":
  main()