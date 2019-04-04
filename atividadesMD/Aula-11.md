<a name="inicio"></a>

# Aula 11: Decomposição de Instruções do Tipo I

## Contextualização

### Instruções do tipo I

As instruções desse tipo:

-    Não possuem só uma opção para o campo de opcode, como as do tipo R;

-    Possuem dois campos de registradores: Rs e Rt;

-    Possuem um campo  com um valor imediato:

    -    Esse valor, de 16 bits, está codificado na instrução;

    -    E representa um **inteiro com sinal**.

São utilizadas para:

-   Carregar valores imediatos (constantes) nos registradores;

-   Fazer operações lógicas e aritméticas com valores imediatos, por exemplo:

```asm
            addi rs, rt, #valor;
```

-   Escrever na memória (sw);

-   Ler da memória (lw);

-   Fazer desvios condicionais (beq).

<br>

As instruções desse tipo, para a nossa implementação, são:

-   Load word: lw;

-   Store word: sw;

-   Branch on equal: beq.

<br>

### Formato das instruções do tipo I

Lembrando dos campos existentes, no MIPS DLX, para as instruções em geral:

| opcode | Rs | Rt | Rd | shamt | funct |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |
| MSB (b31) ||||| LSB (b0) |


A instrução do tipo I agrupa os campos:

-   **Rd**

-   **shamt**

-   **funct**

Para formar o campo **imediato**, necessário ao funcionamento dessa instrução.

| opcode | Rs | Rt | imediato |
|--------|----|---|----- |
| 6 bits | 5 bits | 5 bits | 16 bits |
|         |          |          |         |
|         |          |          |         |
|         |          |          |         |
|31~26 | 25~ 21 | 20~16 | 15~0 |

***

#### Exemplo de Branch on Equal

Sintaxe:

```asm
    beq  $rs,  $rt,  imediato
```

Sua operação:

> PC += (R[rs] == R[rt] ? 4 + distancia : 4);

Onde:

