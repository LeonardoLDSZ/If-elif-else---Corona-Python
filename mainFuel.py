from calculo import Calculo

def main():
    print("""
        Demonstração de valores gastos com combustível durante uam viagem, tendo como base o consumo do veiculo,
        e a distancia determinada pelo usuário!    
    """)

    print('Combustíveis disponíveis para o calcúlo:')
    print('     - Diesel')
    print('     - Gasolina')
    print('     - Álcool')

    print(' ')

    try:
        distancia = float(input('Distância em Quilômetros a ser percorrida:\n'))
        consumo = float(input('Consumo de combustível do veículo (Km/h):\n'))
        calculo = Calculo()
        print(calculo.calcular_gasto(distancia, consumo))
    except ValueError as erro:
        print('O valor informado não é válido')

if __name__ == "__main__":
    main()




