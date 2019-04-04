<a name="inicio"></a>

# Aula 2: Elementos de um Computador Simplificado

## Objetivos:

1. Projetar circuito (decodificador) de endereçamento;
2. Implementar um registrador em VHDL;
3. Aplicar o tipo de dados *`array`* do VHDL;
4. Implementar memória RAM em VHDL.

***

## Atividade: Endereçamento

### Mapa de memória

Para o circuito abaixo, qual o mapeamento de memória implementado?

Esse mapeamento é de memória ou de E/S?

![Decodificador](./imagensCircuitos/decoder-1.jpg "Decodificador de Endereços")

Para entender o funcionamento dos CIs usados, consulte a [Lista dos Circuitos Integrados TTL](https://en.wikipedia.org/wiki/List_of_7400-series_integrated_circuits "Família 74XX").

***

No decodificador abaixo, de um computador de 16 bits, foram utilizadas todas as linhas de endereçamento disponíveis.

Esse tipo de decodificação é chamada de [exaustiva ou completa][exaustiva] - ela seleciona um único endereço de memória.

![Decodificador de E/S](./imagensCircuitos/I_O-decoder.jpg "Decodificador de E/S")

Nesse caso, é possível mudar o endereço para 0xF500?

Quais as modificações necessárias?

***

<!---
A decodificação incompleta, ou parcial, faz com que o trecho de memória endereçado se repita no mapa de memória
--->

Desenhe o mapa de memória para o projeto abaixo.

![Sistema Mínimo com o 8085] [Sistema8085]

***

## Atividade: Registrador em VHDL.

Queremos implementar o registrador de 8 bits mostrado abaixo:

![Imagem do Registrador] (imagensComponentes/registrador8bitsPCFS.png)

Para criar um registrador, inicialmente, criaremos o esqueleto do circuito:

-   Crie um novo arquivo com o nome *`registrador`*;
-   Adicione esse arquivo ao projeto.
-   Adicione ao arquivo a biblioteca IEEE e a cláusula de uso para: *`ieee.std_logic_1164.all`*;
-   Crie uma entidade chamada *`registrador`* ;
-   Crie uma arquitetura chamada *`comportamento`*;
-   Defina a [*Top Level Entry*][topLevelEntity] para a entidade desse arquivo;

>    É importante usar o nome *`registrador`* para o arquivo e entidade, pois reutilizaremos esse arquivo no projeto hierárquico.

**Personalização do código:**

**Entidade:**

A largura de dados do registrador será definida com:

-   O tipo de dados da biblioteca **IEEE**: ***std_logic_vector***:
    -   Com o seu limite superior definido por um parâmetro.
-   A declaração *`generic`*:
    -   Onde está definido o valor padrão desse parâmetro.

No nosso caso, definiremos a largura de dados do registrador em 8 bits.

Também adicionaremos um sinal de habilitação (Enable) e outro de reinicialização (Reset).

<!--
O código da *`Entity`* será similar a [este código][entidadeRegistrador].
-->

**Arquitetura:**

O funcionamento do registrador, definido dentro da *Architecture*, será feito com:

-   O template *`Basic Positive Edge Register with Asynchronous Reset and Clock Enable`*.
-   Portanto, insira esse *template* dentro da *`architecture`*:

O funcionamento é similar ao flip flop tipo D, porém, a atualização da saída é executada para o vetor todo.

Lembre que o *reset* deve ser feito em todo o vetor. Para tanto, utilize o comando:

-   DOUT <= (OTHERS => '0');

Ele faz com que todos os bits do registrador, na quantidade definida no parâmetro *`generic`*, recebam a atribuição do nível lógico '0'.

[Compile][compilacao] o circuito e verifique, com o [RTL Viewer][rtlViewer], se o resultado da compilação foi o [desejado][rtlREG].

**Simulação:**

Para testar o registrador, precisaremos de:

-   Sinal de *clock*;
-   Sinal de entrada de dados com a largura definida no *`generic`*.

Na simulação, como foi definida a largura de 8 bits para o registrador, o vetor de teste pode ser agrupado em 8 bits e exibido em hexadecimal. Veja uma opção para fazer o [vetor de estímulos][vetorREG].

Verifique o [resultado][simulREG] da simulação.

***

## Atividade: Memória em VHDL

#### Dicas

-   Pense qual resultado que deseja obter:

    -   Esboce no papel um diagrama representando esse objetivo;

    -   Ou uma tabela da verdade. Ou o que for mais adequado.

-   Monte a estrutura básica do VHDL no seu arquivo de trabalho:

    -   Utilize um componente por arquivo;

    -   O nome do arquivo deve ser o nome da entidade desse componente;

    -   Assim é mais fácil de reutilizá-lo no futuro.

-   Para alguns casos, o uso da configuração com *generics* permite:

    -   Criar componentes mais versáteis, com largura de entrada/saída parametrizáveis.

    -   Aumentando a possibilidade de reutilização desse código.

-   Verifique se o esquema RTL é funcionalmente similar ao seu objetivo de implementação.

-   Simule o funcionamento do seu circuito. Se houver uma tabela da verdade:

    -   Ela já indica os vetores de entrada e os resultados na saída.

    -   Caso não exista ou a quantidade de possibilidades é muito grande:

        -   Fique atento para os casos nos extremos da sua faixa de valores de entrada.

***

### Contextualização:

#### Lógica sequencial e memórias.

De uma forma muito geral, podemos dividir as memórias em dois grupos:

-   As que podem ser lidas e escritas dinamicamente:
    -   RAM (*Random Access Memory*);
-   As que podem ser escritas somente durante a sua fabricação/implementação no produto e lidas dinamicamente:
    -   ROM (*Read Only Memory*).

As memórias podem ser vistas como um *array* bidimensional:

-   Onde cada elemento é um registrador (o elemento básico da lógica sequencial);
-   Esses elementos são agrupados para formar a largura da palavra da memória.
-   E esses grupos de registradores podem ser endereçados de forma unívoca:
    -   Através de um circuito decodificador de endereços:
        -   Que decodifica o endereço de entrada para uma única linha de palavra.
-   Como é um *array* bidimensional, cada elemento individual (bit):
    -   Pode ser identificado através do endereço da palavra a que pertence, e da sua posição de bit dentro dessa palavra.

<br>

O esquema de uma memória RAM de 4 bits e 4 posições:

![](imagensComponentes/memoriaRAM.png)

<br>

Na memória estática, para cada célula (bit), temos um circuito similar ao abaixo:

<br>

![](imagensComponentes/SRAM_Cell_Inverter_Loop.png)

***

#### Arrays em VHDL.

Como visto acima, a abstração de uma memória é o *array*. Portanto, faz todo sentido utilizar um *array em VHDL* para descrever uma memória.

Em VHDL, o *`array`* é um tipo de dados composto:

-   Contendo uma coleção de dados de um mesmo tipo:
    -   Diferindo do *`record`*, que é uma coleção de dados de tipos diferentes.
-   Com a localização desses dados indexada através de um valor do tipo escalar.

Um exemplo de *`array`* é o *std_logic_vector*, que é um *array* de dados contendo somente dados do tipo std_logic.

Sua definição, mostrada abaixo, está no pacote *std_logic_1164* da biblioteca *ieee*.

```vhd
    type std_logic_vector is array (natural range <>) of std_logic;
```

A declaração de um *`array`* pode ser feita de duas formas:

-   Com uma faixa irrestrita de valores para o índice:
    -   Como a definição, acima, do *std_logic_vector*;
    -   Nesse caso, na declaração de uso do *`array`* também deve ser declarada a restrição de faixa.
-   Com uma faixa determinada de valores para o índice.

Para uma faixa numérica determinada a declaração é esta:

```vhd
    type word is array (31 downto 0) of bit;
```

No caso das memórias precisamos de um `array` bidimensional. Ele pode ser descrito utilizando um tipo que é um `array` de um subtipo:

```vhd
    subtype word_t is std_logic_vector((DATA_WIDTH-1) downto 0);
    type memory_t is array(2**ADDR_WIDTH-1 downto 0) of word_t;

    signal ram : memory_t;
```

Como o índice do `array` é do tipo escalar:

-   Se o endereço da memória estiver definido como `std_logic_vector`:
    -   Deverá ser feita a conversão de tipos;
    -   Tanto na leitura quanto na escrita dos dados.

```vhd
    endereco    : in std_logic_vector((larguraEndBancoRegs-1) downto 0);
    ...
    saida <= ram(to_integer(unsigned(endereco)));
    ...
    ram(to_integer(unsigned(endereco))) <= dadoEntrada;
```

-   Se o endereço da memória estiver definido como natural:
    -   A conversão de tipos é desnecessária.

```vhd
    endereco    : in natural range 0 to 2**larguraEndBancoRegs - 1;
    ...
    ram(endereco) <= dadoEntrada;
    ...
    saida <= ram(endereco);
```

<br>

Em outras implementações, que não seja algum tipo de memória, a faixa do `array` pode ser um tipo enumerado:

```vhd
    type etapas is (inicial, primeira, segunda, terceira, final); -- enumeração

    type etapasConsideradas is array (primeira to terceira) of natural;
```

Além disso, o *`array`* em VHDL possui alguns atributos:

-   ARRAY'left: limite esquerdo da faixa de índices de ARRAY;
-   ARRAY'right: limite direito da faixa de índices de ARRAY;
-   ARRAY'range: a faixa de índices de ARRAY;
-   ARRAY'reverse_range: a faixa invertida de índices de ARRAY;
-   ARRAY'length: o comprimento da faixa de índices de ARRAY.

#### Memória e FPGA

A FPGA possui, além dos blocos lógicos, os blocos de DSP e os blocos dedicados de memória.

Para pequenas quantidades de memória, pode-se implementar utilizando os registradores dos blocos lógicos. Porém, para tamanhos maiores de memória, pode-se economizar os blocos lógicos usando os blocos de memória.

Para fazer com que a ferramenta de síntese mapeie o código VHDL para os blocos de memória, são necessários alguns cuidados:

-   Usar memória síncrona;
-   Evitar uso de *reset* no código da memória;
-   Verificar se a leitura durante a escrita, se existir, é coerente com o modelo da FPGA;
-   Entre outros.

A Intel (Altera) indica, no manual de boas práticas de codificação, que sejam utilizados os modelos por ela fornecidos. Veja os modelos disponíveis nos *templates* do Quartus e no site da Altera:

<https://www.altera.com/support/support-resources/design-examples/design-software/vhdl.html>

***

### Objetivo

Codificar um bloco de memória RAM com:

-   Largura de 8 bits;
-   1024 posições;
-   Sinal de habilitado: *enable* ou *chip-enable* (CS);
-   Síncrona.

Crie o seu projeto e codifique a memória.

Para a simulação, além da leitura e escrita, não se esqueça de testar todos os sinais de controle.


<br><br>

## Referências

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

***

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!---
######### (inicio dos links) ##########
--->

[linksUteis]: ./linksUteis.html

[exaustiva]: https://en.wikipedia.org/wiki/Memory-mapped_I/O

[Sistema8085]: ./imagensCircuitos/cpu8085.png "Endereçamento no 8085"

[topLevelEntity]: ./quartus/_recursosQuartus.html#configurar-a-top-level-entity

[compilacao]: ./quartus/_compilarProjetoQuartus.html

[rtlViewer]: ./quartus/_rtlViewerQuartus.html

[simulREG]: ./vhdl/_simulacaoRegistrador.html

[rtlREG]: ./vhdl/_rtlRegistrador.html

[vetorREG]: ./vhdl/_simulacaoConfigRegistrador.html

***

***
