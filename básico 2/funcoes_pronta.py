def cumprimento():
  print('olá')

cumprimento()

def soma(a, b):
  x = a + b 
  print(f'a soma é {x}')

soma(1, 1)

# a ordem dos parâmetros importa
def soma(a, b=1):
  x = a + b 
  print(f'a soma é {x}')

soma(1)
soma(b = 10, a = 10)


# a palavra-chave return indica o que será retornado quando a função for chamada; se o return não for colocado e a função for chamada, será retornado um 'None'
def soma(a, b):
  x = a + b 
  return x

n1 = int(input('insira o primeiro número: ' ))
n2 = int(input('insira o segundo número: ' ))
resultado = soma(n1, n2)
print(f'a soma é: {resultado}')



