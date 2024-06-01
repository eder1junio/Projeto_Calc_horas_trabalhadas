
def salvaHORAS(horasEntrada=0,horaInicioIntervalor=0,horaFinIntervalor=0,horaDeSaida=0,horasTrabalhadas=0,datas=0):

    with open("horasTrabalhadas.txt", "a") as arquivo:
        arquivo.write(f"data:{datas} entrada:{horasEntrada}, saida:{horaInicioIntervalor}, entrada:{horaFinIntervalor} saida{horaDeSaida}, horas totais:{horasTrabalhadas}\n ")

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

    data = input("digite a data")
    while True:
        horasEntradaAmnha = int(input("digite as horas de entrada  de manha"))
        if horasEntradaAmnha < 24:
            break
    while True:
        minutosEntradaAmanha = int(input("digies os minutos de entrada de manha "))
        if minutosEntradaAmanha > 0 and minutosEntradaAmanha <60:
            break
    while True:
        horasSaidaAmanha= int(input("digite a hora de saida de manha"))
        if horasSaidaAmanha < 24:
            break
    while True:
        minutoSaidaAmanha = int(input("digite os nimutos de saida de manha "))
        if minutoSaidaAmanha >0 and minutoSaidaAmanha <60:
            break
   

    horasAmanha, minutosAmanha = calcularHoras(horasEntradaAmnha,minutosEntradaAmanha,horasSaidaAmanha,minutoSaidaAmanha)
    print(horasAmanha,minutosAmanha)
    while True:
        horasEntradaTarde = int(input("digite as horas de entrada de tarde  "))
        if horasEntradaTarde< 24:
            break
    while True:
        minutosEntradaTarde = int(input("digies os minutos de entrada de tarde "))
        if minutosEntradaTarde > 0 and minutosEntradaTarde <60:
            break
    while True:
        horasSaidaTarde= int(input("digite a hora de saida de tarde "))
        if horasSaidaTarde < 24:
            break
    while True:
        minutoSaidaTarde = int(input("digite os nimutos de saida de tarde  "))
        if minutoSaidaTarde >0 and minutoSaidaTarde <60:
            break
    
    tardehoras,tardeminutos  = calcularHoras(horasEntradaTarde,minutosEntradaTarde,horasSaidaTarde,minutoSaidaTarde)
    print(tardehoras, tardeminutos)
    totalHorasTrabalhadas = horasAmanha+tardehoras
    totalminutos = minutosAmanha+tardeminutos
    if totalminutos > 60:
        totalminutos = totalminutos-60
        totalHorasTrabalhadas = totalHorasTrabalhadas +1


    totalHorasTrabalhadas = horasAmanha+tardehoras
    horasCompletasAmanha = f"{horasEntradaAmnha}:{minutosEntradaAmanha}"
    horasCompletasAmanhaSaida = f"{horasSaidaAmanha}:{minutoSaidaAmanha}"
    horasCompletasTarde = f"{horasEntradaTarde}:{minutoSaidaTarde}"
    horasCompletasTardeSaida = f"{horasSaidaTarde}:{minutoSaidaTarde}"
    totalHorasTrabalhadasMinutos = f"{totalHorasTrabalhadas}:{totalminutos}"
    salvaHORAS(data,horasCompletasAmanha,horasCompletasAmanhaSaida,horasCompletasTarde,horasCompletasTardeSaida,totalHorasTrabalhadasMinutos)
      

    sn = input("vc gostaria de sair do progrma")
    if sn == "sS":
        break



