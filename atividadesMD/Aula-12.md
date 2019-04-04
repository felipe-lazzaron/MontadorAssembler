<a name="inicio"></a>

# Aula 12: Decomposição de Instruções do Tipo J

## Contextualização

### Instruções do tipo J

As instruções desse tipo:

-   Possuem uma única opção para o campo de opcode, como as do tipo R;

-   Possuem um campo  com um valor imediato:

    -   Esse valor, de 26 bits, está codificado na instrução;

    -   E representa um inteiro sem sinal.

-   São utilizadas para:

    -   Fazer desvios incondicionais no programa.

### Formato das instruções do tipo J

Lembrando dos campos existentes, no MIPS DLX, para as instruções em geral:

| opcode | Rs | Rt | Rd | shamt | funct |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |
| MSB (b31) ||||| LSB (b0) |


A instrução do tipo J agrupa os campos:

-   **Rs**

-   **Rt**

-   **Rd**

-   **shamt**

-   **funct**

Para formar o campo **imediato**, de 26 bits, que será ultilizado para definir o endereço de destino.

| opcode | imediato |
|--------|----|
| 6 bits | 26 bits |
|         |          |
|         |          |
|         |          |
|31~26 | 25~0 |

***

#### Exemplo de Jump

Sintaxe:

```asm
    j    endereço
```

Sua operação:

-   PC = endereço;

Onde:

endereço=(PC+4)[31..28],imediato<25..0>,0,0);

Note que não existe nenhuma operação de soma, portanto, o endereço é absoluto.

Como os quatro bits mais significativos são retirados do PC, estamos dividindo o espaço de memória em blocos ou páginas fixas.

O tamanho dessas páginas é definido pelo número de bits vindos do PC, neste caso: 4 bits. Dessa forma, teremos 16 ($2^4$) páginas diferentes.

O endereço de destino será um valor absoluto, de uma posição de memória, dentro da página corrente. A página é definida pelo valor de PC+4.

Como cada instrução ocupa 4 bytes, podemos dizer que o valor do imediato é o número de ordem, da instrução destino, dentro da página.


## Exercício A

Para a instrução:

```asm
  j 0x700:
```

Qual seria a sua codificação?

| opcode | imediato |
|:--------:|:----:|
| 6 bits | 26 bits |
|         |          |
|<input type="text" id="A1" value="" maxlength="6" size="6" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> | <input type="text" id="A2" value="" maxlength="26" size="26" onkeyup="validaBinario(id)" onchange="validaBinario(id)"> |
|         |          |
|31~26 | 25~0 |


<div class="bloco solucao" id="sol-ExA">
<div class="conteudo">
<p style="color:red">Solução:</p>

A instrução em assembly define o endereço de destino como:

> 0x700

Precisamos calcular o imediato que, após convertido, resulte em 0x700.

Esse endereço (0x700) convertido para binário e com 26 bits:

-   00.0000.0000.0000.0111.0000.0000

A conversão é dada por:

> endereço=(PC+4)[31..28],imediato<25..0>,0,0);

Então:

0x700=(PC+4)[31..28],imediato<25..0>,0,0);

Os 4 bits mais significativos são do valor do PC, que podemos ignorar.

Então:

0x700=(imediato<25..0>,0,0)

00.0000.0000.0000.0111.0000.0000=(imediato<25..0>,0,0);

Para eliminar os dois zeros da direita, fazemos dois deslocamentos para a direita (com preenchimento à esquerda com zero):

00.0000.0000.0000.0001.1100.0000=imediato<25..0>;

> imediato=0x01C0

| opcode | imediato |
|:--------:|:----:|
| 6 bits | 26 bits |
|         |          |
| 000010 | 00.0000.0000.0000.0001.1100.0000 |
|          |            |
|31~26 | 25~0 |


</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

***

<br>

## Atividade

Faça a análise das instruções anteriores:

-   Descreva o funcionamento RTL da arquitetura para implementá-las;

-   Esboce o caminho de dados;

-   Simule o funcionamento de cada instrução;

-   Se não estiver bom, reinicie o processo.

Com o caminho de dados pronto:

-   Implemente em VHDL e simule.

Quando estiver funcional:

-   Mescle com o caminho de dados das instruções:

    -   Do tipo R e do tipo I.

-   Implemente no kit de desenvolvimento:

    -   E faça os testes necessários.

#### Dicas

Para iniciar, use o fluxo de dados das instruções do tipo R e do tipo I como referência:

![](imagensMIPS/decomposicaoInstrucoes_R_I_cicloUnico.svg){width=800px}

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

