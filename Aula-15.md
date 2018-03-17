<a name="inicio"></a>

# Atividades

Ir para o [fim do documento](#fimDocumento) e referências.

---

## 1) Projetar o controlador da ULA do MIPS DLX

### Contextualização

Uma solução adotada no MIPS DLX foi a divisão da unidade de controle em duas partes:

-   Unidade de Controle da ULA;

-   Unidade de Controle do Fluxo de Dados.

![Decodificação em duas etapas](./imagensMIPS/decoder2unidadesVisaoGeral.svg)


Na ULA, temos 4 pontos de controle com as seguintes funções:

-   InverteA:

    -   Inverte a entrada A da ULA (bit a bit). Juntamente com InverteB, implementa a função NOR;

-   InverteB:

    -   Inverte a entrada B da ULA (bit a bit). No primeiro bit, está conectado com o Carry In para fazer o complemento de 2;

-   Seleção:

    -   Dois bits para determinar a entrada do MUX que será enviada para a saída.

![ULA MIPS DLX](./imagensMIPS/ULA32bits(MIPS)pq.svg)

Para compatibilidade com o descrito no livro texto, utilizaremos a seguinte ordenação para os bits da palavra de controle da ULA:

Bit|Função
-----|----
bit 3|InverteA
bit 2|InverteB
bit 1|bit 1 da seleção do MUX
bit 0|bit 0 da seleção do MUX

<br>

---

### Objetivo

Definir o circuito da Unidade de Controle da ULA para que:

-   Execute as operações necessárias para a implementação de cada uma das instruções abaixo:

    -   Carrega palavra (_load word: lw_);

    -   Armazena palavra (_store word: sw_);

    -   Soma (_add_);

    -   Subtração (_sub_);

    -   E lógico (_and_);

    -   OU lógico (_or_);

    -   Comparação Menor Que (_set if less than: slt_);

    -   Desvia Se Igual (_branch equal: beq_);

    -   Salto incondicional (_jump: j_).

### Procedimento

Para tanto, precisamos correlacionar os códigos das instruções com a operação desejada da ULA. Uma forma simples, é a utilização de tabelas com:

-   As informações de entrada, que já são conhecidas;

-   O resultado desejado na saída.

De posse dessa tabela preenchida, podemos visualizar as possíveis otimizações, ou mesmo utilizar Karnaugh.

#### Palavra de Controle da ULA (ULActrl)

Inicialmente, precisamos definir o conteúdo da palavra de controle:

-   Para cada operação que a ULA deverá executar;

-   Considerando as informações acima.

|Função|ULActrl
:-------:|:----------:
|AND| |
|OR| |
|ADD|  |
|SUB|  |
|SLT|  |
|NOR|  |

Esses serão os nossos sinais de saída.

#### Sinais de Entrada

Como a intenção é trabalhar com duas unidades de controle separadas, iremos analisar todas as entradas e procurar uma forma de separação que também simplifique a implementação.

Os sinais de entrada são os bits que definem a instrução a ser executada. Eles são:

-   Campo de _opcode_ (bit 31 até bit 26) da instrução;

-   Campo de _funct_ (bit 5 até bit 0) da instrução;

#### Tabelas

Para preencher a [tabelas][tabelasULA], com o mapeamento das entradas e saídas, utilizaremos as informações acima e o _green card_.

A análise dessas tabelas deve permitir a substituição dos _opcodes_ por um sinal intermediário (chamado de ULAop). Esse sinal será gerado pela Unidade de Controle do Fluxo de Dados e enviado para a Unidade de Controle da ULA.

O resultado deve ser parecido com a tabela abaixo:

ULAop|Operação
-----|--------
XX|ADD
XY|SUB
XZ|etc
YY|etc
YZ|etc

A otimização pode ser feita manualmente ou utilizando programas.

#### Implementação

De posse das equações, ou circuito, deve ser feita:

-   A implementação em VHDL;

-   O teste de funcionamento;

-   O envio do código VHDL e _printscreen_ do teste.

---

<br>

#### Referências

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

---

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!--
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[tabelasULA]: ./MIPS/_tabelasULA.html

[linksUteis]: ./linksUteis.html
