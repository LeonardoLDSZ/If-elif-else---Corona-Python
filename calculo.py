class Calculo:
    def __init__(self):
        self.__valor_gasolina = 3.89
        self.__valor_alcool = 3.39
        self.__valor_diesel = 3.49

    def calcular_gasto(self, distancia, consumo):
        if (distancia <= 0 or consumo <= 0):
            raise Exception('O valor informado não pode ser menor ou igual a zero')

        gasto_gasolina = round((distancia / consumo) * self.__valor_gasolina, 2)
        gasto_alcool = round((distancia / consumo) * self.__valor_alcool, 2)
        gasto_diesel = round((distancia / consumo) * self.__valor_diesel, 2)

        return """
        O importe total gasto será de:
        
        Gasolina: R$ {}
        Álcool: R$ {}
        Diesel: R$ {}
        """. format(gasto_gasolina, gasto_alcool, gasto_diesel)










