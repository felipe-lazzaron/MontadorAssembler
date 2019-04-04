<a name="inicio"></a>

# Atividades

Antes das atividades práticas, será necessário ler e discutir:

-   A especificação do [projeto 2][projeto2] (processador de 32 bits *);

-   A arquitetura do [processador MIPS DLX][arqMIPS];

-   As [instruções][instrucoesDLX] que serão implementadas nesse processador;

> *O processador que implementaremos é o MIPS DLX, uma versão simplificada do MIPS original.

---

## 1) Simular as instruções que serão implementadas

Para tomar contato com o MIPS e seu conjunto de instruções, utilizaremos:

-   Um simulador para o MIPS, o QtSpim;

-   Um [código de referência][somaVetores] que deve ser estudado;

-   E convertido para uma versão que utilize somente as instruções que serão implementadas (opções A e B).

Além disso, utilizaremos o [ _green card_ ][greenCard] do MIPS, que explica o funcionamento de todas as instruções e pseudo instruções.

É importante se acostumar a consultar o _green card_. Ele possui, reunidas em duas páginas, uma grande quantidade de informações sobre o processador.

### Contextualização

O QtSpim é um simulador da arquitetrua MIPS-32, que possui [mais instruções][SPIM] que o MIPS original. Além das instruções extras, ele possui alguns recursos, como:

-   Interpretar o código _assembly_ diretamente;

-   Um sistema de _debug_;

-   Algumas chamadas de sistema operacional (_syscall_);

-   Suporta as pseudo instruções do montador do MIPS;

-   Possibilidade de ativar ou desativar o _delayed load_ e o _delayed branch_.

A ordenação dos bytes na memória segue a convenção da máquina em que o SPIM está rodando (no caso, os processadores Intel são _little endian_).

#### Chamadas do Sistema

O QtSpim suporta 16 chamadas de sistema. As que poderemos utilizar estão mostradas na tabela abaixo:

 | Serviço | Código | Entrada | Saída |
 | --------- | :--: |----------------------| -------------- |
 | Imprime Inteiro | 1 | \$a0 = inteiro | |
 | Imprime _String_ | 4 | \$a0 = endereço inicial da _string_ (terminada com _NULL_) | |
 | Leitura de Inteiro | 5 |   | \$v0 = inteiro digitado no console |
 | Leitura de _String_ | 8 | \$a0 = endereço inicial do _buffer_. \$a1 = comprimento do _buffer_ ||
 | Terminar | 10 | | |
 | Imprime _Char_ | 11 | \$a0 = caractere |   |
 | Leitura de _Char_ | 12 | | \$v0 = caractere digitado  |

#### Organização da Memória

Ele utiliza a mesma convenção de segmentos de memória que o MIPS.
Na inicialização, os ponteiros estão com os seguintes valores:

-   O _stack pointer_ aponta para: 0x7FFFFFFC;

-   O _global pointer_ aponta para: 0x10008000;

-   O _program counter_ aponta para: 0x00400000;

![**Mapa de Memória do SPIM**](./imagensMIPS/mapaMemoriaMIPS-1.svg)

<br>

Uma lista das instruções que serão impelementadas, com a explicação do seu funcionamento, pode ser encontrada [aqui][instrucoesDLX].

Um resumo da arquitetura do MIPS pode ser visto [aqui][arqMIPS].

Caso não tenha feito o download do QtSpim, clique [aqui][DwQtSpim].

---

## Objetivo

Utilizaremos o QtSpim, para analisar o funcionamento das instruções que serão implementadas **(opções A e B)** no _hardware_. As instruções da opção A são:

-   Carrega palavra (_load word: lw_);

-   Armazena palavra (_store word: sw_);

-   Soma (_add_);

-   Subtração (_sub_);

-   E lógico (_and_);

-   OU lógico (_or_);

-   Comparação Menor Que (_set if less than: slt_);

-   Desvia Se Igual (_branch equal: beq_);

-   Salto incondicional (_jump: j_).


Para auxiliar na construção do programa, outras instruções podem ser utilizadas.

Também faça uso das instruções da opção B.

### Familiarizando-se com o QtSPim

Inicialmente iremos nos familiarizar com o QtSpim.

E, para entender o que o projeto original do MIPS passou de responsabilidades para o montador/compilador, faremos alguns programas com a configuração:

-   MIPS Simple Machine.

Os programas devem executar as seguintes tarefas:

-   Impressão de um valor inteiro no console;

-   Impressão de uma _string_ no console;

-   A soma de dois vetores, criando um terceiro vetor (veja o [programa de referência][somaVetores]). Além disso, ele deve:

    -   Imprimir o resultado da soma, passo a passo, no console;

    -   Quando terminar, deve fazer um salto para a rotina de finalização do programa:

        -   Que escreverá fim no console.

-   Com a memória ainda contendo os valores do programa anterior:

    -   Subtrair do vetor de resultados, os valores do primeiro vetor;

    -   Imprimir os resultados, passo a passo, no console;

    -   Ao término, fazer um salto para a rotina de finalização do programa (a mesma rotina do programa de soma).

Não se esqueça de guardar os fontes desses programas.

Para auxiliar na execução, utilize o livro sobre o [QtSpim][qtspim], que também está [aqui][qtSpimLocal].

Para diminuir a digitação, tem um modelo de programa _assembly_ [aqui][modeloASM].

A ajuda do QtSPim possui (**vale a pena verificar**):

-   Informações sobre o uso do programa;

-   O conteúdo do apêndice A do livro texto:

    -   Sobre montadores e programação do MIPS.

Aqui tem um resumo das [diretivas aceitas pelo SPIM][e9dc8ad3].


### Executando diretamente no MIPS

Porém, durante o teste da sua implementação do MIPS, pode ser necessário executar alguns programas sem o auxílio do montador.

Para entender essa diferença, execute os programas anteriores utilizando a configuração:

-   MIPS Bare Machine.

<!---

### Limitando-se às Instruções que serão Implementadas

Entendidas as diferenças, vamos nos acostumar a utilizar somente as instruções que serão implementadas. Para tanto, iremos refazer os programas somente com essas instruções e utilizando a configuração:

-   MIPS Bare Machine.

Analise as limitações e indique qual instrução, que não está implementada, facilitaria a programação.

--->

---

<br>

#### Referências

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

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
[instrucoesDLX]: ./MIPS/_instrucoesDLX.html

[arqMIPS]: ./MIPS/_arquitetura.html

[linksUteis]: ./linksUteis.html

[modeloASM]: ./MIPS/_modeloProgSpim.html

[qtspim]: http://www.egr.unlv.edu/~ed/mips.html

[qtSpimLocal]: ./MIPS/MIPStextSMv11.pdf

[DwQtSpim]: https://sourceforge.net/projects/spimsimulator/

[e9dc8ad3]: ./MIPS/_diretivasSPIM.html "Diretivas de montagem"

[greenCard]: ./MIPS/COD_4e_GreenCard.pdf

[somaVetores]: ./MIPS/_programaSomaVetores.html

[projeto2]: ./Projetos/Projeto-2.html

[SPIM]: ./MIPS/_spim.html
