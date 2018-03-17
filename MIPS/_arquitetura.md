<a name="inicio"></a>

# MIPS DLX

##### (baseado no capítulo 4 do livro texto)

A arquitetura do MIPS DLX é uma simplificação e atualização da arquitetura original do MIPS. Ela é, principalmente, utilizada para fins didáticos e existem implementações _opensource_.

Suas características principais são:

-   Processador RISC de 32 bits;

-   Arquitetura do tipo _Load/Store_;

-   Possui 32 registradores de uso geral (alguns possuem uso bem definido);

-   Endereçamento de 2^30 palavras de memória (2^32 bytes = 4GBytes);

-   O endereço da memória tem granularidade de um byte (endereços de 32 bits).

-   O acesso à memória é feito com endereços que diferem de 4 bytes (uma _word_):

    -   Esse alinhamento é obrigatório.

-   Formato regular para as instruções;

-   Conjunto de instruções dividido em 6 classes;

-   Não possui _flags_ de estado;

-   _Big Endian_;

-   Não possui suporte de _hardware_ para gerenciar pilhas;

-   Pipeline de 5 estágios;

-   Interrupção.

---

Filosofias do projeto MIPS:

-   Simplicidade favorece a regularidade;

-   Um bom projeto exige um bom compromisso;

-   Menor é mais rápido;

-   Faça as tarefas comuns serem as mais rápidas.

---

## Processador de 32 bits

Todas as instruções MIPS possuem 32 bits de comprimento e o acesso à memória é feito com granularidade de 32 bits.

O endereço de memória também é de 32 bits. Isso simplifica o _hardware_ de carga e decodificação de instruções.

Como o MIPS não possui instruções que utilizam mais do que uma palavra (mais de um acesso à memória para obter a instrução completa), existe um número finito de instruções.

Apesar do acesso à memória ser de 4 bytes (32 bits), o endereçamento de memória é orientado a byte. Dessa forma, cada endereço se refere a uma posição de memória contendo apenas 1 byte (8 bits).

Isso implica que uma palavra do processador, quando armazenada na memória, ocupará 4 posições de memória (quatro endereços consecutivos) e deve iniciar em endereços que são múltiplos de 4. Este requisito é chamado de restrição de alinhamento.

---

## Arquitetura do tipo _Load/Store_

O MIPS só pode fazer operações lógicas e aritméticas entre registradores ou entre registradores e constantes imediatas.

Um registrador recebe (_load_) um valor armazenado na memória através de uma instrução que só faz a carga. Por outro lado, o conteúdo de um registrador pode ser armazenado (_store_) na memória através de uma instrução específica para isso.

---

## Banco de Registradores

O MIPS possui 32 registradores de uso geral e outros 32 registradores de ponto flutuante (que não serão abordados).

O hardware MIPS não impõe um uso específico para os registradores de uso geral (exceto r0). Ou seja, onde um registrador é necessário, qualquer registrador funcionará.

No entanto, a seguinte convenção para o uso dos registradores evoluiu como padrão para a programação MIPS. Ela é usada pela maioria das ferramentas, compiladores e sistemas operacionais:

  | Registradores | Nome | Descrição
  | :-: | :- | :----------------------------
  | 0  | \$zero | Sempre retorna 0, não é modificável. A escrita é ignorada.
  | 1  | \$at | Reservado para uso do montador (_assembler temporary_).
  | 2-3 | \$v0, \$v1 | Valores retornados pela sub-rotina.
  | 4-7 | \$a0-\$a3 | (argumentos) Quatro primeiros parâmetros para a sub-rotina.
  | 8-15 | \$t0-\$t7 | (temporários) Sub-rotinas pode usar sem salvar.
  | 16-23 | \$s0-\$s7 | Para variáveis da sub-rotina, precisa restaurar antes de retornar.
  | 24-25 | \$t8, \$t9 | (temporários) As sub-rotinas podem usar sem salvar.
  | 26-27 | \$k0, \$k1 | Reservado para uso do manipulador da interrupção/trap.
  | 28 | \$gp | Ponteiro Global; usado para acessar variáveis "_static_" ou "_extern_".
  | 29 | \$sp | Ponteiro da pilha (_stack pointer_).
  | 30 | \$s8/\$fp | Ponteiro da estrutura (_frame pointer_) ou nona variável da sub-rotina.
  | 31 | \$ra | Endereço de retorno para chamada de sub-rotina (JAL & JALR).

