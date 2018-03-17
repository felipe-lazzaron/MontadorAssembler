<a name="inicio"></a>

# VHDL Básico #

>**Baseado no livro Free Range VHDL, de 2013, escrito por Bryan Mealy e Fabrizio Tappero.**
>
>**E nos slides do curso de VHDL da Altera.**

[Ir para o fim do documento](#fimDocumento).

**Conteúdo:**

-   [Regras de Ouro do VHDL](#regras-de-ouro-do-vhdl);
-   [Invariantes do VHDL](#invariantes-do-vhdl);
-   [Unidades de projeto](#unidades-de-projeto);
-   [Entidades](#entidades);
-   [Arquiteturas](#arquiteturas);
-   [Classes de Objetos](#classes-de-objetos);
-   [Tipos de dados](#tipos-de-dados);
-   [Estilos usados nas Arquiteturas](#estilos-usados-nas-arquiteturas);
    -   [Estilo Comportamental](#comportamental);
    -   [Estilo Fluxo de Dados](#fluxo-de-dados);
    -   [Estilo Estrutural](#estrutural).
-   [Instanciação de Componentes](#instanciação-de-componentes);
-   [Lista de palavras reservadas](#palavras-reservadas).

***

## Regras de Ouro do VHDL: ##

*   VHDL é uma descrição, ou projeto, do hardware e não uma programação dele.
    *   As linhas de código não são executadas sequencialmente com exeção de algumas construções da linguagem.
    *   As linhas de código serão executadas simultaneamente.
*   Deve-se possuir uma visão de como o circuito final será.
    *   Se ele for muito complexo, use uma divisão em blocos menores até chegar às unidades construtivas básicas.

***

## Invariantes do VHDL: ##

-   Não distingue maiúscas de minúsculas (case insensitive).
-   Não é sensível as espaços e tabulações.
-   Comentários iniciam com dois sinais de menos: `--`.
-   O uso de parenteses nas operações é uma boa prática. Apesar de existir precedência entre as operações, o uso de parenteses aumenta a legibilidade.
-   Os comandos VHDL terminam com ponto e vírgula: `;`.
-   O comando _if_ necessita que:
    -   Cada _if_ tenha os seus comandos correspondentes: _then_  e _end if;_.
    -   No caso do _else if_, no VHDL, ele é chamado de: _elsif_.
-   Os comandos _case_ e _loop_ possuem um comando de término:
    -   O _end case_ e o _end loop_.
-   Os identificadores são os nomes dados às variáveis, sinais, portas, entre outros.
    -   Eles não possuem limite de comprimento.
    -   Esses nomes só podem utilizar uma combinação dos seguintes conjuntos de caracteres:
        -   Letras (A-Z e a-z);
        -   Números (0-9);
        -   O caractere de sublinhado: "\_".
    -   Os identificadores precisam iniciar com uma letra.
    -   Eles não podem terminar com o caractere de sublinhado.
    -   E não podem usar dois caracteres de sublinhado consecutivos.

-   Existe um conjunto de [palavras reservadas](#tabelaPalavrasReservadas) que não podem ser utilizadas como identificadores.

***

## Unidades de projeto: ##

O VHDL utiliza uma abstração do tipo "caixa-preta" com uma estrutura hierárquica que permite:

-   Agrupar unidades funcionais básicas para criar um circuito mais complexo e:
    -   Disponibilizar seu uso através de uma interface desse módulo;
    -   Que esconde os detalhes do circuito que executa a funcionalidade desejada (a caixa-preta).
-   A cada nível hierárquico agrupam-se:
    -   Mais módulos e cria-se um circuito cada vez mais complexo;
    -   Que será disponibilizado, para o nível superior, através de uma nova interface de uso (ou seja, um novo módulo, mais complexo, composto de módulos mais simples).
-   Variar a quantidade de detalhes disponíveis a cada nível hierárquico.

Essa abordagem permite:

-   Reutilizar o código criado anteriormente pelos projetistas;
-   Facilitar a compreenção do circuito através da análise da interligação dos módulos (nomeados adequadamente). O que é mais simples do que analisar o circuito com uma grande quantidade de portas lógicas interligadas.  

**Principais elementos de projeto:**

Os principais elementos de projeto da linguagem VHDL são:

-   [Entidades](#entidades) (`entity`):
    -   descreve os pinos de acesso à "caixa-preta". Ou seja, a interface de uso do circuito.
-   [Arquiteturas](#arquiteturas) (`architecture`):
    -   descreve o funcionamento interno do circuito.
-   [Configurações]() (`configuration`):
    -   associa uma entidade com uma arquitetura, formando um circuito.
-   [Pacotes]() (`package` e `package bodies`):
    -   é uma forma de armazenar modelos, definições, etc...

O VHDL possui dois pacotes embutidos (não precisam ser declarados):

-   Standard;
-   TEXTIO.

<img src="../imagensVHDL/entidadeArquiteturaPCFS_2D.png" align="center" width="400">

***

#### Bibliotecas: ####

As definições básicas da linguagem (como os tipos, as funções de conversão entre os tipos, constantes matemáticas, funções aritméticas, entre outros recursos), estão contidas nas bibliotecas.

Uma biblioteca pode conter um ou mais pacotes. O VHDL possui duas bibliotecas implícitas (não precisam ser declaradas):

-   Work: se refere aos módulos do projeto atual;
-   STD: contem os pacotes:
    -   standard, que define os tipos: bit, boolean integer, real e time.
    -   textio: que define as operações com arquivos.

Para adicionar uma biblioteca precisamos de dois comandos:

*   O `library`, que declara a biblioteca para ser utilizada:
    *   É um nome simbólico para o caminho (`path`) da biblioteca.
*   O `use`, que especifica o pacote e objetos que existem na biblioteca definida com `library`.

A biblioteca mais comum é a `IEEE`. E seus pacotes comumente usados são:

*   `ieee.std_logic_1164.all`
*   `ieee.numeric_std.all`

O exemplo abaixo mostra a utilização dos comandos `library` e `use`.

Os nomes entre os sinais `<` e `>`, incluindo os sinais, devem ser personalizados para a biblioteca e pacotes necessários à aplicação em desenvolvimento.

```vhdl
-- A library clause declares a name as a library.  It
-- does not create the library; it simply forward declares it.
library <library_name>;

-- Use clauses import declarations into the current scope.
-- If more than one use clause imports the same name into the
-- the same scope, none of the names are imported.

-- Import all the declarations in a package
use <library_name>.<package_name>.all;

-- Import a specific declaration from a package
use <library_name>.<package_name>.<object_name>;

-- Import a specific entity from a library
use <library_name>.<entity_name>;

-- Import from the work library.  The work library is an alias
-- for the library containing the current design unit.
use work.<package_name>.all;

-- Commonly imported packages:
  -- STD_LOGIC and STD_LOGIC_VECTOR types, and relevant functions
  use ieee.std_logic_1164.all;

  -- SIGNED and UNSIGNED types, and relevant functions
  use ieee.numeric_std.all;
```

#### Entidades: ####

Todo projeto deve possuir, no mínimo, uma entidade. Toda entidade deve possuir um nome. A entidade descreve a visão externa (interface) do circuito que a utiliza.

As entidades podem ser correlacionadas com o encapsulamento de um chip, onde temos os pinos de entrada, saída e eventualmente bidirecionais.

A construção mínima da entidade deve possuir uma seção declarativa, chamada de `port();`. Nela são definidos os nomes dos pinos, sua direção (modo), o tipo de dados relacionado a ele e, opcionalmente, um valor de inicialização. São os sinais que os circuitos externos a essa entidade utilizam para interagir com ela.

Além da seção `port();` pode existir uma seção chamada de `generic();`, onde são definidos parâmetros configuráveis em tempo de compilação.

Essa seção simula a passagem de argumentos que serão utilizados na compilação. Pode-se definir, por exemplo, o número de _bits_ utilizados como entrada ou saída daquele módulo.

Em tempo de execução a parametrização não pode ser alterada, já que os circuitos foram criados durante a compilação. Lembre que estamos criando circuitos e não executando uma rotina de programa.

Os [tipos de dados](#tiposDados) que existem na linguagem VHDL estão definidos em uma seção mais à frente.

<br>

**Estrutura básica:**

O modelo geral de uma entidade está mostrado abaixo (retirada do Quartus Prime Lite). Note que alguns trechos são opcionais, como o `generic` e os valores de inicialização.

```vhdl
entity <entity_name> is
  generic                      
  (
    -- O generic é opcional.
  <name>	: <type>  :=	<default_value>;
  <name>	: <type>  :=	<default_value>
  );
  port    -- O port é obrigatório e possui o objeto “signal” implícito.
  (
  -- Input ports
    -- "in" indica que é uma porta no modo de entrada.
    -- O valor de inicialização é opcional.
  <name>	: in  <type>;  
  <name>	: in  <type> := <default_value>;  

  -- Inout ports
    -- "inout" indica que é uma porta no modo bidirecional.
    -- Não existe valor de inicialização.
  <name>	: inout <type>;

  -- Output ports
    -- "out" indica que é uma porta no modo de saída.
    -- O valor de inicialização é opcional.
  <name>	: out <type>;
  <name>	: out <type> := <default_value>

  -- Buffer ports
  -- Similar a Out, mas permite realimentação interna.
  <name>  : buffer  <type>;
  );
end <entity_name>;   -- Também pode ser utilizado: "end entity";
```
<br><br>

**Exemplos:**

Abaixo temos um exemplo do modelo, disponível no Quartus Prime Lite, de um somador configurável através de `generic`:

```vhdl
-- Quartus Prime VHDL Template
-- Signed Adder

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity signed_adder is
  generic
  (
      	DATA_WIDTH : natural := 8
  );
  port
  (
    		a	   : in signed	((DATA_WIDTH-1) downto 0);
    		b	   : in signed	((DATA_WIDTH-1) downto 0);
    		result : out signed ((DATA_WIDTH-1) downto 0)
  );

end entity;

architecture rtl of signed_adder is
begin
         result <= a + b;
end rtl;
```
Na instaciação do componente existe a opção de alterar o valor do `generic`. Se o valor não for alterado, será criado um somador de 8 bits (como foi definido na entidade). Para saber como instanciar um módulo e alterar o `generic`, veja a [seção sobre instanciação](#instanciar).

Abaixo, temos outro exemplo de entidade usando o `generic`. Note que é possível fazer aritmética com o valor do `generic` para definir a largura de dados dos `ports`.

```vhdl
-- Quartus Prime VHDL Template
-- Unsigned Multiply

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity unsigned_multiply is
  generic
  (
        DATA_WIDTH : natural := 8
  );
  port
  (
      		a	   : in unsigned ((DATA_WIDTH-1) downto 0);
      		b	   : in unsigned ((DATA_WIDTH-1) downto 0);
      		result  : out unsigned ((2*DATA_WIDTH-1) downto 0)
  );

end entity;

architecture rtl of unsigned_multiply is
begin
         result <= a * b;
end rtl;
```
<br>

***
#### Arquiteturas: ####

Toda entidade deve possuir, ao menos, uma arquitetura. Ela deve descrever o funcionamento interno do circuito associado à entidade. Para uma mesma entidade, pode-se ter arquiteturas diferentes, que descrevem circuitos de forma diferente ou com funcionalidade diferente.

Uma mesma arquitetura pode ser modelada com estilos diferentes. Esses estilos são:

*   [Data\-Flow (fluxo de dados):](#fluxo-de-dados)
    *   Um conjunto de comandos concorrentes que representam o fluxo dos dados pelo circuito.
*   [Behavioral (comportamental):](#comportamental)
    *   Um conjunto de comandos concorrentes que representam o comportamento da entidade;
    *   Um conjunto de comandos sequenciais que representam o comportamento da entidade.
*   [Structural (estrutural):](#estrutural)
    *   Um conjunto de componentes interconectados que representam a estrutura da entidade.
*   Híbrido:
    *   Uma mistura dos modelos acima.

Abaixo temos um modelo geral de uma arquitetura (retirada do Quartus Prime Lite). Note que existem vários comandos opcionais.

```vhdl
-- Library Clause(s) (optional)
-- Use Clause(s) (optional)

architecture <arch_name> of <entity_name> is

  -- Área reservada para declarações.
  -- Declarations (optional)

begin

  -- Descrição do funcionamento do circuito.
  -- Pode utilizar os seguintes comandos:

  -- Process Statement (optional)   -- podem existir vários

  -- Concurrent Procedure Call (optional)

  -- Concurrent Signal Assignment (optional)

  -- Conditional Signal Assignment (optional)

  -- Selected Signal Assignment (optional)

  -- Component Instantiation Statement (optional)

  -- Generate Statement (optional)

end architecture;
```

Entre a definição da arquitetura e o `begin`, temos a área reservada para declarações (caso existam). Em seguida, entre o `begin` e o `end`, temos a área reservada para a descrição do funcionamento do circuito. Os detalhes sobre os grupos de declarações, que podem ser utilizados na descrição do funcionamento, está disponível nos links abaixo:

-   [Process Statement](#processo);

-   [Concurrent Procedure Call]();

-   [Concurrent Signal Assignment]();

-   [Conditional Signal Assignment]();

-   [Selected Signal Assignment]();

-   [Component Instantiation]();

-   [Generate Statement]().

<br>

**Exemplos:**

Abaixo temos uma entidade com 2 pinos de entrada e um de saída. Note que essa entidade pode ser utilizada com diferentes funções: AND, OR e XOR. A arquitetura a ser utilizada pode ser configurada com o comando `configuration` ou no momento da instaciação.

```vhdl
-- Quartus Prime VHDL Template
-- Configurable gate architecture

library ieee;
use ieee.std_logic_1164.all;
entity configurable_gate is
  port
  (
        i1 : in std_logic;
        i2 : in std_logic;
        o1 : out std_logic
  );
end configurable_gate;

-- Three possible architectures
architecture and_gate of configurable_gate is
begin
        o1 <= i1 AND i2;
end and_gate;

architecture or_gate of configurable_gate is
begin
        o1 <= i1 OR i2;
end or_gate;

architecture xor_gate of configurable_gate is
begin
        o1 <= i1 XOR i2;
end xor_gate;
```

***
#### Classes de Objetos ####

Em VHDL, os objetos são uma representação abstrata de dados armazenados. Existem quatro classes de objetos:

*   A classe `variable` é usada para armazenar informações locais:
    *   Seu valor é alterado no momento da atribuição. É utilizada em trechos de código que possuem execução sequencial.
*   A classe `constant` é similar a uma `variable` mas seu valor é imutável após a atribuição inicial.
*   A classe `signal` é usada para descrever conexões entre os elementos do projeto (como um fio):
    *   Pode ser usada em trechos de código sequencial ou concorrente. Seu valor pode ser alterado mas a mudança ocorre "algum tempo" depois da avalição da expressão de atribuição.
*   A classe `file` é usada para armazenar dados de forma persistente:
    *   A principal aplicação é na simulação, onde pode salvar resultados ou carregar vetores de teste.

Ao criar os objetos dessas classes, deve-se associar cada objeto a um tipo de dados. A sintaxe geral é vista abaixo:

<img src="../imagensVHDL/classeObjetoTipo-1.png" align="center" width="400">

<br>

Existe uma excessão a essa sintaxe. Ela ocorre dentro da entidade, onde a definição do `port` não define o seu objeto. Nesse caso, o objeto `signal` está implícito.

É obrigatório declarar um objeto do tipo `signal` ou `variable` antes de usá-los:

-   Os sinais são declarados no topo do corpo da arquitetura, logo antes do `begin`;
-   As variáveis devem ser declaradas dentro do `process`.

Sinais declarados na arquitetura são chamados de sinais intermediários e não possuem declaração de modo (`in`, `out` ou `inout`).

A atribuição de um novo valor a um objeto `signal` deve ser feita com o operador de atribuição, que possui um `process` implicito:

*   <=

Para um objeto do tipo `variable`, deve-se utilizar outro operador de atribuição:

*   :=  

As atribuições podem ser por agregados:

# Preencher<== #

A diferença entre `variables` e `signals` está no momento da mudança de seu valor. Uma variável muda seu valor logo após a atribuição ser executada. Ao contrário, um sinal só muda o seu valor "algum tempo" depois que a expressão de atribuição de sinal é avaliada (existe uma temporização implícita).

A variável é geralmente utilizada para descrever o comportamento e os sinais para representar as ligações (fios).

Caso as atribuições sejam feitas dentro de uma construção `process`, elas serão agendadas para o término desse mesmo `process`. A atribuição real não é feita antes do término do processo.

~~Isso tem conseqüências importantes para os valores atualizados de variáveis ​​e sinais. Isso significa que você nunca deve assumir que uma atribuição de sinal pode acontecer instantaneamente e também significa que você pode aproveitar variáveis ​​sempre que você precisa implementar um contador ou armazenar valores durante a execução de um processo.~~

Além disso, o uso de uma variável deve ser sempre dentro da construção `process`.

#### Escopo dos Objetos ####

A visibilidade desses objetos está relacionada ao lugar onde eles foram declarados:

*   Declarações feitas dentro de um pacote:
    *   São acessíveis a todas as entidades que usam aquele pacote.
*   Declarações feitas dentro de uma entidade:
    *   São acessíveis a todas as arquiteturas que usam aquela entidade.
*   Declarações feitas dentro de uma arquitetura:
    *   São acessíveis a todas as sentenças dentro daquela arquitetura.
*   Declarações feitas dentro de um processo:
    *   São acessíveis somente dentro daquele processo.

<!--
```
<Classe do objeto> <nome/identificador do objeto>: <tipo de dado> [:=valor inicial];
```
-->

<a name="tiposDados"></a>

### Tipos de Dados: ###

O VHDL é uma linguagem fortemente tipada e nela existem três categorias de tipos de dados:

1.  Tipos escalares (`scalar`): seus valores possuem uma ordem sequencial.

2.  Tipos compostos: podem ser compostos de elementos:
    -   de um único tipo, caracterizando um arranjo (`array type`);
    -   de tipos diferentes, caracterizando um registro (`record type`).

3.  Tipos de acesso: permitem o  acesso a objetos de um dado tipo através de ponteiros (`pointers`).

Cada tipo de dados define:

*   Um conjunto de valores que esses objetos podem assumir;
*   E um conjunto de operações que podem ser executadas com os objetos desse tipo.

Ou seja, um objeto de certo tipo não pode receber valores de outro tipo de objeto:

*   Deve ser feita a [conversão de tipos](#convTipos).

![](../imagensVHDL/tiposDadosVHDLptbr-svg.png)

Além dos tipos de dados predefinidos, o programador pode criar novos tipos e subtipos de dados. Em geral, esses novos tipos estão disponíveis em pacotes ou bibliotecas VHDL.

# PAREI AQUI #

O pacote `standard` da biblioteca `std`, que é incluído por padrão, possui os seguintes tipos predefinidos:

-   `bit`: é um tipo com dois valores ('0' ou '1').
-   `bit_vector`: um `array` de `bit`. No seu lugar, é mais usado o `std_logic_vector`.
-   `boolean`: um tipo enumerado com dois valores (`true` ou `false`).
-   ~~`boolean_vector`: é um vetor composto somente com tipos `boolean`.~~
-   `integer`: valores decimais inteiros, tanto positivos quanto negativos.
-   `natural`: é um subtipo de `integer` onde não existem os números negativos.
-   `positive`: é um subtipo de `integer` onde não existe o zero e os números negativos.
-   `integer_vector`: é um vetor composto somente com tipos `integer`.
-   `character`: é um tipo enumerado com 256 símbolos.
-   `string`: é um vetor composto somente com tipos `character`.
-   `real`: valores decimais fracionários.
-   `time`:

A biblioteca do IEEE possui o pacote O tipo `std_logic_1164`, que define os tipos:

-   `std_logic`: tipo resolvido que possui 9 valores. Suporta múltiplos sinais acionando um único sinal;
-   `std_logic_vector`: é um vetor composto somente com tipos `std_logic`.
-   `std_ulogic`: possui os mesmos 9 valores, porém não é resolvido. Não suporta múltiplos sinais acionando um único sinal, ocorrerá um erro.
-   `std_ulogic_vector`: é um vetor composto somente com tipos `std_ulogic`.

O uso do tipo `std_logic` suplantou o tipo `bit`.

```vhdl
    type my_count is range 0 to 100;     -- user-defined type
    constant max_count : my_count := 31; -- user-defined constant
    signal tmp_sclk : std_logic;         -- intermediate signal
```

#### Tipo de Dados: Enumerado ####

É formado por uma faixa de valores definida pelo usuário.
TYPE <nome_tipo_dados>  IS
        (itens ou valores permitidos para o seu tipo de dados, separados por virgula)

```vhdl
type estado is (ST0,ST1,ST2,ST3);
```
O tipo `std_logic` é um tipo enumerado, como mostra a sua definição:

```vhdl
type std_logic is ( 'U',  -- uninitialised
                    'X',  -- forcing unknown
                    '0',  -- forcing 0
                    '1',  -- forcing 1
                    'Z',  -- high impedance
                    'W',  -- weak unknown
                    'L',  -- weak 0
                    'H',  -- weak 1
                    '-'   -- unspecified (do not care)
);
```

Isso permite que ele cubra situações, durante as simulações, onde dois sinais, um com nível lógico alto e outro com nível baixo, excitem uma entrada. O resultado é obtido através de uma tabela de resolução:

|U|   X | 0 | 1 | Z | W | L | H |'--'|   |       |
|---|---|---|---|---|---|---|---|---|----|-------|
|'U'|'U'|'U'|'U'|'U'|'U'|'U'|'U'|'U'|--| **U** |
|'U'|'X'|'X'|'X'|'X'|'X'|'X'|'X'|'X'|--| **X** |
|'U'|'X'|'0'|'X'|'0'|'0'|'0'|'0'|'X'|--| **0** |
|'U'|'X'|'X'|'1'|'1'|'1'|'1'|'1'|'X'|--| **1** |
|'U'|'X'|'0'|'1'|'Z'|'W'|'L'|'H'|'X'|--| **Z** |
|'U'|'X'|'0'|'1'|'W'|'W'|'W'|'W'|'X'|--| **W** |
|'U'|'X'|'0'|'1'|'L'|'W'|'L'|'W'|'X'|--| **L** |
|'U'|'X'|'0'|'1'|'H'|'W'|'W'|'H'|'X'|--| **H** |
|'U'|'X'|'X'|'X'|'X'|'X'|'X'|'X'|'X'|--|**'--'**|



#### Subtipos ####

Subtipos são tipos predefinidos:

-   Aos quais é aplicada uma restrição de faixa de valores;
-   Qualquer atribuição de valor, fora dessa faixa, gera um erro.

```vhdl
SUBTYPE <name> IS <base type> RANGE <user range>;

SUBTYPE first_ten IS integer RANGE 1 to 10;
SUBTYPE byte IS bit_vector(7 downto 0);  -- little endian
SUBTYPE byte IS bit_vector(0 to 7);  -- big endian
```

***

<a name="convTipos"></a>

#### Conversão de Tipos ####

Como o VHDL é uma linguagem fortemente tipada, para fazer operações com objetos de diferentes tipos, temos que fazer a conversão de tipos desses objetos. Ela pode ser feita através de `type cast` ou através de funções de conversão. A figura abaixo mostra as formas de fazer as conversões e os casos em que aplicamos cada uma.

![Conversão de tipos em VHDL](../imagensVHDL/vhdl-type-conversionsPCFS.svg)

O uso de um vetor, como o `std_logic_vector`, não define o significado de seus componentes. Ou seja, ele só define que existe um grupo de sinais juntos. Dessa forma, para fazer operações com esses vetores é necessário convertê-los em tipos com ou sem sinal (`signed`, `unsigned`, ou `integer`). Essa conversão permite que o grupo de bits seja entendido como números e seja possível fazer cálculos com os mesmos.

Um bom exemplo é a descrição de um contador, onde não se pode incrementar um sinal `std_logic_vector`. É preciso convertê-lo primeiro  em `signed`, `unsiged` ou `integer`, fazer o incremento e se for o caso, convertê-lo novamente para `std_logic_vector`. Isso pode ser visto no trecho de código abaixo:

```vhdl
    library IEEE;
    use IEEE.std_logic_1164.all;
    use ieee.numeric_std.all

    signal val1, val2 : std_logic_vector( 31 downto 0 );

    -- Incorreto:
    val2 <= val1 + 1;

    -- Correto:
    val2 <= std_logic_vector( unsigned(val1) + 1 );
```

Para fazer cálculos com tipos `signed` ou `unsigned` é necessário utilizar o pacote padronizado pelo IEEE: `numeric_std`. Por questões de compatibilidade, é preferível usar as bibliotecas e pacotes padronizados pelo IEEE.

A Synopsys possui bibliotecas que não são padronizadas, apesar da sua popularidade. O seu uso deve ser evitado. Elas são:

-   `std_logic_signed`;
-   `std_logic_unsigned`;
-   `std_logic_arith`.

#### Atributos ####

Atributos de sinais:

-   sinal‘delayed(<Tempo>) – Valor do sinal atrasado em <Tempo> unidades de tempo
-   sinal‘stable(<Tempo>) – True se nenhum evento ocorrer sobre o sinal nas últimas
<Tempo> unidades de tempo.
-   sinal‘quiet(<Tempo>) – True se o sinal sinal se mantiver constante por <Tempo>
unidades de tempo
-   sinal‘last_value – Valor do sinal sinal antes da última variação/mudança
-   sinal‘last_event – Instante no qual o sinal sinal sofreu alteração pela última vez
-   sinal‘last_active – Instante no qual o sinal esteve ativo na última vez
-   sinal‘event – True se um evento ocorreu no sinal sinal no ciclo corrente
-   sinal‘active – True se o sinal sinal está ativo no ciclo corrente
-   sinal‘transaction – Valor de bit alterado a cada vez que o sinal sinal sofre alterações

Atributos de escalares:

-   sinal’left – primeiro (mais a esquerda) valor em sinal
-   sinal’right – último (mais a direita) valor em sinal
-   sinal’low – menor valor em sinal
-   sinal’high – maior valor em sinal
-   sinal’ascending – True se sinal está em uma faixa ascendente, False caso contrário
-   sinal’image(x) – string representando o valor de x
-   sinal’value(s) – o valor em <Nome do Sinal> que é representado por s

Aplicados apenas a tipos discretos ou físicos:

-   sinal‘pos(x) – número da posição x em sinal;
-   sinal‘val(n) – valor contido na posição "n" do sinal.
-   sinal‘succ(x) – valor em sinal na posição um a mais que a de x
-   sinal‘pred(x) – valor em sinal na posição um a menos que a de x
-   sinal‘leftof(x) – valor em sinal na posição um a esquerda de x
-   sinal‘rightof(x) – valor em sinal na posição um a direita de x

Atributos de vetores:

-   sinal‘left(N) – Limite esquerdo da faixa de dimensão N do sinal sinal
-   sinal‘right(N) – Limite direito da faixa de dimensão N do sinal sinal
-   sinal‘low(N) – Limite inferior da faixa de dimensão N do sinal sinal
-   sinal‘high(N) – Limite superior da faixa de dimensão N do sinal sinal
-   sinal‘range(N) – Faixa do índice de dimensão N do sinal sinal
-   sinal‘reverse_range(N) – Reverso do índice de dimensão N do sinal sinal
-   sinal‘length(N) – Comprimento do índice de dimensão N do sinal sinal
-   sinal‘ascending(N) – True se faixa do indice de dimensão N de sinal está em uma faixa acendente, Falso caso contrário
-   sinal‘element(N) – Elemento subtipo de sinal

### Instanciação de Componentes ###

***
## Paradigma de Programação VHDL ##

### Declarações Concorrentes ###

### Operador de Atribuição para Sinais (`signal`) ###

### Declarações Concorrentes de Atribuição para Sinais (`signal`) ###

### Atribuição Condicional (`when`) para Sinais (`signal`) ###

### Atribuição Seletiva (`whith select`) para Sinais (`signal`) ###

<a name="processo"></a>

### Declaração de Processos (`process`) ###


Sempre que for necessário um ambiente de execução sequencial, onde as linhas de código são executadas uma após a outra (como em C ou Java), é necessário utilizar a construção `process`. Dentro de um processo, todas as instruções são executadas sequencialmente de cima para baixo. No entanto, o processo em si será executado simultaneamente com o resto do código.

No exemplo abaixo, a execução do `process` e a atribuição ao `port` G não são executadas sequencialmente. Eles são executados concorrentemente (tudo ao mesmo tempo).

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity circuitoExemplo is
    port (
        A,B,C : in   std_logic;
        F, G  : out  std_logic
    );
end entity;

architecture nome of circuitoExemplo is

    signal sig_1 : std_logic;

begin
    process (a,b,c)     -- Este process é executado em paralelo com a atribuição ao G.

          variable var_1 : integer;

    begin          -- Daqui até o "end process", a execução é sequencial.
          F <= not (A and B and C);     
          sig_1 <= A;
          var_1 := 34;
    end process;   -- Fim do trecho sequencial.

    G <= not (A and B);  -- Esta atribuição é executada em paralelo com o process.

end architecture;
```

<!---
Os três principais sabores dos estilos de modelagem VHDL incluem modelos de fluxo de dados, comportamentais e estruturais.
Modelos comportamentais VHDL, por definição, usam declarações do processo.

Os modelos de fluxo de dados VHDL, por definição, usam atribuição de sinal concorrente, atribuição de sinal condicional e / ou atribuição de sinal selecionada.

A declaração do processo é uma declaração simultânea. As declarações que aparecem dentro da declaração do processo são instruções sequenciais.

A instrução if tem uma analogia direta com a instrução de atribuição de sinal condicional usada no modelagem de fluxo de dados.

A declaração CASE tem uma analogia direta com a instrução de atribuição de sinal selecionada usada no modelagem de fluxo de dados.

Tanto a declaração do caso como a instrução if podem ser aninhadas. Declarações de atribuição de sinal concorrentes, condicionais e selecionadas não podem ser aninhadas.

A declaração concorrente mais simples é a declaração de atribuição de sinal concorrente (por exemplo, "F <= A;"). Seu equivalente sequencial é a declaração de atribuição de sinal seqüencial e possui a mesma sintaxe.
--->

***
## Estilos usados nas Arquiteturas: ##

### Comportamental: ###

O estilo comportamental não fornece detalhes sobre como o projeto é implementado no hardware. Ele define como as saídas do circuito reagem às entradas e suas variações. Assim, os detalhes da implementação do circuito são deixados aos cuidados da ferramenta de síntese.

A modelagem comportamental está em um nível de abstração acima da modelagem de fluxo de dados. Pode-se dizer que a modelagem comportamental, no projeto de circuitos, é a própria abordagem "caixa-preta".

A modelagem comportamental se baseia na declaração do processo (`process`), que é um tipo de declaração simultânea que executa o seu conteúdo de forma sequencial.

A principal diferença entre `process` e as outras três declarações concorrentes está na abordagem da concorrência que o processo usa.

##### Comando Process: #####


***

### Fluxo de Dados: ###

Esse estilo de arquitetura especifica um circuito como uma representação simultânea do fluxo de dados através do circuito.

Na abordagem de fluxo de dados, os circuitos são descritos mostrando as relações de entrada e saída entre os vários componentes internos do VHDL. Esses componentes incluem operadores como AND, OR, XOR, etc.

As três formas de declarações simultâneas que falamos até agora:

*   Atribuição concorrente de sinal;
*   Atribuição condicional de sinal;
*   Atribuição seletiva de sinal.

<!--
blocking assignments inside process
are evaluated in the order in which they appear in the code, just as one would expect in a standard programming language.

nonblocking assignments inside process
are evaluated concurrently; all of the statements are evaluated before any of
the signals on the left hand sides are updated.
-->

Essas três são todas as declarações que são encontradas em arquiteturas de estilo de fluxo de dados. Em outras palavras, se você usou exclusivamente instruções de atribuição de sinal concorrentes, condicionais e selecionadas em seus modelos VHDL, você usou um modelo de fluxo de dados.

Se você possui um conhecimento prático da lógica digital, é bastante fácil imaginar os circuitos subjacentes em termos de portas lógicas padrão. Essas instruções de atribuição de sinal descrevem efetivamente como os dados fluem dos sinais à direita
 do operador de atribuição (o "<=") para o sinal no lado esquerdo desse operador.

O estilo de arquitetura descrita através de fluxo de dados tem pontos fortes e pontos fracos:

-   É possível ver o fluxo de dados no circuito examinando o código VHDL.
-   Estimar como a lógica real será após a síntese do circuito.
-   Funciona bem para circuitos pequenos e relativamente simples.
-   Para circuitos mais complicados é vantajoso usar o estilo comportamental.

```vhdl
entity AND2 is
      port (
          X, Y : in   BIT;
          Z    : out  BIT
      );
end entity;

architecture FluxoDados of AND2 is
begin
      Z <= X AND Y;
end architecture;

```

### Estrutural: ###

Em VHDL, a modularidade é conseguida através do uso de pacotes (`packages`), componentes (`components`) e funções (`functions`). A seguir, veremos como usar os componentes.

A abordagem para usar um componente no VHDL é:

   1) Nomeie o módulo que você planeja descrever (a entidade);
   2) Descreva o que o módulo fará (a arquitetura);
   3) Deixe o programa saber que o módulo existe e pode ser usado (declaração do componente);
   4) Use o módulo em seu código (instanciação de componentes ou mapeamento).

Abaixo pode-se ver um exemplo de descrição estrutural. É a constução de uma porta NAND através da conexão de uma porta AND e outra NOT (definidas em outro arquivo do projeto).

```vhdl
entity NAND2 is
   port (
        A,B : in BIT;
        Z   : out BIT
  );
end NAND2;

architecture STRUCTURAL of NAND2 is

    -- Utilizado com um fio entre a saída da porta AND e a entrada do INVERSOR.
    signal I: Bit;     

    -- A entidade do componente está definida em outro arquivo do projeto.
    -- Aqui é declarada a sua utilização.

    component AND_2 is
        port(
            I1,I2: in Bit;
            O1: out BIT
        );
    end component;

    component INVERT is
        port(
            I1: in Bit;
            O1: out Bit
        );
    end component;

begin
    -- Instancia os componentes e faz as conexões (mapeamento):
    U0: AND_2 port map (I1,I2,I);         --faz a conexão através do posicionamento.
    U1: INVERT port map (I1=>I, O1=>Z);   --faz a conexão de forma explicita.
end STRUCTURAL;
```

<!---

Modelagem estrutural em VHDL suporta conceitos de design hierárquico. A capacidade de abstrair circuitos digitais para níveis mais altos é a chave para entender e projetar circuitos digitais complexos.

O design digital usando captura esquemática é uma abordagem desatualizada: você deve resistir à inclinação e / ou diretiva a todo custo.

O modelo estrutural VHDL suporta a reutilização de unidades de design. Isso inclui as unidades que você já criou, bem como a capacidade de usar bibliotecas de módulos predefinidos.

Se você usa uma ferramenta de desenvolvimento de software FPGA de um dos principais players de FPGA no mercado, você poderá usar blocos digitais já desenvolvidos uma vez que os declarar. Nesse caso, a declaração da entidade não é a da Lista 8.2, mas sim uma inclusão de biblioteca simples em seu código VHDL que se parece:

Structural modeling in VHDL supports hierarchical design concepts. The ability to abstract digital circuits to higher levels is the key to understanding and designing complex digital circuits.

Digital design using schematic capture is an outdated approach: you should resist the inclination and/or directive at all costs.

The VHDL structural model supports the reuse of design units. This includes units you have previously designed as well as the ability to use predefined module libraries.

If you use one FPGA software development tool from one of the major FPGA players in the market, you will be able to use digital blocks already developed once you declare them. In this case the entity declaration is not the one of Listing 8.2 but instead a simple library inclusionin your VHDL code that looks like:

```vhdl

library UNISIM;
use UNISIM.VComponents.all;
```

All digital blocks available from this library package are described in the documentation of the FPGA software development tool (e.g. Xilinx ISE).
--->

***
### Laços: ###

### Operadores VHDL: ###

#### Operadores Lógicos ####

#### Operadores Relacionais ####

#### Operadores de Deslocamento ####

#### Operador Outros (`others`) ####

#### Operadores de Concatenação ####

#### Operadores Módulo e Resto ####

#### Circuitos Sequenciais ####

#### Elementos de Armazenamento ####



Elementos de armazenamento em VHDL são inferidos pela ausência da especificação do valor de saída para qualquer, possível, condição de entrada.

A geração não intencional de elementos de armazenamento geralmente é listada pelo sintetizador como geração de `latch`. Mais uma vez, os `latchs` são geradas quando há pelo menos uma condição de entrada que não possui uma especificação de saída correspondente.

Os elementos de memória podem ser induzidos tanto:

-   No estilo de modelagem por fluxo de dados;
-   Quanto no estilo de modelagem comportamental.

Se um sinal for declarado na entidade como sendo de saída (`out`), ele não poderá aparecer no lado direito de um operador de atribuição de `signal`. Esta limitação pode ser contornada usando-se `signals` intermediários para quaisquer atribuições funcionais. Em seguida, atribui-se o `signal` intermediário ao `signal` de saída (uma atribuição concorrente).

A especificação de modo de `buffer` deve ser evitada. Em seu lugar pode-se utilizar a declaração de `signals` intermediários.

### Generate if ###

***
### Máquinas de Estados Finitos ###


<!---  Important Points
 Modeling FSMs from a state diagram is a straightforward process using VHDL behavioral modeling. The process is so straightforward that it is often considered cookie cutter. The real engineering involved in implementing FSM is in the generation of the state diagram that solved the problem at hand.

Due to the general versatility of VHDL, there are many approaches that can be used to model FSMs using VHDL. The approach used here details only one of those styles but is generally considered the most straightforward of all styles.

The actual encoding of the FSM’s state variables when enumeration types are used is left up to the synthesis tool. If a preferred method of variable encoding is desired, using the attribute approach detail in this section is a simple but viable alternative.  --->

***

### RTL ###
<!--- Important Points
VHDL can be used to easily implement circuits at the register transfer level. The corresponding VHDL models can be implemented in either structural of full behavioral format.

RTL level VHDL models should strive for simplicity in their designs.
If the behavioral models in the RTL design become complicated, the chances that your circuit works correctly greatly diminish due to the synthesis of the complicated circuit. --->

<br><br>

***

<a name="tabelaPalavrasReservadas"></a>

## Palavras Reservadas: ##

São identificadores reservados da linguagem VHDL. Possuem propósito especial e não devem ser utilizadas para declarar identificadores no código sendo escrito.

| Palavra  | Utilização |  
|----|--------------------------------------------|
| abs | Operador. Valor absoluto do operando à direita. Não usa: () |
| access | Usado para definir um tipo de acesso, um ponteiro |
| after | Especifica um atraso |
| alias | Criar outro nome para um identificador existente |
| all | Desreferencia o que precede o .all |
| and | Operador lógico "e". Operandos ficam à esquerda e direita |
| architecture | Unidade de projeto |
| array | Usado para definir um array, vetor ou matriz |
| assert | Verificação do programa feita por ele mesmo |
| attribute | Usado para declarar atributos de funções |
| begin | Início de um trecho definido por begin/end |
| block | Início de uma estrutura de bloco |
| body | Utilizado na declaração de pacote: "package body" |
| buffer | Um modo de um sinal |
| bus | Um modo de um sinal, pode ter vários sinais internos |
| case | Parte do comando case |
| component | Inicia a definição de um componente |
| configuration | Uma unidade de projeto primária |
| constant | Declara que um identificador é somente de leitura |
| disconnect | Condição de um sinal |
| downto | Indica um intervalo decrescente: 31 downto 0 |
| else | Parte do comando "if" |
| elsif | Parte do comando "if" |
| end | Parte de muitos comandos, pode ser seguido por palavra reservada ou identificador |
| entity | Uma unidade de projeto primária |
| exit | Instrução sequencial, usada em laços |
| file | Usado para declarar um arquivo |
| for | Início de um comando de laço |
| function | Inicia declaração e corpo de uma função |
| generate | Fazer cópias, possivelmente usando um parâmetro |
| generic | Introduz uma parte genérica de uma declaração |
| group | Coleção de tipos que podem receber um atributo |
| guarded | Causa uma espera até que um sinal mude de Falso para Verdadeiro |
| if | Usado no comando "if" |
| impure | Uma função impura é suposta como tendo efeitos colaterais |
| in | Indica um parâmetro de entrada |
| inertial | Característica de um sinal |
| inout | Indica que um parâmetro é de entrada e saída |
| is | Usado como um conectivo em várias declarações |
| label | Nome de atributo usado como especificação de entidade |
| library | Designa um nome de biblioteca |
| linkage | Um modo para uma porta, usado como buffer e inout |
| literal | Usado na declaração de atributo de grupos |
| loop | Instrução sequencial: loop ... end loop; |
| map | Usado para mapear parâmetros, como no _port map_ |
| mod | Operador. Módulo do operando à esquerda pelo operando da direita |
| nand | Operador. "NAND" entre operandos da esquerda e direita |
| new | Aloca memória e retorna ponteiro de acesso |
| next | Instrução sequencial, usada em laços (loop) |
| nor | Operador. "NOR" de operandos à esquerda e direita |
| not | Operador. complemento de operando à direita |
| null | Pode ser uma instrução sequencial que não faz nada ou um valor |
| of | Usado em declarações de tipo: nome "of" TIPO; |
| on | Usado como um conectivo em várias declarações |
| open | Trabalhar com arquivo |
| or | Operador. "OU" lógico entre operandos da esquerda e direita |
| others | Preencher os dados faltantes, pode até ser todos |
| out | Indica que um que é uma saída |
| package | Uma unidade de projeto contendo subprogramas, funções, componentes, etc... Também pode ser: package body |
| port | Definição de interface. Também pode ser: port map |
| postponed | Faz o "process" esperar por todos os processos não adiados |
| procedure | Um procedimento de programação |
| process | Define o código sequencial ou concorrente a ser executado |
| pure | Uma função pura pode não ter efeitos secundários |
| range | Utilizado nas definições de tipo: range 1 to 10; |
| record | Define um novo tipo de registro |
| register | Modificador de parâmetro do sinal |
| reject | Cláusula no mecanismo de atraso (delay). Deve ser seguido por um valor de tempo |
| rem | Operador. Resto da divisão do operando da esquerda pelo da direita |
| report | Instrução e cláusula utilizada na instrução "assert". Envia uma "string" para a saída |
| return | Declaração usada em procedimento ou função |
| rol | Operando da esquerda é rotacionado à esquerda o total de vezes indicado no operando da direita |
| ror | Operando da esquerda é rotacionado à direita o total de vezes indicado no operando da direita |
| select | Instrução de seleção para atribuição de valor a um sinal |
| severity | Utilizado com o "assert" e "report" |
| signal | Declaração de que um objeto é um sinal |
| shared | Usado para declarar objetos compartilhados |
| sla | Operador. Operando da esquerda sofre deslocamento aritmético para a esquerda o total de vezes indicado no operando da direita |
| sll | Operador. Operando da esquerda sofre deslocamento lógico para a esquerda o total de vezes indicado no operando da direita |
| sra | Operador. Operando da esquerda sofre deslocamento aritmético para a direita o total de vezes indicado no operando da direita |
| srl | Operador. Operando da esquerda sofre deslocamento lógico para a direita o total de vezes indicado no operando da direita |
| subtype | Declaração que restringe um tipo existente |
| then | Parte do teste de condição "if" |
| to | Indicador intermediário de um intervalo: range 1 to 10 |
| transport | Característica do sinal |
| type | Declaração para criar um novo tipo |
| unaffected | Indica, dentro de uma condicional, que um sinal não deve ser receber um novo valor |
| units | Usado para definir novos tipos de unidades |
| until | Usado na instrução "wait" |
| use | Define a utilização de um pacote para a unidade de projeto atual |
| variable | Declaração de que um objeto é uma variável |
| wait | Instrução sequencial. Também é usada na instrução "case" |
| when | Usado para escolhas na instrução "case" e outras |
| while | Tipo da instrução "loop" |
| with | Usado na instrução "select" para definir o sinal usado na seleção |
| xnor | Operador. "XNOR" entre operandos da esquerda e direita |
| xor | Operador. "XOR" entre operandos da esquerda e direita |

<a name="fimDocumento"></a>
[Ir para o início do documento](#inicio).
