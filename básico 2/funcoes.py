#Título

def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)

    

#Soma

def soma(a,b):
    x=a+b
    return x


titulo("Vamos somar dois números?")

n1 = int(input("digite um número"))
n2 = int(input("digite outro número"))
resultado = soma(n1, n2)
print("a soma é", {resultado})


