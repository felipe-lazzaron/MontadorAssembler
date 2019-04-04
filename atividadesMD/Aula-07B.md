<a name="inicio"></a>

# Aula 7: Temporização em Circuitos Digitais - Continuação

## Temporização na Lógica Sequencial

### Contextualização

Os circuitos lógicos sequenciais são caracterizados pela presença de um sinal de _clock_, que determina o momento em que as transições devem ocorrer.

Vamos nos limitar ao circuito do registrador, que é composto de um ou mais _flip-flops_ do tipo _D_ - como mostrado abaixo.


   |                              Flip Flop                              | Registrador de 8 bits |
   | :----------------------------------------------------------------: | :-----------------------------------------------------------: |
   | ![Flip-Flop do tipo D](imagensComponentes/FF_D.svg) | ![Registrador de 8 bits](imagensComponentes/registrador_8bits_PCFS-1.svg){ width=40% } |

Nesse tipo de circuito, a transição do _clock_ determina o momento da transferência do sinal de entrada (**_D_**) para a saída (**_Q_**). Apesar de existirem flip-flops sensíveis à transição de subida (ou borda de subida) e à transição de descida (ou borda de descida), trataremos somente do primeiro caso. O segundo caso funciona de forma similar.

O funcionamento do _flip-flop_ tipo D segue as condições mostradas na tabela abaixo:

  | CLK | D | Q | | Comentário |
  |:---:|---|---|---|---|
  | 0 | X | Q | | Mantém o estado anterior |
  | 1 | X | Q | | Mantém o estado anterior |
  | ↑ | 0 | 0 | | O valor de D atinge a saída Q após o tempo de propagação |
  | ↑ | 1 | 1 | | O valor de D atinge a saída Q após o tempo de propagação |

#### Disciplina Dinâmica

São as regras de temporização que garantem que o circuito sequencial funcione corretamente. Elas estabelecem os tempos, em relação ao _clock_, necessários para os sinais de entrada e saída se mantenham estáveis.

Com relação aos sinais de entrada, temos:

-   O _setup time_ (_tsetup_), que é o tempo mínimo que o sinal _D_ deve estar **estável antes** da borda do _clock_;

-   O _hold time_ (_thold_), que é o tempo mínimo que o sinal _D_ deve continuar **estável após** a borda do _clock_.


