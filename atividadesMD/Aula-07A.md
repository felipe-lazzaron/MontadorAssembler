<a name="inicio"></a>

# Aula 7: Temporização em Circuitos Digitais

## Objetivos

1.  Analisar os problemas decorrentes das características de temporização dos circuitos digitais.

2.  Propor soluções.


## Temporização

Para simplificar, durante o projeto consideramos que o tempo que um sinal leva para atravessar uma porta lógica, ou tempo de propagação, é inexistente. Podemos assim, diminuir o total de variáveis a serem consideradas durante a fase inicial do projeto.

Apesar do teste funcional não levar em consideração a temporização, é necessário verificar se o circuito ainda é funcional com os valores reais de temporização.

As consequências dos atrasos de propagação são, muitas vezes, pouco intuitivas.

### Contextualização

A lógica combinacional possui duas características de temporização:

-   O tempo de atraso de propagação;

-   O tempo de contaminação.

#### Tempo de Atraso de Propagação

É o tempo máximo entre:

-   Uma mudança nos sinais de entrada do circuito;

-   E a estabilização de sua saída.

Isso é devido à formação de circuitos RC dentro da porta. Dessa forma, o tempo de carga das capacitâncias (inclusive as parasitas) atrasa a passagem do sinal.

Por exemplo, para uma porta do tipo _buffer_ (uma porta não inversora), o tempo de propagação teria a seguinte influência no sinal de saída **Y**:

