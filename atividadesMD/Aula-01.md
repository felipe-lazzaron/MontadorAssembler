<a name="inicio"></a>

# Aula 1: Quartus e Circuitos Combinacionais

## Objetivos

1.  Rever o uso do Quartus.
2.  Usar Template do Quartus.
3.  Visualização RTL.
4.  Rever blocos construtivos combinacionais.

## Pré-requisitos

Ter o Quartus Prime instalado e funcional. Ele está disponível no site da Intel:

[Download Center for FPGAs](http://fpgasoftware.intel.com/?edition=lite   "Baixar Quartus Lite")

***

## Atividade: Uso do Quartus

### Criar projeto no Quartus Prime Lite

Crie um projeto no Quartus com o nome Aula1. Caso precise de auxílio, acesse a página:

[Criar Projeto no Quartus](./quartus/_criarProjetoQuartus.html)


### Compilar o Projeto

Uma vez criado o circuito, deve-se testar o seu funcionamento através de simulação.
Porém, para simular é preciso compilar o circuito. Existem três formas diferentes de fazer a compilação, veja no link abaixo:

[Compilar Projeto no Quartus][compilacao].

### Simular o Circuito

Para verificar o funcionamento do circuito criado, utilize uma simulação:

[Simular Circuito no Quartus][simulacaoVWF].

### Uso dos Templates do Quartus

Para os circuitos básicos, o Quartus provê um conjunto de modelos que obterão a melhor implementação para o circuito. Além disso, a _Intel_ indica como boa prática de projeto a utilização desses modelos.

[Acessar os templates][bibliotecaTemplates].

### Visualizar o Diagrama Lógico do Circuito (RTL)

Para verificar se o código criado é realmente o circuito desejado, utiliza-se:

[Visualização RTL][visualizacaoRTL].

***

## Atividade: Blocos Construtivos Combinacionais

**Para auxiliar, utilize:**

-   Os [templates do Quartus][bibliotecaTemplates];

-   A [ajuda interna][vhdlBasico];

-   O livro sobre lógica digital (free pdf) Digital McLogic Design de Mealy & Mealy no fim da página dos [links úteis][linksUteis];

**Dicas:**

-   Antes de codificar, pense qual resultado que deseja obter;

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

### Principais Circuitos Combinacionais

A lógica combinacional permite criar uma variedade de circuitos. Porém, em termos de blocos funcionais, os principais são:

-   Multiplex;

-   Decodificador;

-   Somador;

-   Comparador;

-   A Unidade Lógica e Aritmética (ULA ou ALU).

A conexão adequada desses circuitos, e a adição de registradores, permite a criação de um caminho de dados (ou fluxo de dados).

O projeto de um processador, ou qualquer circuito mais complicado, pode ser dividido em:

-   Fluxo de dados;

-   Unidade de controle.

A seguir, iremos implementar alguns desses circuitos combinacionais.

***

<a name="mux"></a>

## 1) Multiplex 2x1 em VHDL (usando *generics*).

### Contextualização

O multiplex, também chamado de MUX, é um componente combinacional muito utilizado em circuitos digitais. Ele permite a seleção de uma entrada, dentre as suas _"n"_ entradas, que será direcionada para a saída.

Abaixo, temos o símbolo, circuito e tabela da verdade de um Mux 2x1 (2 entradas e 1 saída).

| ![](imagensComponentes/circuitoSimboloMultiplex_2-to-1-svg.png) |
|:-------------------------:|
| Acima temos o símbolo e o circuito interno de um MUX com 1 bit do tipo 2x1.
Abaixo está a sua tabela da verdade. |

|Sel|Y|
|:--:|:--:|
| 0 | A |
| 1 | B |

Pode-se pensar no Mux como sendo um componente com:

-   2^N portas de entrada;

-   Uma porta de saída;

-   Onde, a cada instante, a seletividade entre uma dada entrada "X" e a saída:

    -   Seja definida por um decodificador binário para decimal de N para 2^N;

    -   Que possui na sua entrada o valor binário do "endereço" da porta X.

-   Permitindo que o sinal da entrada X alcance a saída.


### Objetivo

A ideia é implementar um Mux 2x1 que possua dois vetores (de bits) de entrada e um vetor de saída. O que permitirá a reutilização do componente é a possibilidade de configurar a largura (total de bits) desses vetores para o valor desejado, de forma simples.

Uma forma prática de reutilizar os circuitos criados é através do uso:

-   Da declaração *`generic`*:

    -   Uma forma de parametrizar o código, sendo possível alterar o parâmetro:

        -   A cada instanciação do componente;

        -   Ela é avaliada em tempo de compilação, pesquise a sua sintaxe e funcionamento;

-   E do tipo de dados ***std_logic_vector***:

    -   Veja a sua declaração e a forma de usar o parâmetro definido na *`generic`*;

    -   Em algum dos links fornecidos.

Serão feitas duas implementações, ambas com comandos VHDL combinacionais:

-   A construção **WHEN ELSE**;

-   E a construção **WITH SELECT**.

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

[Compile o projeto][compilacao] e verifique a implementação através do [RTL Viewer][visualizacaoRTL].

No início, é um pouco complicado entender o diagrama RTL, não se assuste  :-) .

