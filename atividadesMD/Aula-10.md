<a name="inicio"></a>

# Aula 10: Decomposição de Instruções do Tipo R

## Contextualização

Como visto anteriormente, o MIPS possui:

-   3 formatos básicos de instruções:

    -   Tipo R (registro);

    -   Tipo I (imediato);

    -   Tipo J (salto).

Além disso, a codificação dessas instruções:

-   Utiliza uma palavra de 32 bits;

-   Que foi dividida em campos bem definidos.

| opcode | Rs | Rt | Rd | shamt | funct |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |
| MSB (b31) ||||| LSB (b0) |

Esses campos são agrupados:

-   Dependendo do tipo de instrução.

***

O significado dos nomes dos campos:

-   Opcode: Contém o código da instrução a ser executada;

-   Rs: O número do registrador com o primeiro operando da instrução definida em op;

-   Rt: O número do registrador com o segundo operando da instrução definida em op;

-   Rd: O número do registrador de destino do resultado da instrução definida em op;

-   shamt: Total de deslocamento (shift amount).

-   funct: Seleciona uma variação específica da operação definida em opcode.


<br>

### Formato das instruções do tipo R

Analisaremos o formato das instruções do tipo R:

-   Para determinar a estrutura de hardware necessária para implementar esse tipo de instrução.

Todas instruções do tipo R:

-   Utilizam 3 registradores;

-   O campo opcode é sempre igual a zero;

-   O campo “funct” define a função a ser realizada.


A função dos registradores:

-   Rs e Rt contém os argumentos da operação;

-   Rd é o destino do resultado da operação.

Qual a codificação para a soma mostrada abaixo:

```asm
       add $t0, $s1, $s2
```

Dica:

>   Consulte valor de “funct” e o endereço dos registradores no greencard.

| opcode | Rs | Rt | Rd | shamt | funct |
|--------|----|---|----- |------- | ------- |
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |
|         |          |          |         |          |          |
|         |          |          |         |          |          |
|         |          |          |         |          |          |
|31~26 | 25 ~21 | 20 ~16 | 15 ~11 | 10 ~6 | 5 ~0 |



Agora que a codificação das instruções do tipo R, já é conhecida:

-   Vamos analisar o seu funcionamento.

***

### Blocos Construtivos Úteis para este Fluxo de Dados

Registrador de uso geral (n bits, configurável);

![](imagensComponentes/registradorGenerico&EnablePCFS.svg){width=200px}

Memória (RAM e ROM);

![](imagensComponentes/MemoriaRAM(dados).svg){width=400px}

Banco de Registradores;

![](imagensComponentes/arquivoRegistradores-1.svg){width=400px}

ULA:

-    Considere que a ULA executa qualquer operação lógica ou aritmética;

-    Quando acabar a analise de todas instruções, saberemos quais operações a ULA necessitará;

![](imagensComponentes/ULA.svg){width=400px}

MUX.

![](imagensComponentes/Multiplexer_N-2N.svg){width=300px}

<br>

### RTN

Básico sobre RTN (register transfer notation):

Formaliza a descrição:

    Do funcionamento. RTN abstrata: usa a arquitetura;

    Da estrutura. RTN concreta: usa a organização:

        Cada passo é um pulso de clock.

Misto de linguagem natural e expressões matemáticas:

    Estabelece a relação entre o que está do lado esquerdo do símbolo com o que está do lado direito.

As transferências só acontecem no pulso de clock;

Considera que os sinais estão estáveis no momento do clock;

Considera que a lógica combinacional tem resposta instantânea


Símbolo | Significado
:----:|------------------------------
<- | Transferência entre registradores: Regesquerda recebe o valor do Regdireita .
[ ] | Índice de Word: seleciona uma palavra, ou a faixa de palavras, da memória indicada.
< > | Índice de Bit: seleciona a faixa de bits ou um bit da memória indicada.
n...m | Índice de Faixa: indica a faixa da esquerda para a direita (pode ser decrescente).
-> | If-then: verdadeiro na esquerda implica receber valor ou aplicar ação na direita.
:= | Definição: ajuda a documentar. ld(opcode:=3) → R[ra] ← M[MA]
# | Concatenação de bits.
: | Separador de ações que acontecem em paralelo.
; | Separador de ações que acontecem em sequência: da esquerda para direita.
@ | Repete o número de vezes, da direita, o que está na esquerda (concatena).
{ } | Modificador de operação.
( ) | Agrupamento de operações ou valores.
= ≠ < ≤ ≥ > | Operadores de comparação, retorna valores binários (≠ pode ser: !=).
+ - * / | Operadores aritméticos.
^v¬⊕≡ | Operadores lógicos: and, or, not, xor, equivalência. Pode usar: & \| !


