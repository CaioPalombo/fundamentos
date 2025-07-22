

def main():
#remover = dict_metodo_clear()
 copiar = dict_metodo_copy()
 novo_dicionario = dict_metodo_fromkeys()
 #valor_chave = dict_metodo_get()
 #itens_valor_chave = dict_metodo_items()
 #lista_chaves = dict_metodo_keys()
 #remover_retornar = dict_metodo_popitem()
 #inserir_valor = dict_metodo_setdefault()
 #remover_a_partir_da_chave = dict_metodo_pop()
 #valor_por_item = dict_metodo_values()
 #atualizar =  dict_metodo_update()

cores = {'frias' : ['azul', 'verde', 'ciano'], 'quentes' : ['vermelho', 'laranja', 'rosa']}

print('nosa lista é:',cores)
print('-'*30)

#Remove

def dict_metodo_clear():
  print(cores)
  cores.clear()
  print(cores)

#copiar

def dict_metodo_copy():
  dict_copia_cores = cores.copy
  print(dict_copia_cores)

#novo_dict

def dict_metodo_fromkeys():
  chaves = {'vermelho', 'azul'}
  valores = 'cores_primarias'
  print(chaves, type(chaves))
  cores_primarias = dict.fromkeys(chaves)
  print(cores_primarias, type(cores_primarias))
  #novo dict a partir de uma sequencia de valores
  cores_primarias = dict.fromkeys(chaves, valores)
  print(cores_primarias, type(cores_primarias))
  #dicionario a partir de uma lista
  valores_02 = []
  valores_02.append('cores puras')
  cores_primarias =  dict.fromkeys(chaves, valores_02)
  print(cores_primarias)
  valores_02.append('dá origem a outras cores')
  print(cores_primarias)
  print('-'*30)

def dict_metodo_get():
  print(cores.get('branco'))







if __name__  == "__main__":
  main()