Existem outros registradores de uso específico:

-   PC, contador de programa, que armazena o endereço da instrução em
    execução.

-   EPC, registrador com o endereço da instrução em que ocorreu a interrupção. Esse é o endereço de retorno da interrupção;

-   Cause, registrador com o código da causa da exceção ocorrida.

<!--- -   FPSR, registrador de estado de ponto flutuante, utilizado para desvio condicional com base no resultado de operações de FP (1 bit). -->

<!--
-   "hi" e "lo", que são usados na multiplicação (quando ocorre um resultado superior a 32 bits) e na divisão (para resultados com quociente e resto). O acesso a esses registradores é feito com instruções especiais.

-->

A identificação dos registradores começam com um cifrão (\$). Em seguida, eles podem ter nomes (\$zero a \$ra) ou números (\$0 a \$31). Ao programar _assembly_ para o MIPS, geralmente é melhor usar os nomes dos registradores.

O registrador \$zero, sempre possui o valor 0 e é somente para leitura. A escrita é ignorada. A pseudoinstrução _nop_ é traduzida para uma escrita nesse registrador.

O registrador \$at (_Assembler Temporary_) é usado para valores temporários dentro de pseudoinstruções (_move, li, la, etc..._). Ele não é preservado através de chamadas de função.

Os registradores \$v armazenam valores de retorno das funções. Não são preservados através de chamadas de função.

Os registradores \$a0 até \$a3 são usados para passar argumentos para funções. Eles não são preservados através de chamadas de função. Se houver mais argumentos, eles serão passados através da pilha.

Os registradores temporários (\$t0 a \$t9) são de uso geral. Não são preservados
através de chamadas de função.

Os registradores "S" (\$s0 a \$s7) são de uso geral. Eles devem ser salvos na entrada de uma rotina e restaurados na saída dela.

Os registradores \$k são reservados para uso do _kernel_ do sistema operacional.

O registrador \$gp é usado como ponteiro para a área que armazena as variáveis globais ou estáticas (_Global Pointer_). Esse ponto é a fronteira entre essas variáveis e a região que armazena as variáveis alocadas dinamicamente (_Heap_). Por isso, ele também serve de ponteiro base para essas variáveis.

O registrador \$sp é usado como ponteiro para a pilha (_Stack Pointer_).

O registrador \$fp é usado como ponteiro para a estrutura de pilha usada na chamada de uma sub-rotina (_Frame Pointer_). Caso não seja utilizada essa estrutura, ele pode ser usado como \$s8.

O registrador \$ra é usado como ponteiro para o endereço de retorno na chamada de sub-rotinas.

No caso dos registradores que não são preservados através da chamada de uma função, caso possuam dados importantes, é responsabilidade do programador preservar seus valores.

A convenção, no caso do MIPS, é que a responsabilidade por preservar os registradores seja dividida entre a rotina chamante e a rotina chamada.

A rotina que chama a função, é responsável por salvar e recuperar os registradores (caso utilize):

-   Temporários: \$t0-$t9;

-   Argumentos: \$a0-$a3;

-   Valores de retorno: \$v0-$v1.

Dessa forma, a rotina chamada possui liberdade para alterar os valores desses registradores sem se preocupar se eles são utilizados na rotina chamante.

A rotina que é chamada (a própria função), é responsável por salvar e recuperar os registradores:

-   Os registradores de uso geral: \$s0-$s7;

-   O ponteiro para o endereço de retorno: \$ra (usado pela instrução: jal).

Ou seja, a rotina chamante pode considerar que esses registradores não foram alterados pela rotina chamada.

Um registrador pode ser carregado com um byte (8 bits); com meia palavra (_halfword_: 16 bits) ou uma palavra inteira (32 bits).

---

## Endereçamento

<!--Fazer desenho para cada tipo de endereçamento. -->

