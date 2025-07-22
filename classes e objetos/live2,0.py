class Fila:
    c_fila = []

    #manipulação da abstração de dado

    @classmethod                
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)


    #Manipulação de exemplo ou instância 

    def __int__(self):
        self.s_fila = []
        
    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)            