![**Temporização em Relação ao Sinal de Saída e o Clock**](imagensComponentes/generalSequentialTimingEntrada-1.svg#p30 "")

<br>

Com relação aos sinais de saída, temos:

-   O tempo de contaminação do _clock_ até a saída _Q_ (_tccq_), que é o tempo mínimo que o sinal _Q_ inicia a sua alteração **após** a borda do _clock_;

-   O tempo de propagação do _clock_ até a saída _Q_ (_tpcq_), que é o tempo máximo que o sinal _Q_ demorará para ficar **estável após** a borda do _clock_.


![**Temporização em Relação ao Sinal de Saída e o Clock**](imagensComponentes/generalSequentialTimingSaida-1.svg#p30 "")

<br>

A figura abaixo, mostra os sinais com relação às duas referências, entrada e saída.

![**Temporização em Relação ao Sinal de Saída e o Clock**](imagensComponentes/generalSequentialTiming-1A.svg#p30 "")

<br>

Para que o circuito do _flip-flop_ funcione adequadamente, o sinal de entrada deverá ficar estável no período entre o início de _tsetup_ e o término de _thold_ (ambos em relação ao momento do _clock_). Podemos chamar esse período de janela de estabilidade da entrada.

Porém, o que acontece se ocorrer uma transição do sinal _D_ dentro da janela de estabilidade da entrada?

-   A disciplina dinâmica seria desrespeitada.

#### Metaestabilidade

A consequência da quebra, ou desrespeito, da disciplina dinâmica é a ocorrência de um sinal metaestável.

Esse sinal se caracteriza pela indefinição do seu nível lógico por um período de tempo indeterminado. Isso é um problema para os circuitos que recebem um sinal externo assíncrono, como o apertar de um botão. Não é possível garantir que o botão não será apertado e ficará estável durante a janela de estabilidade da entrada.

![**Violação da Disciplina Dinâmica na Entrada**](imagensComponentes/Metaestabilidade-1.svg#p30 "")

O resultado dessa violação da disciplina dinâmica é a metaestabilidade na saída do _flip-flop_. A saída fica em um estado indefinido por um tempo que é uma variável aleatória, ou seja, indeterminado. Porém, a saída, em algum momento, alcançará um nível estável. O tempo decorrido entre a borda ativa do _clock_ e a  estabilidade do sinal de saída é chamado de tempo de resolução (_t\_res_). A figura abaixo mostra a característica geral da violação da disciplina dinâmica.

![**Consequência, na Saída, da Violação da Disciplina Dinâmica**](imagensComponentes/MetaestabilidadeSaida-1.svg#p30 "")

Uma conclusão interessante é que se a disciplina dinâmica for respeitada podemos considerar que _t\_res_ = _tpcq_.

***

## Atividades sobre Temporização na Lógica Sequencial

### Exercício A

O _pipeline_ é uma técnica de projeto digital muito utilizada. Praticamente todos os processadores atuais utilizam um _pipeline_. De uma maneira simples, ele consiste em isolar blocos de lógica combinacional entre registradores de fronteira (R1 e R2), como mostrado abaixo.

![**Pipeline**](imagensComponentes/pipeline-3.svg#p30 "")

O funcionamento do circuito pode ser entendido se considerarmos que a cada _clock_, os sinais de entrada, tanto de R1 quanto R2, são transferidos para as respectivas saídas.

Durante o período entre as bordas ativas de dois _clocks_ (clk_t1 e clk_t2) consecutivos, os sinais que chegaram à saída de R1 (após o _tpcq_ de clk_1) devem "atravessar" a lógica combinacional e estarem estáveis na entrada de R2 para serem amostrados pelo _clock_ clk_2.

Para essa situação, qual seria a frequência máxima do _clock_ para que não ocorra a violação da disciplina dinâmica e, consequentemente, o aparecimento de metaestabilidade?

Para os registradores, considere as seguintes características:

-   R1 = R2;

-   O _setup time_ é igual a _tsetup_;

-   O _hold time_ é igual a _thold_;

-   O tempo de contaminação do _clock_ até a saída _Q_ é igual a _tccq_;

-   O tempo de propagação do _clock_ até a saída _Q_ é igual a _tpcq_;

Para o bloco combinacional, considere:

-   O tempo de contaminação é igual a _tcd_;

-   O tempo de propagação é igual a _tpd_.

***

<div class="bloco solucao" id="sol-0">
<div class="conteudo">

<p style="color:red">Solução:</p>

Como condição inicial, consideraremos que os sinais, na entrada de R1, estão estáveis na ocorrência do primeiro _clock_.

Para chegar à frequência máxima, teremos que calcular o período mínimo de _clock_ (Tc) que respeite a disciplina dinâmica. Assim, o sinal na entrada de R1, após o primeiro _clock_, deve atravessar o próprio R1 e a etapa combinacional para chegar à entrada de R2 pelo menos _tsetup_ antes do segundo _clock_.

Podemos dizer que Tc deve ser maior ou igual a soma de _tsetup(R2)_ com os tempos de propagação dos outros componentes existentes no caminho dos dados.

Como já sabemos o momento de chegada, vamos considerar o que existe no caminho.

Após o primeiro _clock_, os sinais na entrada de R1 chegarão à sua saída (Q1) após o tempo de propagação de R1, ou seja, _tpcq(R1)_.

Desconsiderando qualquer atraso na interligação dos componentes (trilhas do circuito impresso), podemos dizer que o sinal de Q1 está estável na entrada do circuito combinacional em _tpcq(R1)_. E o mesmo sinal, estará estável na saída do circuito combinacional após um intervalo de _tpd(CL)_.

Assim, considerando a ordem em que os sinais fluem, teremos:

**Tc &ge; _tpcq(R1)_ + _tpd(CL)_ + _tsetup(R2)_**

Lembrando que R1 = R2, então seus tempos característicos serão os mesmos.

![Frequência Máxima do _Clock_](imagensComponentes/pipelineTimingBeetwenRegisters-1a.svg#p40)

</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

***

<br>

### Exercício B

Considerando o circuito anterior, como poderíamos, sem causar problemas de funcionamento, aumentar a frequência de funcionamento do _pipeline_?

![**Frequência Máxima do _Clock_**](imagensComponentes/pipeline-3.svg#p40)


<div class="bloco solucao" id="sol-1">
<div class="conteudo">

<p style="color:red">Solução:</p>

Como as características dos registradores não podem ser modificadas, temos que trabalhar com o tempo de propagação do circuito lógico combinacional.

Para tanto, podemos verificar se é possível separar a lógica combinacional em duas etapas e adicionar mais um registrador entre elas.

Para obter o máximo desempenho, o tempo de propagação de cada etapa deve ser o mesmo. Além disso, essa divisão em etapas não pode alterar o resultado da lógica combinacional.

![Aumentando a Frequência Máxima do _Clock_](imagensComponentes/pipeline-4.svg#p40)

Caso se consiga balancear os tempos de propagação das etapas, o _clock_ poderá ter a sua frequência praticamente dobrada.

</div><button onclick="exibe(this)">Ver Solução</button>
</div>

***

<br>

### Exercício C

Em muitos casos, não é possível desprezar os tempos de propagação na interligação entre o _clock_ de cada registrador, como fizemos anteriormente. Nesses casos, o _clock_ chega em momentos diferentes para cada registrador do circuito.

A variação máxima entre o tempo de chegada da mesma borda ativa do _clock_, entre os registradores, é chamada de _clock skew_. Abaixo temos uma figura explicativa desse fenômeno:

![_**Clock Skew**_](imagensComponentes/pipelineClockSkew-1.svg#p30)

Levando em consideração o _clock skew_, qual seria a equação para a frequência máxima do _clock_ para o circuito mostrado acima?

Considere que o valor do _clock skew_ seja igual a _tskew_.

***

<div class="bloco solucao" id="sol-2">
<div class="conteudo">

<p style="color:red">Solução:</p>

O sentido do fluxo de dados é de R1 para R2. A borda ativa do _clock_ acontece primeiro em R2 (esse momento será TckR2), e depois de um intervalo de _clock skew_, acontece em R1 (TckR1).

Utilizando uma notação indicadora de _clocks_ consecutivos como:  TckRx(1), TckRx(2), TckRx(3), ... , TckRx(i), TckRx(i+1), onde Rx indica o registrador em uso.

E usando como referência o momento de um _clock_ qualquer em R2, chamado de TckR2(i), e o mesmo _clock_ em R1, chamado de TckR1(i), podemos definir uma relação entre o momento do _clock_ nesses registradores:

TckR1(i) = TckR2(i) + _tskew_

Considerando o período mínimo de _clock_ para que o circuito funcione sem problemas, chamado de Tc, teremos o intervalo entre duas bordas ativas consecutivas dado por:

TckR2(i) + Tc = TckR2(i+1)

Consequentemente, o período mínimo do _clock_ será dado por:

Tc = TckR2(i+1) - TckR2(i)

Considerando que:

-   Existe uma defasagem de tempo entre o _clock_ em R1 e em R2;

-   O sinal parte de R1 no momento TckR1(i) e será utilizado em R2 em TckR2(i+1).

O tempo disponível, ou útil (Tu), para o sinal atravessar o circuito será:

Tu = TckR2(i+1) - TckR1(i)

Tu = TckR2(i+1) -  ( TckR2(i) + _tskew_ )

Tu = TckR2(i+1) - TckR2(i) - _tskew_

Como Tc = TckR2(i+1) - TckR2(i), teremos:

Tu = Tc - _tskew_

Ou seja, o tempo útil para o sinal sair de R1 e chegar a R2 é menor que o Tc. Dessa forma, o _tsetup_ de R2 fica comprometido, causando problemas no circuito.

![**_Clock Skew_ e a Violação de _tsetup_**](imagensComponentes/pipelineClockSkew-3a.svg#p30)


Uma solução é adicionar o tempo _tskew_ ao período do _clock_, diminuindo a frequência máxima.

Dessa forma, teríamos:

novoTc = Tc + _tskew_

E o tempo útil seria dado por:

Tu = novoTc - _tskew_

Tu = Tc + _tskew_ - _tskew_

Tu = Tc

Nesse caso, o _tsetup_ de R2 não ficaria comprometido.

A ocorrência de _clock skew_ pode ser compensada com uma diminuição da frequência do _clock_.

![**Solução: Tu = Tc + _Clock Skew_**](imagensComponentes/pipelineClockSkew-3b.svg#p30)


<br>

</div><button onclick="exibe(this)">Ver Solução</button>
</div>


***

### Exercício D

Levando em consideração o _clock skew_, qual seria a equação, para a frequência máxima do _clock_, para o circuito mostrado abaixo?

![_**Clock Skew**_](imagensComponentes/pipelineClockSkew-2.svg#p30)

Considere que o valor do _clock skew_ seja igual a _tskew_.


***

<div class="bloco solucao" id="sol-3">
<div class="conteudo">

<p style="color:red">Solução:</p>

Neste caso, temos a condição inversa à do exercício anterior.

O sentido do fluxo de dados é de R1 para R2. A borda ativa do clock acontece primeiro em R1 (esse momento será TckR1), e depois de um intervalo de _clock skew_, acontece em R2 (TckR2).

Utilizando uma notação indicadora de clocks consecutivos como: TckRx(1), TckRx(2), TckRx(3), ... , TckRx(i), TckRx(i+1), onde Rx indica o registrador em uso.

E usando como referência o momento de um clock qualquer em R1, chamado de TckR1(i), e o mesmo clock em R2, chamado de TckR2(i), podemos definir uma relação entre o momento do clock nesses registradores:

TckR2(i) = TckR1(i) + _tskew_

<p style="color:red">Continuar!!!!!!!</p>

![_**Clock Skew**_](imagensComponentes/pipelineClockSkew-2a.svg#p30)

<br>

![_**Clock Skew**_](imagensComponentes/pipelineClockSkew-2aa.svg#p30)

<br>

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

<!-- FIM -->

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

