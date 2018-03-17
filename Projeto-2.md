<a name="inicio"></a>

## Projeto 2: Processador compatível com MIPS DLX.

Ir para o [fim do documento](#fimDocumento) e referências.

## Descrição:

Este projeto será a implementação de um processador RISC de 32 bits.
Ele deverá executar um subconjunto das instruções do MIPS DLX<!--[MIPS DLX][ArquiteturaDLX]-->.

Esse subconjunto é formado pelas instruções abaixo:

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

Tal qual a implementação do livro texto, não trabalharemos com nenhuma das instruções de ponto flutuante. Também não implementaremos todas as instruções que trabalham com inteiros, por exemplo: deslocamento, multiplicação e divisão.

As instruções restantes, para completar o conjunto todo do MIPS DLX, poderão ser implementadas com as mesmas técnicas usadas para implementar este subconjunto.

---

### Opções de Projeto:

O projeto poderá seguir duas trilhas.

A primeira trilha será a implementação das seguintes funcionalidades:

-   MIPS Mono Ciclo, com as 9 instruções listadas acima. A nota máxima é limitada ao C;

-   MIPS Múlti Ciclo, com as 9 instruções listadas acima. A nota máxima é limitada ao B;

-   MIPS com as 9 instruções listadas acima, com _pipeline_ e hardware para evitar _hazards_.


A segunda trilha será a implementação das seguintes funcionalidades:

-   MIPS Mono Ciclo com as 9 instruções listadas acima. A nota máxima é limitada ao C;

-   MIPS Mono Ciclo e Múlti Núcleos <!--([ver detalhes][detalhesMulticore])-->. A nota máxima é limitada ao B;

-   MIPS Mono Ciclo com interrupção ou SIMD 128 bits.

---

### Entrega:

A data de entrega, que está no plano de aula, é: 28/11/2017.

#### Avaliação:

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

#### Execução:

Em grupo, com até 3 alunos.

---

### Leituras:

Para a trilha 1, ler os itens abaixo do livro texto (Organização e Projeto de Computadores: A Interface Hardware/Software):

-   Capítulo 4, item 4.1 até 4.9;

-   Apêndice C e D, completos;.

Para a trilha 2:

-   Capítulo 4, item 4.1 até 4.4;

-   Apêndice C e D, completos.

Comum a ambas trilhas:

-   [Arquitetura do MIPS na wikipedia (nosso interesse: MIPS I).](https://en.wikipedia.org/wiki/MIPS_architecture)

-   [A página do DLX na wikipedia.](https://en.wikipedia.org/wiki/DLX)

-   Um resumo de [referência sobre o MIPS](https://booksite.elsevier.com/9780124077263/downloads/COD_5e_Greencard.pdf) (todas instruções e outros detalhes - download gratuito no site da editora).

-   Resumo (interno) da [arquitetura do MIPS][ArquiteturaDLX]

<!--
-   [Metodologia][metodologia].

-   [Arquitetura do MIPS DLX][ArquiteturaDLX].
***

### Ferramentas:
-->

<br>

**Referências:**

[Página com links][links] de referências sobre VHDL, Quartus, etc ...

---

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!---
######### (inicio dos links) ##########
--->

[links]: ./linksUteis.html

[ArquiteturaDLX]: ./MIPS/_arquitetura.html

<!--

[metodologia]: ./MIPS/metodo.html

[detalhesMulticore]: ./MIPS/multicore.html
-->
