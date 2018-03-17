<a name="inicio"></a>

# Atividades

Ir para o [fim do documento](#fimDocumento) e referências.

---

## 1) Projetar a Unidade de Controle do Fluxo de Dados do MIPS DLX

### Contextualização

Uma vez implementada e testada a Unidade de Controle da ULA, vamos implementar:

-   Unidade de Controle do Fluxo de Dados.

![Decodificação em duas etapas](./imagensMIPS/decoder2unidadesVisaoGeral.svg)

Da mesma forma que na implementação da UC da ULA, teremos que levantar todas entradas e saídas necessárias para esse controlador.

Ele deve atuar em todos os pontos de controle do fluxo de dados, inclusive o ULAop.

![Fluxo de Dados do MIPS DLX](./imagensMIPS/fluxoDadosCompleto-1ciclo-Finalpq.png)

<br>

---

### Objetivo

Definir o circuito da Unidade de Controle do FD para que:

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

Inicialmente, para entender o problema, devemos levantar a quantidade de pontos de controle do FD.

Em seguida, devemos analisar os efeitos da ativação e desativação de cada ponto de controle do FD. E, resumir em uma tabela.

O próximo passo é relacionar esses efeitos com o funcionamento de cada instrução (ou tipo de instrução) a ser executada.

Finalmente, chegamos à etapa mais emocionante: a construção da tabela relacionando as entradas e saídas desejadas.

De posse dessa tabela preenchida, podemos visualizar as possíveis otimizações, ou mesmo utilizar Karnaugh.

#### Palavra de Controle do Fluxo de Dados (FDctrl)

Inicialmente, precisamos definir o conteúdo da palavra de controle. O desenho do FD, em alta resolução, está na figura abaixo:

[Fluxo de Dados MIPS DLX][fdMIPS] em alta resolução.

Para manter um padrão, utilizaremos os nomes já descritos no desenho. Liste, da esquerda (MSB) para a direita (LSB), todos os pontos de controle e os seus nomes. Esses serão os nossos sinais de saída.

#### Sinais de Entrada

Os sinais de entrada são os bits que definem a instrução a ser executada. Eles são:

-   Campo de _opcode_ (bit 31 até bit 26) da instrução.

#### Tabelas

Para preencher as [tabelas][tabelasFD], com o mapeamento das entradas e saídas, utilizaremos:

-   O _green card_;

-   Cópias do desenho do FD, em alta resolução, para simular o funcionamento de cada instrução:

    -   Utilize um programa de edição de imagens, em _bit map_, para colorir o caminho de cada instrução e seus pontos ativos.

Caso não consiga fazer a simulação diretamente:

-   Descreva o funcionamento da instrução em pseudocódigo ou em RTN;

-   Em seguida, utilizando esse código, avalie como seria o fluxo dos sinais através do FD e quais pontos teriam que ser ativados.

Com a tabela preenchida, para todas as instruções, deve ser feita a otimização. Ela pode ser feita manualmente ou utilizando programas.

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

[fdMIPS]: ./imagensMIPS/fluxoDadosCompleto-1ciclo-Final.png

[tabelasFD]: ./MIPS/_tabelasFD.html

[linksUteis]: ./linksUteis.html
