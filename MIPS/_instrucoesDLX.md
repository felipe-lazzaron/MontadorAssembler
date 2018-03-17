# Descrição das Instruções a Implementar

## Instruções de Referência à Memória

### Carrega palavra (_load word: lw_)

Carrega um registrador, determinado na instrução (\$t), com a palavra localizada na posição de memória que é o resultado da soma do conteúdo do segundo registrador (também definido na instrução: \$s) e o valor imediato. O imediato possui 16 bits.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :-------------------------: |
| lw \$t, imediato(\$s) | I       | 0x23 / NA | \$t = MEM\[endereço]; PC += 4; |

O valor do endereço é dado pela soma de dois inteiros de 32 bits:

-   O primeiro, chamado de base, é o conteúdo do registrador definido na instrução (\$s);

-   E o segundo, chamado de deslocamento, é gerado pela extensão do sinal do campo imediato (que é de 16 bits).

A extensão do sinal do valor imediato, cria um valor de 32 bits, onde:

-   Os 16 bits mais significativos (31~16) = {imediato\[15]}. Ou seja, repete 16 vezes o valor do bit 15 do valor imediato;

-   Os 16 bits menos significativos (15~0) = imediato. Ou seja, o próprio imediato.

O seja, o endereço é a soma do conteúdo do registrador com o seguinte agregado:

-   endereço = ( R\[\$s] + {16{imediato\[15]}, imediato} ).

### Armazena palavra (_store word: sw_)

Armazena o conteúdo de um registrador, definido na instrução (\$t), na posição de memória determinada pela soma do conteúdo de um segundo registrador (também definido na instrução: \$s) com o valor imediato. O imediato possui 16 bits.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :-------------------------: |
| sw \$t, imediato(\$s) | I       | 0x2B / NA | MEM\[endereço] = \$t; PC += 4; |

O valor do endereço é dado pela soma de dois inteiros de 32 bits:

-   O primeiro, chamado de base, é o conteúdo do registrador definido na instrução (\$s);

-   E o segundo, chamado de deslocamento, é gerado pela extensão do sinal do campo imediato (que é de 16 bits).

A extensão do sinal do valor imediato, cria um valor de 32 bits, onde:

-   Os 16 bits mais significativos (31~16) = {imediato\[15]}. Ou seja, repete 16 vezes o valor do bit 15 do valor imediato;

-   Os 16 bits menos significativos (15~0) = imediato. Ou seja, o próprio imediato.

O seja, o endereço é a soma do conteúdo do registrador com o seguinte agregado:

-   endereço = ( R\[\$s] + {16{imediato\[15]}, imediato} ).

---

<br>

## Instruções Lógicas e Aritméticas

### Soma (_add_)

Soma o conteúdo de dois registradores, definidos na instrução, e armazena o resultado em um terceiro registrador (também definido na instrução), que pode, ou não, ser um dos dois anteriores.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :-------------------------: |
| add \$d, \$s, \$t   | R         | 0x0 / 0x20 | \$d = \$s + \$t; PC += 4; |

### Subtração (_sub_)

Faz a subtração entre o conteúdo de dois registradores, definidos na instrução, e armazena o resultado em um terceiro registrador (também definido na instrução), que pode, ou não, ser um dos dois anteriores.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :-------------------------: |
| sub \$d, \$s, \$t | R | 0x0 / 0x22 | \$d = \$s - \$t; PC += 4; |


### E lógico (_and_)

Executa a operação lógica "E", bit a bit, entre o conteúdo de dois registradores, definidos na instrução, e armazena o resultado em um terceiro registrador (também definido na instrução), que pode, ou não, ser um dos dois anteriores.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :-------------------------: |
| and \$d, \$s, \$t | R | 0x0 / 0x24 | \$d = \$s & \$t; PC += 4; |

### OU lógico (_or_)

