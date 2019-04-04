<a name="inicio"></a>

# Aula 6 - Atividade 1

Ir para o [fim do documento](#fimDocumento) e referências.

---

## Objetivos

Aplicar máquina de estados em um projeto simples.

## Máquina de estados microprogramada

Faremos uma máquina de estados para sequenciar as três primeiras letras do seu nome, na ordem correta e na ordem reversa. Para tanto, utilizaremos uma FSM microcontrolada.

<br>

### Contextualização

A máquina de estados, de uma maneira simplificada, é um dispositivo que percorre uma determinada sequência de passos.

<div class="figure">
<img src="./imagensFSM/diagramaEstadosSequenciaSimples.svg" alt="Sequência Simples" style="width:300px;"/><p class="caption">Sequência Simples</p>
</div>

Essa sequência de passos é definida durante o projeto da máquina. Ela pode ser:

-    Tão simples como a sequência de números entre 0 e 9;

-    Ou tão complexa como as atividades necessárias para executar uma instrução em um computador.


<div class="figure">
<img src="./imagensFSM/estadosMEF.svg" alt="MEF" style="width:500px;"/><p class="caption">Estados de Execução das Instruções do MIPS</p>
</div>

Para determinar, a cada passo (ou estado), qual será o passo seguinte, são necessárias duas informações:

-    O seu passo (estado) atual;

-    As entradas atuais.

Cada estado possui um conjunto de sinais que determinam a saída da máquina. Essa saída carrega consigo as informações que serão utilizadas no controle de um circuito.

A máquina de estados transforma o estado atual (codificado em algum padrão binário) e as variáveis de entrada, no próximo estado e nos sinais de saída.

<div class="figure">
<img src="./imagensFSM/maquinaEstadosMooreWikipedia-ptbr-1.svg" alt="Figura" style="width:600px;"/><p class="caption">Máquina de Estados</p>
</div>

Ou seja, é uma máquina que está sempre relacionando:

-   De onde veio (entradas e estado atual);

-   Para onde vai (próximo estado e saídas).

<div class="figure">
<img src="./imagensFSM/AlNaCordaBamba-2.png" alt="Sempre na Corda Bamba" style="width:500px;"/>
<p class="caption">Corda Bamba</p>
</div>

Pode-se implementar o circuito, de transformação de estado, através de uma memória. Onde a lógica de transição e de saída estarão armazenadas.


<div class="figure">
<img src="./imagensFSM/maquinaEstadosROM-pcfs-4-Grande.svg" alt="Figura" style="width:600px;"/><p class="caption">Máquina de Estados com ROM</p>
</div>

O endereçamento de cada posição dessa memória dependerá:

-   Das variáveis de entrada;

-   E do passo (estado) atual.

<div class="figure">
<img src="./imagensFSM/formatoEnderecoFSM_ROM.svg" alt="Figura" style="width:600px;"/><p class="caption">Formato do Endereço da ROM</p>
</div>

Cada posição dessa memória, determinada como mostrado acima, deve conter:

-   Sinal de saída para o estado atual;

-   O endereço do próximo estado.

<div class="figure">
<img src="./imagensFSM/formatoDadoFSM_ROM.svg" alt="Figura" style="width:600px;"/><p class="caption">Formato do Conteúdo da ROM</p>
</div>


> *Veja mais detalhes nas informações extras que acompanham esta aula (no blackboard).

<br>

### Dicas

Exemplo de código de inicialização de memória [em VHDL][initVHDL]. Ele também aborda a conversão do tipo usado no endereçamento.

Exemplo de código de inicialização de memória a partir do conteúdo de um [arquivo mif][initFile].

<br>

## Referências

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

---

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

***

<br>

***

***

<!-- FIM -->

<!--
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[initFile]: ./vhdl/_fileInitROM.html

[initVHDL]: ./vhdl/_inlineInitROM.html

[linksUteis]: ./linksUteis.html