distancia=(14@imediato<15>#imediato<15..0>#0#0);


#### Exemplo de Load

Sintaxe:

```asm
    lw  $rt,  imediato($rs);
```

Operação:

> R[rt] = M[R[rs]+extSinal(imediato)]

Onde:

extSinal = (16@imediato<15>#imediato<15..0>)



#### Exemplo de Store

Sintaxe:
```asm
    sw  $rt,  imediato($rs);
```

Operação:

> M[R[rs]+extSinal(imediato)] = R[rt]

Onde:

extSinal = (16@imediato<15>#imediato<15..0>)

***

<br>

## Exercício A

Para a instrução:

```asm
  beq  $t0, $t1, 0x500:
```

Qual seria a sua codificação?

| opcode | Rs | Rt | imediato |
|:--------:|:----:|:---:|:-----:|
| 6 bits | 5 bits | 5 bits | 16 bits |
|         |          |          |         |
|<input type="text" id="A1" value="" maxlength="6" size="6" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="A2" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="A3" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="A4" value="" maxlength="16" size="16" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> |
|         |          |          |         |
|31~26 | 25~ 21 | 20~16 | 15~0 |


<div class="bloco solucao" id="sol-ExA">
<div class="conteudo">
<p style="color:red">Solução:</p>

| opcode | Rs | Rt | imediato |
|:--------:|:----:|:---:|:-----:|
| 6 bits | 5 bits | 5 bits | 16 bits |
|         |          |          |         |
| 000100 | 01000 | 01001 | 0000.0101.0000.0000 |
|          |            |           |          |
|31~26 | 25~ 21 | 20~16 | 15~0 |


</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

***

<br>

## Exercício B

Para a instrução:
```asm
    lw  $t0,  0x48($sp)
```
Qual seria a sua codificação?


| opcode | Rs | Rt | imediato |
|--------|----|---|----- |
| 6 bits | 5 bits | 5 bits | 16 bits |
|         |          |          |         |
|<input type="text" id="B1" value="" maxlength="6" size="6" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="B2" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="B3" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="B4" value="" maxlength="16" size="16" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> |
|         |          |          |         |
|31~26 | 25~ 21 | 20~16 | 15~0 |


<div class="bloco solucao" id="sol-ExB">
<div class="conteudo">
<p style="color:red">Solução:</p>

| opcode | Rs | Rt | imediato |
|:--------:|:----:|:---:|:-----:|
| 6 bits | 5 bits | 5 bits | 16 bits |
|         |          |          |         |
| 100011 | 11101 | 01000 | 0000000001001000 |
|          |            |           |          |
|31~26 | 25~ 21 | 20~16 | 15~0 |



</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

***

<br>

## Exercício C

Para a instrução:
```asm
    sw  $t1,  4($sp):
```

Qual seria a sua codificação?

| opcode | Rs | Rt | imediato |
|--------|----|---|----- |
| 6 bits | 5 bits | 5 bits | 16 bits |
|         |          |          |         |
|<input type="text" id="C1" value="" maxlength="6" size="6" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="C2" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="C3" value="" maxlength="5" size="5" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="C4" value="" maxlength="16" size="16" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> |
|         |          |          |         |
|31~26 | 25~ 21 | 20~16 | 15~0 |


<div class="bloco solucao" id="sol-ExC">
<div class="conteudo">
<p style="color:red">Solução:</p>

| opcode | Rs | Rt | imediato |
|:--------:|:----:|:---:|:-----:|
| 6 bits | 5 bits | 5 bits | 16 bits |
|         |          |          |         |
| 101011 | 11101 | 01001 | 0000000000000100 |
|          |            |           |          |
|31~26 | 25~ 21 | 20~16 | 15~0 |

</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

***

<br>

## Atividade

Faça a análise das instruções anteriores:

-   Na sequência:

    -   LW, SW e BEQ (fica mais fácil).

-   Descreva o funcionamento RTL da arquitetura para implementá-las;

-   Esboce o caminho de dados;

Simule o funcionamento de cada instrução;

-   Se não estiver bom, reinicie o processo.

Com o caminho de dados pronto:

-   Implemente em VHDL e simule.

Quando estiver funcional:

-   Mescle com o caminho de dados para as instruções do tipo R.

-   Implemente no kit de desenvolvimento:

-   E faça os testes necessários.

#### Dicas

Para determinar a estrutura de hardware necessária para implementar instruções do tipo I, veremos suas características.

As instruções do tipo I:

-   Utilizam 2 registradores;

-   O campo opcode define qual instrução será executada;

-   O campo "imediato" possui um inteiro, com sinal, de 16 bits (complemento de 2).

A função dos registradores:

-   Rt contém um argumento da operação;

-   Rs é o destino do resultado da operação.

A instrução **LW**:

```asm
    lw  $rt,  imediato($rs);
```

Carrega o dado, em _\$rt_, da posição da memória principal indicada por _imediato(\$rs)_.

Onde, o valor do _imediado_ é somado ao valor de _\$rs_ e deverá ser o endereço da memória.

Para somar o _imediato_, precisamos estender o seu sinal.

O conteúdo desse endereço será escrito no registrador _\$rt_.

Para executar essas funções, precisaremos de:

**Memória:**

![](imagensComponentes/MemoriaRAM(dados).svg){width=400px}

![](imagensComponentes/memoriaROM(Instrucoes).svg){width=300px}

**Banco de Registradores:**

![](imagensComponentes/arquivoRegistradores-1.svg){width=400px}

**Extensor de Sinal:**

![](imagensComponentes/extensorSinal.svg){width=400px}

**ULA:**

![](imagensComponentes/ULA.svg){width=400px}

**Registradores:**

![](imagensComponentes/registradorGenerico&EnablePCFS.svg){width=200px}

**Para mesclar com o FD das instruções do tipo R, precisaremos do MUX:**

![](imagensComponentes/Multiplexer_N-2N.svg){width=300px}

<br><br>

Para iniciar, use o fluxo de dados das instruções do tipo R como referência:

![](imagensMIPS/fluxoInstrucoesAritmeticasComentado-a.svg){width=800px}

***

## Referências

### RTN

<div class="bloco solucao" id="RTN">
<div class="conteudo">
<p style="color:red">Conteúdo:</p>


**Básico sobre RTN (register transfer notation)**

**Formaliza a descrição:**

-   Do funcionamento:

    -   RTN abstrata, usa a arquitetura;

-    Da estrutura:

    -   RTN concreta, usa a organização:

        -  Cada passo é um pulso de clock.

-   É um misto de linguagem natural e expressões matemáticas:

    -   Estabelece a relação entre o que está do lado esquerdo do símbolo com o que está do lado direito.

-   As transferências só acontecem no pulso de clock;

-   Considera que os sinais estão estáveis no momento do clock;

-   Considera que a lógica combinacional tem resposta instantânea.

<br>

**Símbolos Utilizados:**

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

<br>

**Exemplos:**

-   Flip-flop: A ← B

-   Registrador: A<m..1> ← B<m..1>

-   Incremento do PC: PC ← PC + 4

-   Carrega instrução da memória:

    -   RTN abstrata:

        -   IR ← M[PC]

    -   RTN concreta:

        -   MAd ← PC : C ← PC + 4

        -   MD ← M[MAd] : PC ← C

        -   IR ← MD

-   Extensão de sinal de 16 para 32 bits, do Reg1:

    -   (16@Reg1<15>#Reg1<15..0>)

-   Seleção de registrador (rn) no banco de regs.:

    -   A ← (rn = 0 → 0 : rn != 0 → R[rn] )

</div>
<button onclick="exibe(this)">Ver Conteúdo</button>
</div>

***

Solução do fluxo de dados para _lw_ e _sw_:

<div class="bloco solucao" id="sol-FDTipoI">
<div class="conteudo">
<p style="color:red">Solução:</p>

![](imagensMIPS/decomposicaoInstrucoes_Lw_Sw_cicloUnico-a.svg "Não Disponível"){width=800px}

</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

***

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

