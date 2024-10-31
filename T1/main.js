
function criaTrilha(pontosDeParada, distanciaDiaria) {
    let trilha = {
        tamanhodaTrilha: 0,
        pontosDeParada: pontosDeParada,
        distanciaDiaria: distanciaDiaria
    }
    return trilha;

}

function verificaProximaParada(distanciaPercorrida, proximaParada, distanciaRestanteDeHoje) {
    if ((proximaParada - distanciaPercorrida) < distanciaRestanteDeHoje) {
        return true;
    }
    return false;

}



function percorrer(trilha) {
    let distanciaPercorrida = 0;
    let pontosDeParadaPercorridos = 0;
    let distanciaDiaria = trilha.distanciaDiaria;
    let distanciaRestanteDeHoje = distanciaDiaria
    let pontosDeParada = trilha.pontosDeParada;
    let tamanhodaTrilha = trilha.tamanhodaTrilha;
    let estadoDoDia = "dia"
    let contadorDeDias = 0
    console.log("oi")

    while (pontosDeParada.lenth > 0) {
        if (distanciaRestanteDeHoje === 0) {
            estadoDoDia = "noite"
        }
        else if (estadoDoDia === "dia") {

            while (true) {
                let i = 0;
                if (!(verificaProximaParada(distanciaPercorrida, pontosDeParada[i], distanciaRestanteDeHoje))) {
                    while
                }
                let proximaParada = pontosDeParada[0];
                if (verificaProximaParada(distanciaPercorrida, proximaParada, distanciaRestanteDeHoje)) {

                }
            }
            if (estadoDoDia === "noite") {
                console.log("Dormiu")
                contadorDeDias++;
                estadoDoDia = "dia";
                let distanciaRestanteDeHoje = distanciaDiaria;
            }

        }
    }
}

function main() {
    let trilha = criaTrilha([4, 8, 15, 23, 30, 35, 40, 50, 60], 10);
    percorrer(trilha);
}

main();