No caso do MIPS, ele se restringe às instruções de leitura e escrita na memória. O endereçamento pode ser:

-   Direto Imediato:

    -   Usa como destino um ponto definido no programa (_label_). O deslocamento é dado pelo valor imediato (16 bits com sinal) dentro da instrução;

-   Indireto:

    -   Usa o valor de um registrador como endereço.

-   Indexado:

    -   Utiliza um endereço base, dado pelo conteúdo de um registrador;

    -   Somado a um deslocamento (índice ou _offset_) definido na instrução;

    -   O deslocamento pode ser negativo.

O endereçamento indexado é útil no acesso de vetores (_arrays_) e pilhas. É utilizado com o _stack pointer_ e com o _frame pointer_.

---

## Instruções

### Classes das instruções

As instruções do MIPS podem ser divididas em 6 classes.

As 3 classes abordadas aqui:

-   Referência à memória (_load & store_);

-   Lógicas e Aritméticas;

-   Salto e desvio (_jump & branch_);

E as 3 que não abordaremos:

-   Ponto Flutuante;

-   Movimentação (_Move_);

-   Especiais.


A filosofia de projeto do MIPS considera que:

-   Implementar apenas um pequeno núcleo com as instruções mais comuns:

    -   Algumas dezenas e não centenas.

-   Simplifica o projeto:

    -   Aumentando o desempenho dessas instruções.

As instruções ficam armazenadas na mesma memória que o programa (arquitetura von Neumann) e possuem 4 bytes (32 bits), sempre com alinhamento de 4 bytes. Elas operam na memória e nos registradores.

Para facilitar o projeto, os 32 bits das instruções foram agrupados em campos e nomeados:

 | Opcode | Rs | Rt | Rd | shamt | funct |
 |---------- | :----------- | :------------ | :------------ | :---------- | :------------|
 | 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |


O significado dos nomes dos campos:

-   __Opcode__: É o código da instrução a ser executada;

-   __Rs__: O número do registrador com o primeiro operando da instrução definida em _opcode_;

-   __Rt__: O número do registrador com o segundo operando da instrução definida em _opcode_;

-   __Rd__: O número do registrador de destino do resultado da instrução definida em _opcode_;

-   __shamt__: Total de deslocamento (_shift amount_).

-   __funct__: Seleciona uma variação específica da operação definida em _opcode_.

Essa uniformidade na localização do _opcode_ e dos endereços dos registradores facilita o projeto do hardware.

### Formato dos tipos de instruções

O processador MIPS DLX possui 3 tipos distintos de formatos para as instruções: tipo R, I e J. Cada uma delas, utiliza de forma distinta os campos, podendo agrupá-los.

As instruções do tipo R (_register_) tem _opcode_ 0x0 e trabalham com 3
registradores:

-   Rs e Rt são os registradores fonte (contém os argumentos);

-   Rd é o registrador de destino do resultado da operação;

-   O campo “_funct_”, define a função a ser realizada.


| Formato | Bits:    |          |          |          |         |        |
| :-------: | :--------: | :--------: | :--------: | :--------: | :--------: | :------: |
|         | 31 \~ 26 | 25 \~ 21 | 20 \~ 16 | 15 \~ 11 | 10 \~ 6 | 5 \~ 0 |
| tipo R  | 0x0      | Rs       | Rt       | Rd       | sem uso | funct  |

---

As instruções do tipo I (_immediate_) trabalham com 2 registradores e um valor imediato:

-   Rs é o registrador fonte e Rd é o registrador de destino do resultado da operação.

-   O valor imediato possui 16 bits e terá seu bit de sinal estendido, para 32 bits, antes do uso.

-   A instrução é definida pelo _opcode_ e inclui:

    -   As instruções de carga e armazenamento;

    -   As instruções que operam com valores imediatos;

    -   As instruções de desvios condicionais (_branchs_) e desvios com ligação (_link_).


| Formato | Bits:    |          |          |          |
| :-------: | :--------: | :--------: | :--------: | :----------: |
|         | 31 \~ 26 | 25 \~ 21 | 20 \~ 16 | 15 \~ 0  |
| tipo I  | opcode   | Rs       | Rd       | valor imediato (16 bits) |

