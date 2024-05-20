
def salvaHORAS(horasEntrada=0,horaInicioIntervalor=0,horaFinIntervalor=0,horaDeSaida=0,horasTrabalhadas=0,datas=0):

    with open("horasTrabalhadas.txt", "a") as arquivo:
        arquivo.write(f"Data {datas} Horas de entrada{horasEntrada}, Horas inicio Intervalo{horaInicioIntervalor},horas fin do intervalo{horaFinIntervalor} horas de saida{horaDeSaida}, horas trabalhadas{horasTrabalhadas}\n ")

def calcularHoras(horasEntrada,minutosEntrada, horasSaida,minutosSaida):
    
    if minutosEntrada > minutosSaida:
        horasSaida = horasSaida -1
        minutosSaida = minutosSaida + 60

    minutosTotais = minutosSaida - minutosEntrada
    horasTotais = horasSaida - horasEntrada
    if minutosTotais >60:
        minutosTotais =minutosTotais - 60
        horasTotais = horasTotais +1
    horaCompleta = f"{horasTotais}:{minutosTotais}"    
    
    return horasTotais, minutosTotais

while True:

    #data = input("digite a data")
    while True:
        horasEntradaAmnha = int(input("digite as horas de entrada "))
        if horasEntradaAmnha < 24:
            break
    while True:
        minutosEntradaAmanha = int(input("digies os minutos de entrada "))
        if minutosEntradaAmanha > 0 and minutosEntradaAmanha <60:
            break
    while True:
        horasSaidaAmanha= int(input("digite a hora de saida"))
        if horasSaidaAmanha < 24:
            break
    while True:
        minutoSaidaAmanha = int(input("digite os nimutos de saida "))
        if minutoSaidaAmanha >0 and minutoSaidaAmanha <60:
            break
   

    horasAmanha, minutosAmanha = calcularHoras(horasEntradaAmnha,minutosEntradaAmanha,horasSaidaAmanha,minutoSaidaAmanha)
    print(horasAmanha,minutosAmanha)
    while True:
        horasEntradaTarde = int(input("digite as horas de entrada "))
        if horasEntradaTarde< 24:
            break
    while True:
        minutosEntradaTarde = int(input("digies os minutos de entrada "))
        if minutosEntradaTarde > 0 and minutosEntradaTarde <60:
            break
    while True:
        horasSaidaTarde= int(input("digite a hora de saida"))
        if horasSaidaTarde < 24:
            break
    while True:
        minutoSaidaTarde = int(input("digite os nimutos de saida "))
        if minutoSaidaTarde >0 and minutoSaidaTarde <60:
            break
    
    tarde = calcularHoras(horasEntradaTarde,minutosEntradaTarde,horasSaidaTarde,minutoSaidaTarde)
    print(tarde)
    totalHorasTrabalhadas = amanha+tarde
    horasCompletasAmanha = f"{horasEntradaAmnha}:{minutosEntradaAmanha}"
    horasCompletasAmanhaSaida = f"{horasSaidaAmanha}:{minutoSaidaAmanha}"
    horasCompletasTarde = f"{horasEntradaTarde}:{minutoSaidaTarde}"
    horasCompletasTardeSaida = f"{horasSaidaTarde}:{minutoSaidaTarde}"
    salvaHORAS(horasCompletasAmanha,horasCompletasAmanhaSaida,horasCompletasTarde,horasCompletasTardeSaida,totalHorasTrabalhadas)
      

    sn = input("vc gostaria de sair do progrma")
    if sn == "sS":
        break



