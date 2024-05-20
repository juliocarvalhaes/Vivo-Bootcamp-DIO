#Programa que informa onde João (Dono de Bicicletas) informe: cor, modelo, ano e valor da bicleta vendida.
#Uma bike pode: buzinar, parar e correr.
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('PIIIM')
    
    def correr(self):
        print("Catchaaaaao. Eu sou a velocidade!")
    
    def parar(self):
        print('Parando')
        print("Bicicleta parada!")
# Esse método é usado para retornar uma representação em string do objeto quando a função str() é chamada nele.
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
bike_01 = Bicicleta("Azul","Casio-456","2022","1230,00") 
bike_01.buzinar()
bike_01.correr()
bike_01.parar() 
print(bike_01.cor, bike_01.modelo, bike_01.ano , bike_01.valor)  