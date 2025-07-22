def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)


cores_quentes = ('vermelho', 'amarelo', 'larnja')
cores_frias = ('azul', 'verde', 'ciano')
cores_neutras = ('branco', 'preto')


titulo('count')

print('número de vezes que o elemento "verde" aparece na lista cores_firas')
n_vezes = cores_frias.count('verde')
print(n_vezes)

titulo('index')

indice_cores_quentes = cores_quentes.index('vermelho', 1)
print(indice_cores_quentes)
