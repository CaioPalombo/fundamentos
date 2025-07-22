def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)


 #atualizar_posicao = atualiza_posicao()
 #procurar = procurar_item_na_lista()


cores = []
cores_frias = []
cores_quentes = []
cores_neutras = []
titulo('listas')
cores_quentes = ['vermelho', 'amarelo', 'larnja']
cores_frias = ['azul', 'verde']
cores_neutras = ['branco', 'preto']
print(cores_quentes, cores_frias, cores_neutras)

#Adicionar elementos

titulo('cores append')

cores_quentes.append('carmim') 
cores_frias.append('ciano')
cores_neutras.append('cinza')
print(cores_frias, cores_neutras, cores_quentes)

titulo('extend')

cores.extend(cores_quentes)
cores.extend(cores_frias)
cores.extend(cores_neutras)
print(cores)

titulo('index')

#rint( {cores_neutras.index(cores_neutras[-1])})
indice = cores.index('azul')
print('na lsita "cores", o azul está na posição', indice)


titulo('insert')

print(cores_quentes)
cores_quentes.insert(1, 'magenta')
print(cores_quentes)


titulo('remove')

print(cores_quentes)
cores_quentes.remove('carmim')
print(cores_quentes)

titulo('pop')

print(cores_frias)
elemento_removido = cores_frias.pop(0)
print(elemento_removido)
print(cores_frias)

titulo('count')

print(cores_frias)
n_vezes = cores_frias.count('ciano')
print(n_vezes)

titulo('copy')

cores_frias_2 = cores_frias
cores_frias_2.append('anil')
print(cores_frias_2)
print(cores_frias)
cores_frias_2 = cores_frias.copy()
print(cores_frias_2)
cores_frias_2.append('anil')
print(cores_frias_2)



titulo('sort')

print(cores_quentes)
cores_quentes.sort()
print(cores_quentes)
cores_quentes.sort(reverse = True)
print(cores_quentes)
print(cores_quentes[0])
ordem_reversa = sorted(cores_quentes, reverse = True)
print(ordem_reversa)
print(cores_quentes[0])

titulo('reverse')
print(cores_frias_2)
cores_frias_2.reverse()
print(cores_frias_2)


titulo('Atualizar Posi')
print(cores_quentes)
cores_quentes[0] = 'amarelo'
print(cores_quentes)

titulo('procura')

print(cores)
procura = 'preto' in cores
print(procura)