---

As instruções do tipo J (_jump_) trabalham com um operando:

-   Esse operando possui 26 bits e é usado para calcular o endereço de destino do salto.

São instruções de salto incondicional.

| Formato | Bits:    |          |
| :-------: | :--------: | :--------: |
|         | 31 \~ 26 | 25 \~ 0 |
| tipo J  | opcode   | valor imediato (26 bits) |


Dependendo do destino desejado para o salto, os 26 bits do valor imediato podem não ser suficientes. Como todas palavras, na memória, são alinhadas a cada 4 bytes:

-   Os dois bits menos significativos, de qualquer endereço de memória, serão sempre zero:

    -   Por imposição do _hardware_.

-   Consegue-se assim, que o endereço definido pelo valor imediato seja, virtualmente, de 28 bits (endereçando 256MB de memória).

Ainda faltam 4 bits para especificar o destino do salto:

-   Eles são definidos pelos 4 bits mais significativos do endereço da instrução atual;

-   Como o valor imediato possui sinal:

    -   Pode-se acessar, até 128MB, para a frente do endereço atual;

    -   Ou, até 128MB, para trás do endereço atual.

---

## Flags, endianess e pilhas

A arquitetura MIPS não possui registradores (ou _Flags_) específicos para indicar se o resultado de uma operação possui qualificadores (se o resultado da operação é zero; se houve transbordo (_overflow_); se houve geração de vai um (_carry_); etc...).

A detecção dessas condições deve ser feita pelo programador, utilizando as instruções com prefixo SLT (_set less than_). Elas são avaliadas através do conteúdo dos registradores.

O MIPS não possui instruções específicas para trabalhar com pilhas (_push_ e _pop_). É trabalho do programador, conforme o uso, administrar o valor do ponteiro da pilha.

O MIPS original podia utilizar a disposição de bytes, na memória e registradores, do tipo _little endian_ ou _big endian_.

No caso do __DLX__, a disposição dos bytes é feita na forma ___big endian___.

![](../imagensMIPS/registerMemoryBigEndianMediaPCFS.svg)

---

## Execução das Instruções

Todas instruções do MIPS podem ser encaixadas na seguinte sequência de eventos:

-   Busca da instrução na memória (_Instruction Fetch_: IF);

-   Decodificação da instrução e leitura dos registradores durante a decodificação (_Instruction Decode_: ID);

-   Execução da operação ou cálculo de um endereço (_Execute_: EX);

-   Acesso à memória (_Memory Access_: MEM);

-   Escrita do resultado em um registrador (_Write Back_: WB).

As duas primeiras etapas são comuns a todas as instruções, indistintamente.

### Etapa IF

Busca a próxima instrução na memória, utilizando o endereço no registrador PC (_Program Counter_), e armazena esta instrução no IR (_Instruction Register_).

### Etapa ID

A etapa ID executa duas tarefas:

-   Calcular o próximo valor do PC;

-   Buscar os operandos (endereçar os registradores) para a instrução atual.

Existem três possibilidades para o próximo valor do PC:

-   Para as instruções que não fazem desvios: o endereço da próxima instrução é a soma do valor 4 ao valor atual do PC (PC = PC + 4).

-   Para os saltos e desvios (_jump_ e _branch_): pode ser necessário adicionar um valor imediato (o deslocamento do _branch_) ao PC. Esse valor imediato está codificado na própria instrução.

-   Para as instruções de salto indexado por registrador (jr e jalr): é usado o conteúdo de um registrador com o endereço de destino. As instruções que fazem ligação (jal e jalr) salvam o endereço de retorno (__PC+4__) no registrador __$ra__.

### Etapa EX

Utiliza a ALU para fazer os cálculos necessários com os operandos endereçados na etapa ID. Esses operandos podem vir de dois registradores ou um registrador e um valor imediato (codificado na instrução).

### Etapa MEM

Faz a leitura e escrita de operandos na memória. Para isso, o resultado da ALU, com o endereço a ser acessado, é utilizado no acesso. No caso de uma escrita também deve estar disponível o valor a ser escrito na memória.

