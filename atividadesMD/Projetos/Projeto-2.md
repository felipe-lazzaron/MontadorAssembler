<a name="inicio"></a>

# Projeto 2: Processador compatível com MIPS DLX

Ir para o [fim do documento](#fimDocumento) e referências.

## Descrição

Este projeto será a implementação de um processador RISC de 32 bits.
Ele deverá executar um dos dois subconjuntos, mostrados abaixo, das instruções do MIPS DLX<!--[MIPS DLX][ArquiteturaDLX]-->.

O **subconjunto "A"** é formado pelas instruções abaixo:

-   As instruções de referência à memória:

    -   Carrega palavra (_load word: lw_);

    -   Armazena palavra (_store word: sw_).

-   As instruções lógico-aritméticas:

    -   Soma (_add_);

    -   Subtração (_sub_);

    -   E lógico (_AND_);

    -   OU lógico (_OR_);

    -   Comparação menor que (_set if less than: slt_).

-   As instruções de desvio:

    -   Desvio se igual (_branch equal: beq_);

    -   Salto incondicional (_jump: j_).

O **subconjunto "B"** possui as instruções do subconjunto "A" e adiciona as listadas abaixo:

-   A instrução de carga:

    -   Carrega imediato para 16 bits MSB (_load upper immediate: lui_).

-   As instruções lógico-aritméticas:

    -   Soma com imediato (_addi_);

    -   E lógico com imediato (_ANDI_);

    -   OU lógico com imediato (_ORI_);

    -   Comparação menor que imediato (_set if less than: slti_).

-   As instruções de desvio:

    -   Desvio se não igual (_branch not equal: bne_);

    -   Salto e conecta (_jump and link: jal_);

    -   Salto por registrador (_jump register: jr_).

Tal qual a implementação do livro texto, não trabalharemos com nenhuma das instruções de ponto flutuante. Também não implementaremos todas as instruções que trabalham com inteiros, por exemplo: deslocamento, multiplicação e divisão.

As instruções restantes, para completar o conjunto todo do MIPS DLX, poderão ser implementadas com as mesmas técnicas usadas para implementar estes subconjuntos.

---

### Opções de Projeto

O projeto deverá implementar as seguintes funcionalidades:

-   MIPS com _pipeline_:

    -   Executando as instruções do subconjunto A;

    -   Nota máxima: limitada ao C+.

    -   Caso sejam adicionadas as instruções abaixo, o limite da nota será B.

        -   Salto e conecta (_jump and link: jal_);

        -   Salto por registrador (_jump register: jr_).

-   MIPS com _pipeline_:

    -   Executando todas instruções do subconjunto B;

    -   Nota máxima: limitada ao B+.

-   MIPS com _pipeline_:

    -   Executando as instruções do subconjunto B;

    -   Com o hardware para evitar _hazards_;

    -   Nota máxima: sem limite (A+).

---

### Entrega

A data de entrega, conforme o plano de aula, será:

-   Dentro do prazo e com limite de nota definido nas opções de projeto: **29/05/2019**.

-   Não haverá entrega em atraso.

<!---
-   Com atraso. O limite de nota é rebaixado em uma letra (em relação às opções de projeto): 22/11/2018.
--->

### Avaliação

A avaliação do projeto segue o descrito no plano de aula. Ela será feita através dos seguintes itens:

-   Apresentação do projeto, no kit de desenvolvimento:

    -   Com arguição do(s) professor(es).

-   Entrega de um resumo explicativo do funcionamento do circuito, contendo:

    -   Diagrama de blocos do projeto;

    -   Diagrama de estados (se for o caso);

    -   Com comentários (opcional) sobre os problemas encontrados.

-   Entrega do projeto do Quartus, com:

    -   Código VHDL, devidamente documentado e com o nome dos participantes;

    -   Arquivo com conteúdo da microprogramação (se for o caso).

### Execução

Em grupo, com até **4** (quatro) alunos.

---

## Leituras

Ler os itens abaixo, do livro texto (Organização e Projeto de Computadores: A Interface Hardware/Software):

-   Capítulo 4, item 4.1 até 4.9;

-   Apêndice C e D, completos;

-   [Arquitetura do MIPS na wikipedia (nosso interesse: MIPS I).](https://en.wikipedia.org/wiki/MIPS_architecture)

-   [A página do DLX na wikipedia.](https://en.wikipedia.org/wiki/DLX)

-   Um resumo de [referência sobre o MIPS](https://booksite.elsevier.com/9780124077263/downloads/COD_5e_Greencard.pdf) (todas instruções e outros detalhes - download gratuito no site da editora).

-   Resumo (interno) da [arquitetura do MIPS][ArquiteturaDLX]

<br>

## Referências

[Página com links][links] de referências sobre VHDL, Quartus, etc ...

<br>

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

***

<br>

***

***

<!-- FIM -->

<!---
######### (inicio dos links) ##########
--->

[links]: ../linksUteis.html

[ArquiteturaDLX]: ../MIPS/_arquitetura.html

<!--

[metodologia]: ../MIPS/metodo.html

[detalhesMulticore]: ../MIPS/multicore.html
-->
