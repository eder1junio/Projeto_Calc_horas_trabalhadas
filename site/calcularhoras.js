
function formatahoras(totalhoras, totalminutos){
    if (totalminutos <10){
        var totalminutos = "0"+`${totalminutos}`

    }
    if (totalhoras<10){
        var totalhoras = "0"+`${totalhoras}`
    }
    return `${totalhoras}:${totalminutos}`

}


function calcularhorastrabalhadas(horasEntrada,miutosEntrada,horasSaida,miutosSaida){
    if (miutosEntrada > miutosSaida){
        horasSaida = horasSaida -1
        miutosSaida = miutosSaida +60
    }
    totalhoras = horasSaida - horasEntrada
    totalminutos = miutosSaida - miutosEntrada
    return formatahoras(totalhoras,totalminutos)

}  

function mostraHorasTrabalhadas(){
    var entrada = document.getElementById("entrada").value;
    var saidaIntervalo = document.getElementById("intervalosaida").value
    var [horasEntradaSt,minutosEntradast] = entrada.split(":") 
    var [horasIntervaloSt,minutosIntervaloSt] = saidaIntervalo.split(":")
    var horasEntrada = parseInt(horasEntradaSt,10)
    var minutosEntrada = parseInt(minutosEntradast,10)
    var horasIntervalo = parseInt(horasIntervaloSt,10)
    var minutosIntervalo = parseInt(minutosIntervaloSt,10)
    calcularhorastrabalhadas(horasEntrada,minutosEntrada,horasIntervalo,minutosIntervalo)
    alert(calcularhorastrabalhadas(horasEntrada,minutosEntrada,horasIntervalo,minutosIntervalo));

}