Como as instruções operam na memória ou em registradores, mas nunca em ambos, as instruções que não acessam a memória, transferem o valor da ALU diretamente para a próxima etapa (WB). Nesse caso, o resultado da ALU deve ser armazenado no registrador definido na instrução.

### Etapa WB

Essa etapa escreve o valor recebido da etapa MEM no registrador definido na instrução. Para as instruções de escrita na memória, a etapa WB não é utilizada.

---

## Pipeline

O pipeline é uma técnica que explora o paralelismo entre as instruções de um fluxo sequencial. Isso permite que, em um mesmo ciclo de _clock_, sejam executadas diferentes fases de diferentes instruções. Ele tem a vantagem de ser transparente ao programador.

O nome MIPS é a abreviação de Microprocessor without Interlocked Pipeline Stages. Isso, porque a versão original possuia um pipeline de 5 estágios sem intertravamento entre esses estágios.

Isso diz muito sobre o projeto original:

-   Se uma instrução durar mais do que um ciclo de _clock_ para executar;

-   Ela não tem como pausar os estágios anteriores do _pipeline_;

-   Para poder terminar a sua execução.

Para trabalhar com essas limitações, no projeto original, foi feito o seguinte:

-   Foram retiradas as instruções mais complexas (como divisão e multiplicação);

-   Foi ajustada cada etapa do pipeline:

    -   Para que as instruções executassem em um único ciclo de _clock_.

Para resolver os outros problemas que poderiam ocorrer, como por exemplo:

-   A leitura de um dado da memória ou acesso de E/S, não é possível executar em um ciclo de _clock_;

-   A dependência de dados na sequência de instruções atravessando o pipeline;

O trabalho foi passado para o tempo de compilação (ou montagem), onde é feita a análise do fluxo de instruções e são inseridos _NOPs_ para evitar essas ocorrências.

Assim, os programas para o MIPS original eram forçados a ter uma quantidade significativa de instruções _NOP_.

No DLX foi utilizada outra abordagem:

-   O encaminhamento de dados dentro do pipeline;

-   Reordenamento de instruções na fase de compilação do programa.

Além disso, as instruções mais longas podem pausar (intertravar) a atividade do pipeline (chamado de _stall_ ou criação de bolha) até que essas instruções possam ser concluídas.

![](../imagensMIPS/5_Stage_PipelineGrandePCFS.svg)

---

## Interrupção

Uma interrupção é a alteração na sequência de execução do programa. Ela pode ser assíncrona, como uma interrupção de _hardware_, ou síncrona, como uma interrupção de _software_ (_syscall_ e _break_), também conhecida como _trap_.

O funcionamento é da seguinte forma:

-   No ponto do programa em que a interrupção acontece:

    -   Contador de programa (PC) é salvo no registrador especial _EPC_.

-   Ocorre um desvio para a rotina de tratamento de interrupção, cujo endereço é 0x80000180, independente da causa da interrupção. Nessa rotina:

    -   É salvo o estado atual da CPU, ou seja, o banco de registradores;

    -   E, de acordo com a causa da interrupção, lida no registrador especial _Cause_, ela executa ações diferentes.

-   No fim dessa rotina, ocorre a restituição do estado anterior da CPU (o banco de registradores) e um salto para o conteúdo do registrador _EPC_;

-   E o programa continua executando no mesmo ponto em que tinha parado, como se não tivesse sido interrompido.

Os registradores _EPC_ e _Cause_, não fazem parte do banco de registradores do MIPS. Para verificar o seu conteúdo, deve-se usar a instrução de movimento: _mfc0_ (_move from coprocessor 0_).

O coprocessador 0, no MIPS, é chamado de _MIPS processor control_ e é o responsável pela interrupção e diagnósticos do processador.

Para transferir o registrador _Cause_ para o registrador _\$t0_  utiliza-se:

```
   mfc0   $t0,   Cause;
```

Para transferir o registrador _EPC_ para o registrador _\$k0_  utiliza-se:
```
   mfc0   $k0,   EPC;
```

E para retornar ao ponto do programa onde ele foi interrompido:

```
   jr     $k0;
```

---

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).
