var valor;
function botao(num){
    valor = document.calc.visor.value += num;
    x;
    y;
    x = x+y;
}

function reseta(){
    document.calc.visor.value = '';
}

function calcula(){
    resultado = eval(valor);
    document.calc.visor.value = resultado.toLocaleString('pt-BR');
}