![**Tempo de Propagação**](imagensComponentes/atrasoBuffer-1.svg#p30 "Tempo de propagação em uma porta simples." )


#### Tempo de Contaminação

O tempo de contaminação é o tempo mínimo:

-   Entre a mudança dos sinais de entrada;

-   E o início da mudança dos sinais de saída.

![**Tempo de Contaminação**](imagensComponentes/atrasoBuffer-TempoContaminacao.svg#p30 "DicaMouse")

> Fica claro que o tempo de contaminação deve ser menor ou igual ao tempo de propagação.

Entre outras razões, a causa disso pode ser a diferença entre os caminhos, internos da porta, para o circuito de chaveamento para nível alto e o de chaveamento para o nível baixo.


#### Glitch

Considerando o circuito todo, ainda temos a influência do caminho percorrido pelos diferentes sinais que definem a saída.

Para um determinado circuito, podemos ter caminhos diferentes, passando por uma quantidade de portas diferente em cada caminho.
O resultado é que o circuito como um todo poderá ter um caminho mais longo (**caminho crítico**) e um caminho mais curto.

![**Diferenças entre o Caminho Crítico e Caminho Curto**](imagensComponentes/caminhoCritico-1.svg#p30 "Influência de caminhos diferentes para os sinais.")

<!---
O resultado é a ocorrência de um nível indesejado, de curta duração, entre o início e o fim das transições. Esse pulso é conhecido como _glitch_ - que veremos nos exercícios abaixo.
--->
<br>

O desenho abaixo mostra a diferença entre os atrasos em função do caminho. Para esse circuito, o tempo de propagação (_**tpd**_) é a soma das propagações das portas do caminho crítico. Por outro lado, o tempo de contaminação (_**tcd**_) é a soma das contaminações das portas do caminho curto.

![**A diferença de Atraso do Caminho Crítico e do Curto**](imagensComponentes/tempoCombinatorio-2.svg#p50 "Atraso pelo caminho curto e crítico")


***

## Atividade: Temporização na Lógica Combinacional

### Exercício 1

![**Exemplo da Influência da Temporização**](imagensComponentes/raceCondition-1.svg#p30)

Para o circuito mostrado acima, faça a sua tabela da verdade como mostrado abaixo.

|A|B|S|
|:---:|:---:|:---:|
|0|0| |
|0|1| |
|1|0| |
|1|1| |

***

<div class="bloco solucao" id="sol-0">
<div class="conteudo">

Abaixo temos a tabela da verdade para uma porta _AND_.

|A|B|S|
|:---:|:---:|:---:|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

O circuito proposto sempre possui, nas suas entradas, um valor lógico e seu inverso.

Fica claro, pela observação da tabela da porta _AND_, que a saída sempre terá nível _baixo_.

|A|~A|A and ~A|
|:---:|:---:|:---:|
|0|1|0|
|1|0|0|

![**Carta de Tempo para o Circuito, sem Considerar o Tempo de Propagação**](imagensComponentes/temporizacaoCombinacional-1.svg#p40)

</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

<p style="color:brown">
**Considerando o tempo de propagação igual a zero, qual a função desse circuito?**
</p>

***

<br>

### Exercício 2

![**Exemplo da Influência da Temporização**](imagensComponentes/raceCondition-1.svg#p30)

Novamente, usaremos o mesmo circuito - mostrado acima.

Porém, vamos considerar os atrasos das portas envolvidas.

Para simplificar, os atrasos serão:

-   Porta _NOT_:  1 unidade de tempo;

-   Porta _AND_:  1 unidade de tempo.

**Nessas condições, como ficaria a carta de tempo?**

![**Carta de Tempo para Rascunho**](imagensComponentes/temporizacaoCombinacionalGrafico-1a.svg#800)

<a href="./wavedrom/WaveDromEditor.html?{signal%3A%20[{}%2C%0A%20%20[%27Entradas%27%2C%0A%20%20{name%3A%20%27Entrada%27%2C%20wave%3A%20%220..1.....%22}%2C%0A%20%20{name%3A%20%27E%27%2C%20%20%20%20%20%20%20wave%3A%20%27d........%27}%2C%0A%20%20{name%3A%20%27~E%27%2C%20%20%20%20%20%20wave%3A%20%27d........%27}%0A%20%20]%2C%0A%20%20{}%2C%0A%20%20[%27Saída%27%2C%0A%20%20{name%3A%20%27S%27%2C%20%20%20%20%20%20%20wave%3A%20%27d........%27}]%2C%0A]%2C%0A%20%20head%3A{%0A%20%20%20text%3A%27Tabela%20de%20Temporização%27%2C%0A%20%20%20tick%3A0%2C%0A%20}%2C%0A%20foot%3A{%0A%20%20%20text%3A%27Tempo%20em%20Unidades%20de%20Propagação%27%2C%0A%20%20%20tick%3A0%0A%20}%2C%0A}%0A//%20Instruções%3A%0A//%20Cada%20posição%20da%20string%20wave%20equivale%20a%20uma%20unidade%20de%20tempo.%0A//%20As%20posições%20podem%20conter%3A%0A//%20p%20-%20when%20first%20in%20string%20creates%20positive%20edged%20clock%20wave%0A//%20n%20-%20when%20first%20in%20string%20creates%20negative%20edged%20clock%20wave%0A//%20P%20-%20same%20as%20p%20but%20with%20arrow%0A//%20N%20-%20same%20as%20n%20but%20with%20arrow%0A//%200%20-%20low%20level%0A//%201%20-%20high%20level%0A//%20=%20-%20value%20(default%20color%202)%0A//%202%20-%20value%20with%20color%202%0A//%203%20-%20value%20with%20color%203%0A//%204%20-%20value%20with%20color%204%0A//%205%20-%20value%20with%20color%205%0A//%20x%20-%20undefined%20value%0A//%20.%20-%20extends%20previous%20cycle%0A//%20z%20-%20high-impedance%20state%0A//%20u%20-%20pull-up%20(weak%201)%0A//%20d%20-%20pull-down%20(weak%200)%0A//%20|%20-%20extends%20previous%20cycle%20and%20draw%20gap%20on%20top%20of%20it%0A%0A"  target="_blank"><b>Editar a Carta de Temporização</b></a>

***

<div class="bloco solucao" id="sol-1">
<div class="conteudo">
<br>

A saída do circuito, em um primeiro instante, muda de acordo com o sinal que percorre o caminho curto (com menor atraso total). Esse é o sinal _**E**_ e só possui o atraso de uma porta _AND_.

Passada essa mudança, a saída do circuito dependerá do sinal que percorre o caminho crítico, ou seja, o sinal _**~E**_. Ele possui o atraso de uma porta inversora, que transforma _E_ em _~E_ e uma porta _AND_.


![**Carta de Tempo para o Circuito, Considerando o Tempo de Propagação**](imagensComponentes/temporizacaoCombinacional-2a.svg#p40)


</div><button onclick="exibe(this)">Ver Solução</button>
</div>

<p style="color:brown">
**Considerando o tempo de propagação para as portas, qual a função desse circuito?**
</p>

***

### Exercício 3

Para um circuito mais complicado, como o mostrado abaixo, qual seria a saída _Y_ quando o sinal _B_ fizer a transição de nível alto para nível baixo?

![**Circuito Digital**](imagensComponentes/glitch-A-1.svg#600)

![**Mapa de Karnaugh do Circuito Acima**](imagensComponentes/glitch-A-1-Karnaugh.svg#400)

![**Carta de Tempo para Rascunho**](imagensComponentes/temporizacaoGlitch-A-1b.svg#800)


<a href="./wavedrom/WaveDromEditor.html?{signal%3A%20[{}%2C%0A%20%20[%27Entradas%27%2C%0A%20%20{name%3A%20%27A%27%2C%20wave%3A%20%20%220..........%22}%2C%0A%20%20{name%3A%20%27B%27%2C%20wave%3A%20%20%271...0......%27}%2C%0A%20%20{name%3A%20%27C%27%2C%20wave%3A%20%20%271..........%27}%0A%20%20]%2C%0A%20%20{}%2C%0A%20%20[%27Intermediário%27%2C%0A%20%20{name%3A%20%27n2%27%2C%20wave%3A%20%27d..........%27}%2C%0A%20%20{name%3A%20%27n1%27%2C%20wave%3A%20%27d..........%27}%2C%0A%20%20]%2C%0A%20%20{}%2C%0A%20%20[%27Saída%27%2C%0A%20%20{name%3A%20%27Y%27%2C%20wave%3A%20%20%27d..........%27}]%2C%0A]%2C%0A%20%20head%3A{%0A%20%20%20text%3A%27Tabela%20de%20Temporização%27%2C%0A%20%20%20tick%3A0%2C%0A%20}%2C%0A%20foot%3A{%0A%20%20%20text%3A%27Tempo%20em%20Unidades%20de%20Propagação%27%2C%0A%20%20%20tick%3A0%0A%20}%2C%0A}"  target="_blank"><b>Editar a Carta de Temporização</b></a>

***

<div class="bloco solucao" id="sol-2">
<div class="conteudo">

A carta de tempos está na figura abaixo. Em seguida está uma explicação com detalhes sobre o resultado.

![**Carta de Tempo da Solução**](imagensComponentes/temporizacaoGlitch-A-1a.svg#800)

<br>

Na figura abaixo, é possível seguir a sequência de eventos das transições com mais detalhes.

A transição do sinal _B_ afeta tanto o caminho crítico quanto o caminho curto.

No caminho curto, a mudança de _B_ (de 1 para 0) implica na mudança de _n2_ após uma unidade de tempo de propagação. E, consequentemente, _n2_ implica na mudança da saída _Y_, de nível alto para nível baixo, após outra unidade de tempo de propagação. Ou seja, a saída mudou o seu estado após duas unidades de tempo de propagação, uma para a porta _AND_ e outra para a porta _OR_.

No caminho crítico, a mudança de _B_ (de 1 para 0) implica na mudança de _n1_ após duas unidades de tempo de propagação (uma unidade para a porta inversora e outra para a porta _AND_). Por sua vez, a mudança de _n1_ faz com que a saída mude após uma unidade de propagação (referente à porta _OR_). Assim, a saída muda de 0 para 1 após três unidades de propagação.

![**Sequência de Eventos nos Caminhos Crítico e Curto**](imagensComponentes/glitch-A-2.svg#p40 "Influência das Características de Temporização")

Essa sequência tem como resultado a aparição de uma transição indesejada na saída do circuito, ou seja, um _glitch_.

Neste caso, o _glitch_ que aparece na saída, com a mudança somente do sinal _B_ de 1 para 0, pode ser previsto pelo mapa de Karnaugh. Lembre que o mapa de Karnaugh representa a função booleana através da _soma_ de _produtos_, sendo que os produtos podem usar quaisquer valores de entrada ou o complemento desses valores. Ou seja, portas inversoras para o complemento, portas _AND_ para o produto e uma porta _OU_ para a soma de todos produtos.

No mapa abaixo, temos os _produtos_ em vermelho (_BC_) e verde (_\~A\~B_), que, _somados_, são o resultado da simplificação do circuito. Vale notar que, se os sinais _A = 0_ e _C = 1_ estiverem estáveis e ocorrer uma transição de 1 para 0 em _B_, haverá a desativação do produto _BC_ e a ativação do produto _\~A\~B_. Assim, antes da transição, quem determina o valor da saída é o produto _BC_. Após a transição, quem determina o valor de saída, é o produto _\~A\~B_. Esse é o problema, durante a transição não existe um produto que mantenha a saída em nível alto. Portanto, a saída estará em 0 durante a transição.

![**Mapa de Karnaugh com Realce na Transição de B Acima**](imagensComponentes/glitch-A-1-Karnaugh-detalhado.svg#400)


Esse problema pode ser solucionado através da inclusão de mais um produto, cobrindo a transição. Esse produto é mostrado, em verde, na tabela abaixo e é o _\~AC_.

Durante a transição, os valores de _A_ e _C_ estão estáveis, respectivamente, em nível baixo e nível alto. Isso preenche a condição do produto _\~AC_ e manterá a saída em nível alto.

![**Mapa de Karnaugh para Eliminação do Glitch**](imagensComponentes/glitch-A-1-KarnaughSemGlitch.svg#400)

O resultado será um circuito um pouco maior, mais uma porta _AND_, mas sem transições indesejadas na saída. Esse circuito está mostrado abaixo:

![**Mapa de Karnaugh do Circuito Acima**](imagensComponentes/glitch-A-1-Eliminado.svg#600)

</div><button onclick="exibe(this)">Ver Solução</button>
</div>

***

## Referências

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...


<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).



***

<br>

***

***

<!---
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[vhdlBasico]: ./vhdl/_vhdlBasico.html

[bibliotecaTemplates]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[renertaVHDLRefGuide]: http://vhdl.renerta.com

[freeRangeTutoriais]: http://freerangefactory.org/books_tuts.html

[VHDLTutorialElsevier]: http://booksite.elsevier.com/9780124077263/downloads/VHDL_Tutorials/vhdl-tutorial.pdf

[linksUteis]: ./linksUteis.html

[resourcesCOD4Ed]: https://booksite.elsevier.com/9780123747501/downloads/Resources.zip

<!-- FIM -->