Caso tenha algum problema na compilação, verifique que a entidade do arquivo atual é a [Top-Level Entity][topLevelEntity].

Para testar o funcionamento utilize a [simulação][simulacaoVWF]. Um ponto importante na simulação é saber quais os vetores de entrada que são significativos e qual a saída relativa a cada um deles.

***
<a name="ula"></a>

## 2) Circuitos aritméticos em VHDL.

### Contextualização

Para realizar operações aritméticas, como a soma e subtração, utiliza-se o somador completo de **1 bit**, mostrado abaixo:

| ![Somador Completo](imagensComponentes/somadorCompleto.png) | | | ![Diagrama Somador Completo](imagensComponentes/FullAdderWikimedia-A.svg) |
|:-----------:|:-----------:|:-----------:|:-----------:|
| **Tabela da Verdade** | | | **Diagrama** |

A conexão de vários desses somadores nos permite criar a parte aritmética da Unidade Lógica e Aritmética (ULA).

A ULA é composta de:

-   Duas entradas para os operandos em uso;

-   Uma unidade funcional para cada operação executada;

-   Um seletor entre os resultados das operações executadas.

O símbolo da ULA está mostrado abaixo, onde:

-   N: é a largura do vetor de bits para as entradas (A e B) e saída (Y).

-   m: é o seletor de função e depende da quantidade funções implementadas (#func):

    -   Sendo que a quantidade #func deve ser menor ou igual a 2^m.

-   Z: é o *flag* indicador de resultado igual a ZERO.

<br>

| ![](imagensComponentes/aluAula2.png) |
|:-------------------------:|
| Símbolo de uma ULA com N bits |

### Objetivo

Criar um segundo componente, utilizando um arquivo próprio, e implementar uma ULA com as seguintes características:

-   Dados com largura de 4 bits;

-   Utilizando 4  somadores completos interligados;

-   Execute a soma (A + B)   (tipo *unsigned*);

-   *Flag* detector de resultado igual a zero.

Se sobrar tempo, adicione estas funções:

-   Subtração (A - B) (tipo *unsigned*);

-   Rodar 1 bit para a esquerda (dica: pesquise sobre *barrel-shifter*).

-   Comparação entre as duas entradas, indicando somente quando forem iguais:

    -   Adicione um *flag* para indicar valores iguais.

<br>

Crie um novo projeto, como [descrito acima](#criaprojeto), e inicie a sua codificação.

[Compile o seu projeto][compilacao] e verifique a implementação através do [RTL Viewer][visualizacaoRTL]. Para testar, use a [simulação][simulacaoVWF]. Não esqueça de definir vetores de teste significativos e as saídas correspondentes.

<br>

***
<br><br>

## Referências

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

***

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<br>

***

***

<!-- FIM -->

<!---
######### (inicio dos links) ##########
--->

[linksUteis]: ./linksUteis.html

[compilacao]: ./quartus/_compilarProjetoQuartus.html

[simulacaoVWF]: ./quartus/_simulacao.html

[bibliotecaTemplates]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[visualizacaoRTL]: ./quartus/_rtlViewerQuartus.html

[vhdlBasico]:  ./vhdl/_vhdlBasico.html

[novoProjeto]: ./quartus/_criarProjetoQuartus.html

[recursosQuartus]: ./quartus/_recursosQuartus.html

[adicionarArqProjeto]: ./quartus/_recursosQuartus.html#adicionar-um-arquivo-ao-projeto

[clausulaBiblioteca]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[clausulaUse]: ./quartus/_recursosQuartus.html#escolher-os-templates-de-interesse

[entidade]: ./quartus/_recursosQuartus.html#escolher-os-templates-de-interesse

[arquitetura]: ./quartus/_recursosQuartus.html#escolher-os-templates-de-interesse

[topLevelEntity]: ./quartus/_recursosQuartus.html#configurar-a-top-level-entity


<!--
[IntelHierarchicalDesign]: https://www.altera.com/support/support-resources/design-examples/design-software/vhdl/v_hier.html
-->
<!---
fim
--->