Executa a operação lógica "OU", bit a bit, entre o conteúdo de dois registradores, definidos na instrução, e armazena o resultado em um terceiro registrador (também definido na instrução), que pode, ou não, ser um dos dois anteriores.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :-------------------------: |
| or  \$d, \$s, \$t   | R         | 0x0 / 0x25 | \$d = \$s \| \$t;  PC += 4; |


### Comparação Menor Que (_set if less than: slt_)

Compara o conteúdo de dois registradores (definidos na instrução) e indica o resultado em um terceiro registrador (também definido na instrução). Usando o exemplo da tabela abaixo, se o conteúdo do registrador \$s for menor que o conteúdo do registrador \$t, o registrador \$d recebe o valor 1. Caso contrário, \$d recebe o valor 0.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :-------------------------: |
| slt \$d, \$s, \$t   | R         | 0x0 / 0x2A | \$d = (\$s < \$t ? 1: 0); PC += 4; |

Os registradores comparados contém inteiros com sinal.

---

<br>

## Instruções de Desvio

### Desvia Se Igual (_branch equal: beq_)

Compara o conteúdo de dois registradores definidos na instrução. Se forem iguais, desvia para o endereço definido por (PC+4)+(extSinal(imediato << 2)). Caso contrário, continua na próxima instrução.

| Instrução       | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :-----: | :---: | :---: | :-----------------: |
| beq \$s, \$t, imediato | I | 0x04 / NA | if(\$s == \$t) PC += 4 + (Imediato << 2) else PC += 4; |

Ou seja, o endereço de desvio é a soma do PC+4 e do agregado:

-   endereço = (PC + 4) + ({14{imediato\[15]}, imediato, 0, 0}).

### Salto incondicional (_jump: j_)


| Instrução | Formato   | Opcode/Funct | Operação (sintaxe estilo C) |
| :--------------: | :-------: | :-------: | :---------------------------: |
| j valor | J | 0x02 / NA | PC = destino; |

O valor de destino é calculado da através do seguinte agregado:

-   destino = {(PC+4)\[31:28] , valor, 0, 0}

Ou seja, os quatro bits mais significativos do PC+4, concatenado com os 26 bits do campo valor, concatenado com dois bits com o valor 0.

---

<br>

## Formato das Instruções

**Tipo R:**

| Formato | Bits:    |          |          |          |         |        |
| :-------: | :--------: | :--------: | :--------: | :--------: | :--------: | :------: |
|         | 31 \~ 26 | 25 \~ 21 | 20 \~ 16 | 15 \~ 11 | 10 \~ 6 | 5 \~ 0 |
| tipo R  | 0x0      | Rs       | Rt       | Rd       | sem uso | funct  |

<br>

**Tipo I:**

| Formato | Bits:    |          |          |          |
| :-------: | :--------: | :--------: | :--------: | :----------: |
|         | 31 \~ 26 | 25 \~ 21 | 20 \~ 16 | 15 \~ 0  |
| tipo I  | opcode   | Rs       | Rd       | valor imediato (16 bits) |

<br>

**Tipo J:**

| Formato | Bits:    |          |
| :-------: | :--------: | :--------: |
|         | 31 \~ 26 | 25 \~ 0 |
| tipo J  | opcode   | valor imediato (26 bits) |

<br>

---

<!--
# Modos de Endereçamento

Registrador:

Sintaxe: load r1, r2;

Semântica: r1 ← (Reg2);

Imediato (16 bits ou 26 bits, depende da instrução):

Sintaxe:  load r1, #const

Semântica:  r1 ← const;

Indireto por registrador:

Sintaxe: load r1, (r2)

Semântica: r1 ← Mem \[(r2)];

Deslocamento (16 bits):

Sintaxe: r1, deslocamento (Reg2);

Semântica: r1 ← Mem\[deslocamento + (Reg2)]

Relativo ao PC (contador de programa):

Sintaxe:  branch deslocamento;

Semântica: PC ←  PC + step + deslocamento (if branch taken)
-->
