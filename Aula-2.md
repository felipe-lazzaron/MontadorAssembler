<a name="inicio"></a>

## Objetivos:

1.  Rever blocos construtivos combinacionais.
2.  Usar Template do Quartus.
3.  Visualização RTL.


## Conteúdo:

*   [Multiplex](#mux);
*   [Circuitos aritméticos](#ula);

<!--
4.  Usar projeto hierárquico (Instanciar) em VHDL.
*   [Projeto hierárquico](#projHierarquico).
*   [Codificadores](#???)
*   [Decodificadores](#???);  -->

[Ir para o fim do documento](#fimDocumento) e referências.

## Implementações:

#### ** Para auxiliar, utilize:

-   Os [templates do Quartus][bibliotecaTemplates];
-   A [ajuda interna][vhdlBasico];
-   O site da Renerta, ou qualquer outro, que está listado nos [links úteis][linksUteis];
-   O livro sobre lógica digital (free pdf) Digital McLogic Design de Mealy & Mealy no fim da página dos [links úteis][linksUteis];

#### Dicas:

-   Pense qual resultado que deseja obter;
    -   Esboce no papel um diagrama representando esse objetivo;
    -   Ou uma tabela da verdade. Ou o que for mais adequado.
-   Monte a estrutura básica do VHDL no seu arquivo de trabalho:
    -   Utilize um componente por arquivo;
    -   O nome do arquivo deve ser o nome da entidade desse componente;
    -   Assim é mais fácil de reutilizá-lo no futuro.
-   Para alguns casos, o uso da configuração com *generics* permite:
    -   Criar componentes mais versáteis, com largura de entrada/saída configuráveis.
    -   Aumentando a possibilidade de reutilização desse código.
-   Verifique se o esquema RTL é funcionalmente similar ao seu objetivo de implementação.
-   Simule o funcionamento do seu circuito. Se houver uma tabela da verdade:
    -   Ela já indica os vetores de entrada e os resultados na saída.
    -   Caso não exista ou a quantidade de possibilidades é muito grande:
        -   Fique atento para os casos nos extremos da sua faixa de valores de entrada.

***

### Principais circuitos combinacionais.

A lógica combinacional permite criar uma variedade de circuitos. Porém, em termos de blocos funcionais, os principais são:

-   Multiplex;
-   Decodificador;
-   Somador;
-   Comparador;
-   A Unidade Lógica e Aritmética (ULA ou ALU).

A conexão adequada desses circuitos, e a adição de registradores, permite a criação de um caminho de dados (ou fluxo de dados). O projeto de um processador, ou qualquer circuito mais complicado, pode ser dividido em:

-   Fluxo de dados;
-   Unidade de controle.

***

<a name="mux"></a>

## 1) Multiplex 2x1 em VHDL (usando *generics*).

### Contextualização:

O multiplex, também chamado de MUX, é um componente combinacional muito utilizado em circuitos digitais. Ele permite a seleção de uma entrada, dentre as suas "n" entradas, que será direcionada para a saída. Abaixo, temos o símbolo, circuito e tabela da verdade de um Mux 2x1 (2 entradas e 1 saída).

![](imagensComponentes/circuitoSimboloMultiplex_2-to-1-svg.png)

Sel|Y
--|--
0 |A
1 |B

Pode-se pensar no Mux como sendo um componente com:

-   2^N portas de entrada;
-   Uma porta de saída;
-   Onde, a cada instante, a seletividade entre uma dada entrada "X" e a saída:
    -   Seja definida por um decodificador binário para decimal de N para 2^N;
    -   Que possui na sua entrada o valor binário do "endereço" da porta X.
-   Permitindo que o sinal da entrada X alcance a saída.

### Objetivo:

A ideia é implementar um Mux 2x1 que possua dois vetores (de bits) de entrada e um vetor de saída. O que permitirá a reutilização do componente é a possibilidade de configurar a largura (total de bits) desses vetores para o valor desejado, de forma simples.

Uma forma prática de reutilizar os circuitos criados é através do uso:

-   Da declaração *`generic`*:
    -   Uma forma de parametrizar o código, sendo possível alterar o parâmetro:
        -   A cada instanciação do componente;
        -   Ela é avaliada em tempo de compilação, pesquise a sua sintaxe e funcionamento;
-   E do tipo de dados ***std_logic_vector***:
    -   Veja a sua declaração e a forma de usar o parâmetro definido na *`generic`*;
    -   Em algum dos links fornecidos.

Serão feitas duas implementações:

-   Uma com a construção WHEN ELSE;
-   Outra com a WITH SELECT.

<a name="criaprojeto"></a>

Antes de começar a descrever o circuito:

-   Crie um [novo projeto][novoProjeto];
-   Crie o [arquivo inicial][recursosQuartus] com o mesmo nome que irá utilizar na entidade;
-   Adicione esse [arquivo ao projeto][adicionarArqProjeto];
-   Abra o arquivo e, utilizando o [*template*][bibliotecaTemplates], adicione as bibliotecas que serão utilizadas:
    -   [*Library Clause*][clausulaBiblioteca]: *`IEEE`*;
    -   [*Use Clause*][clausulaUse]:  *`ieee.std_logic_1164.all`*
-   Ainda com o [*template*][bibliotecaTemplates], crie a estrutura de trabalho:
    -   [*Entity*][entidade]. Se preferir, no fim da entidade, omitir o nome dela:
        -   Modifique a cláusula *`end`* para *`end entity`*.
    -   [*Architecture*][arquitetura]. Se preferir, no fim da arquitetura, omitir o nome dela:
        -   Modifique a cláusula *`end`* para *`end architecture`*

Para descrever o Mux, use o [*template*][bibliotecaTemplates] do Quartus de cada construção (como ponto de partida). Lembre-se das dicas acima.

[Compile o projeto][compilacao] e verifique a implementação através do [RTL Viewer][rtlViewer]. No início, é um pouco complicado entender o diagrama RTL, não se assuste  :-) .

Caso tenha algum problema na compilação, verifique que a entidade do arquivo atual é a [Top-Level Entity][topLevelEntity].

Para testar o funcionamento utilize a [simulação][simulacaoVWF]. Um ponto importante na simulação é saber quais os vetores de entrada que são significativos e qual a saída relativa a cada um deles.

***
<a name="ula"></a>

## 2) Circuitos aritméticos em VHDL.

### Contextualização:

Outro circuito combinacional muito utilizado é a Unidade Lógica e Aritmética (ULA).

Ela é composta de:

-   Duas entradas para os operandos em uso;
-   Uma unidade funcional para cada operação executada;
-   Um seletor entre os resultados das operações executadas.

O símbolo da ULA está mostrado abaixo, onde:

-   N: é a largura do vetor de bits para as entradas (A e B) e saída (Y).
-   m: é o seletor de função e depende da quantidade funções implementadas (#func):
    -   Sendo que a quantidade #func deve ser menor ou igual a 2^m.
-   Z: é o *flag* indicador de resultado igual a ZERO.

<br>

![](imagensComponentes/aluAula2.png)

### Objetivo:

Criar um segundo componente, utilizando um arquivo próprio, e implementar uma ULA com as seguintes funções:

-   Soma (A + B)   (tipo *unsigned*);
-   Subtração (A - B) (tipo *unsigned*);
-   AND (A and B);
-   OR (A and B);
-   NOT (not A)
-   Indicador (*flag*) de que o resultado é igual a ZERO.

Não trataremos o caso de *overflow* na soma e subtração.

Para padronizar, utilizaremos o seguinte código de escolha da função executada:

 função  | código  
---------|------
 Soma    | 0
 Subtrai | 1
 AND     | 2
 OR      | 3
 NOT     | 4
 reserva | 5
 reserva | 6
 reserva | 7

Se sobrar tempo, adicione estas funções:

-   Rodar 1 bit para a esquerda (dica: pesquise sobre *barrel-shifter*).
-   Comparação entre as duas entradas, indicando somente quando forem iguais:
    -   Adicione um *flag* para indicar valores iguais.

<br>

Crie um novo projeto, como [descrito acima](#criaprojeto), e inicie a sua codificação.

Para um chute inicial:

> No Quartus, existe um exemplo de somador/subtrator dentro de: *templates, VHDL, full designs*.

Usando esse *template* como base, ainda falta adicionar as outras funções e implementar o seletor.

[Compile o seu projeto][compilacao] e verifique a implementação através do [RTL Viewer][rtlViewer].

Para testar, use a [simulação][simulacaoVWF]. Não esqueça de definir vetores de teste significativos e as saídas correspondentes.

***

Se, mesmo assim, sobrou tempo:

-   Implemente o Mux usando um processo e uma construção *if* interna a esse processo.

<!--
### Exemplo de um somador completo para um bit:

![Somador](imagensComponentes/somadorCompleto.png)

--->

***

**Referências:**

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

***

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!---
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[vhdlBasico]:  ./vhdl/_vhdlBasico.html

[bibliotecaTemplates]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[simulacaoVWF]: ./quartus/_simulacao.html

[compilacao]: ./quartus/_compilarProjetoQuartus.html

[rtlViewer]: ./quartus/_rtlViewerQuartus.html

[novoProjeto]: ./quartus/_criarProjetoQuartus.html

[recursosQuartus]: ./quartus/_recursosQuartus.html

[adicionarArqProjeto]: ./quartus/_recursosQuartus.html#adicionar-um-arquivo-ao-projeto

[clausulaBiblioteca]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[clausulaUse]: ./quartus/_recursosQuartus.html#escolher-os-templates-de-interesse

[entidade]: ./quartus/_recursosQuartus.html#escolher-os-templates-de-interesse

[arquitetura]: ./quartus/_recursosQuartus.html#escolher-os-templates-de-interesse

[topLevelEntity]: ./quartus/_recursosQuartus.html#configurar-a-top-level-entity

<!---
#######################################
###########Links Externos##############
####################################### --->

[linksUteis]: ./linksUteis.html
