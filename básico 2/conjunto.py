cores_quentes = {'vermelho', 'amarelo', 'larnja', 'magenta'}
cores_frias = {'azul', 'verde', 'ciano', 'anil'}
cores_neutras = {'branco', 'preto'}


def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)

def main():
    remover = set_remove()
    discartar = set_discard()
   #popar = set_pop()
    adicionar = set_add()
    copiar = set_copy()
    #limpar = set_clear()
    diferenciar = set_difference()
    interseccao = set_intersection()
    interseccao_update = set_intersection_update()
    isdisjoint = set_isdisjoint()
    uniao = set_union()
    #ubset = set_subset()
    #ymettricdif = set_symetricdifference()

#Remover

def set_remove():

    print(cores_frias)
    cor = cores_frias.remove('azul')
    print(cor)

#Descartar

def set_discard():

    print(cores_quentes)
    cor2 = cores_quentes.discard('amarelo')
    print(cor2)

#Pop

def set_pop():

    print(cores_quentes)
    cor_removida = cores_quentes.pop()
    print('a cor removida foi:', cor_removida)

#adicionar

def set_add():
    print(cores_neutras)
    elementos = ('cinza', 'prata')
    eita_cor =  cores_neutras.add(elementos)
    print(eita_cor, cores_neutras)

#copiar

def set_copy():
    copia_quente = cores_quentes.copy()
    copia_quente.add('rosa')
    print(copia_quente)
    print(cores_quentes)
    return copia_quente

#limpar

def set_clear():

    copia_mod = set_copy
    cores_quentes.clear()
    print(cores_quentes)

#diferenca

def set_difference():
    copia_mod = set_copy() 
    #diferenca = cores_quentes.difference(copia_mod)
    #print(diferenca)
    #print(cores_quentes)
    diferenca_a_b = cores_quentes.difference(copia_mod)
    print(diferenca_a_b)

#Interseccao

def set_intersection():
    copia_mod = set_copy() 
    interseccao = cores_quentes.intersection(copia_mod)
    print(interseccao)

#Interseccao_update

def set_intersection_update():
    copia_mod = set_copy()
    interseccao = copia_mod.intersection_update(cores_quentes,copia_mod)
    print(interseccao)

#isdisjoint

def set_isdisjoint():
    verifica = cores_frias.isdisjoint(cores_quentes)
    print(verifica)

#uniao_estável

def set_union():
    uniao_cores = cores_quentes.union(cores_frias)
    print(uniao_cores)
    return uniao_cores

#SubSet

def set_subset():
    cores = set_union
    verificar = cores_frias.issubset(cores)
    print(verificar)

#super_set

def set_superset():
    cores = set_union
    verifica = cores.issuperset(cores_frias)
    print(verifica)

#Diferenca_simetrica

def set_symetricdifference():
    cores = set_union
    verifica = cores_frias.symmetric_difference(cores)
    print(verifica)

if __name__ == "__main__":
    main()