Exemplos:

        Flip-flop: A ← B

        Registrador: A<m..1> ← B<m..1>

        Incremento do PC: PC ← PC + 4

        Carrega instrução da memória:

            RTN abstrata: IR ← M[PC]
            RTN concreta:

        Extensão de sinal de 16 para 32 bits, do Reg1:
            (16@Reg1<15>#Reg1<15..0>)

        Seleção de registrador (rn) no banco de regs.:
            A ← (rn = 0 → 0 : rn != 0 → R[rn] )

MAd ← PC : C ← PC + 4

MD ← M[MAd] : PC ← C

IR ← MD
Memória
Memória

    Em relação ao modelo de memória que utilizaremos:
        As instruções estão na memória do computador:
            No segmento “text”.
        Dentro do processador existe uma memória específica para instruções;
        Que é separada da memória do computador:
            E alimentada através de um cache.

Análise
Análise

    Utilizando a definição da instrução “add”*:
        Defina os blocos construtivos necessários para executá-la;
        Descreva, em RTN, o fluxo entre esses blocos;
        Para cada comando RTN:
            Conecte os blocos construtivos necessários;
            Para que a instrução execute;
            E anote os pontos de controle utilizados.
        Faça um rascunho do fluxo de dados;
        Simule manualmente (papel e caneta).
        *A definição das instruções pode ser encontrada:
        No greencard;
        Na página de atividades (links úteis).

Quando o FD estiver pronto:

    Quando o FD estiver pronto:
        Verifique se atende o funcionamento de todas as outras instruções, do tipo R, que implementaremos:
            Subtração (sub);
            E lógico (and);
            OU lógico (or);
            Comparação Menor Que (set if less than: slt).
    Crie uma tabela com as instruções e os pontos de controle:
        Descrevendo o estado de cada ponto de controle;
        Para cada instrução implementada.

### Exemplo de tabela

    Exemplo de tabela:

        Com os sinais de controle;

        E as instruções.

Instrução  | CtrlR1 | CtrlR2 | OpALU | RegWr | MemRd | MemWr
:-----:|:-----:|:------:|:-----:|:-----:|:------:|:-----:
add |1|0|001|1|0|0
sub|0|1|010|1|0|0
…|...|...|…|...|...|...
slt|0|1|100|1|0|0



### Agora que o FD atende as instruções R

Implemente em VHDL;

    Verifique o funcionamento usando simulação:

        Use a tabela com os pontos de controle.

Implemente no kit de desenvolvimento:

    E faça os testes necessários.

## Atividade

### Exercício A

***

<div class="bloco solucao" id="sol-R">
<div class="conteudo">

<p style="color:red">Solução:</p>

Análise das Instruções tipo R

Como vimos, essas instruções possuem a seguinte expressão geral:

R[rd] ← R[s] operação R[t];

Utilizando a RTN abstrata, poderíamos decompor em:

IR ← M[PC] :  PC ← PC + 4;

Inst(opc:=xx) → R[rd] ← R[rs] operação R[rt]


Onde: inst = instrução executada;
          opc= opcode;
          operação = função definida no campo funct.


Considerando a RTN concreta e todas as etapas da execução:

Fetch: MEND ← PC : IR ← M[PC];

Decode:

UC ← IR<31..26> : CTRULA ← IR<5..0> :

RSEND ← IR<25..21> : RTEND  ← IR<20..16> :

RDEND  ← IR<15..11>;  C ← PC + 4;

Execute:  ULAA ← R[rs] : ULAB ← R[rt]

MemoryAccess: nada

WriteBack: RDWR ← True : R[rd] ← ULAOUT : PC ← C




Olhando apenas a etapa de “fetch”:

-   MEND ← PC : IR ← M[PC];

Podemos definir as unidades funcionais:

Memória;

![](imagensComponentes/MemoriaRAM(dados).svg){width=200px}

Registrador PC;

![](imagensComponentes/programCounter.svg){width=200px}

Registrador de Instruções (IR).

![](imagensComponentes/registradorGenerico&EnablePCFS.svg){width=200px}






memoriaROM(Instrucoes).svg

Multiplexer_N-2N.svg



Olhando apenas a etapa de “decode”:

UC ← IR<31..26> : CTRULA ← IR<5..0> :

RSEND ← IR<25..21> : RTEND  ← IR<20..16> :

RDEND  ← IR<15..11>;  C ← PC + 4;

Podemos definir as unidades funcionais:

Unidade de controle:

![](imagensComponentes/UC.svg){width=400px}

<br>

Banco de registradores:

![](imagensComponentes/arquivoRegistradores-1.svg){width=400px}

<br>

ULA:

![](imagensComponentes/ULA.svg){width=400px}

<br>

Somador para o PC:

![](imagensComponentes/somandorConstante.svg){width=400px}

<br>

Como estamos trabalhando com:

Memórias separadas para instruções e dados;

Podemos retirar o IR e interligar direto no Banco de Registradores.




A etapa de “execute”:

 ULAA ← R[rs] : ULAB ← R[rt]

Não adiciona nenhum componente novo.



A etapa de “memory access”:

Fica sem uso nesse tipo de instrução.



A etapa de “write back”:

RDWR ← True : R[rd] ← ULAOUT : PC ← C

Só mostra as transferências:

Como o PC já é um registrador;

Não é necessário o registrador intermediário: C.


A interligação final:


![**Fluxo de Dados para Instruções do Tipo R**](imagensMIPS/fluxoInstrucoesAritmeticasComentado-a.svg){width=800px}

</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

***

## Exercício C

Para a instrução:
```asm
    sw  $t1,  4($sp):
```

Qual seria a sua codificação?

| opcode | Rs | Rt | Rd | shamt | funct |
|--------|:----:|:---:|:-----:|:------:|:------:|
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |
|         |          |          |         |          |          |
|<input type="text" id="C1" value="" maxlength="6" size="6" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="C2" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="C3" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="C4" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> |<input type="text" id="C5" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)">|<input type="text" id="C6" value="" maxlength="6" size="6" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> |
|         |          |          |         |
|31~26 | 25~ 21 | 20~16 | 15~11 | 10~6 | 5~0 |


<div class="bloco solucao" id="sol-ExC">
<div class="conteudo">
<p style="color:red">Solução:</p>

| opcode | Rs | Rt | Rd | shamt | funct |
|:--------:|:----:|:---:|:-----:|:---:|:-----:|
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |
|         |          |          |         |
| 101011 | 11101 | 01001 | 00000 | 00000 | 000100 |
|          |            |           |          |           |          |
|31~26 | 25~ 21 | 20~16 | 15~11 | 10~6 | 5~0 |

</div>
<button onclick="exibe(this)">Ver Solução</button>
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

