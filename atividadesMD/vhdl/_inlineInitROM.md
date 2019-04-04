# ROM com a Inicialização em VHDL

O endereçamento da memória é feito com o tipo _integer_ definido por uma determinada faixa de valores _natural_.

Por sua vez, a interface dos módulos, em geral, é do tipo _std_logic_.

Para criar um padrão de interface, temos duas possibilidades:

-   Pode-se manter a interface dos endereços como _std_logic_vector_;

-   Pode-se manter a interface dos endereços como _integer_.

Para a simulação é mais interessante usar _std_logic_vector_ que possui 9 estados.

---

<br>

## Inicialização de ROM com Interface usando o Tipo _std_logic_vector_

Para manter a interface da sua memória em **std_logic_vector**:

-   Na sua entidade, mantenha a entrada de endereçamento com o tipo std_logic_vector;

-   Como a memória precisa que o endereçamento seja do tipo natural:

    -   Faça a conversão somente na momento da leitura.

```
    Dado <= memROM (to_integer(unsigned(Endereco)));
```

<br>

No caso da memória síncrona, é necessário manter o _process_ com a lista de sensibilidade **contendo somente o sinal do clock**.

```vhdl
process(clk)
begin
  if(rising_edge(clk)) then
    Dado <= memROM (to_integer(unsigned(Endereco)));
  end if;
end process;

```

<br>

Para a memória assíncrona, pode-se remover todo o _process_ e manter somente a atribuição do conteúdo.

```
        Dado <= memROM (to_integer(unsigned(Endereco)));
```

<br>

### Exemplo de Memória Síncrona

```vhdl
library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;

entity memoria IS
     generic (
          dataWidth: natural := 8;
          addrWidth: natural := 3
     );
    port (
        clk : IN STD_LOGIC;
            Endereco : IN STD_LOGIC_VECTOR (addrWidth-1 DOWNTO 0);
        Dado : OUT STD_LOGIC_VECTOR (dataWidth-1 DOWNTO 0)
    );
end entity;

architecture sincrona OF memoria IS
   type blocoMemoria IS ARRAY(0 TO 2**addrWidth - 1) OF std_logic_vector(dataWidth-1 DOWNTO 0);

    function initMemory
        return blocoMemoria is variable tmp : blocoMemoria := (others => (others => '0'));
    begin
            -- Inicializa os endereços:
        tmp(0) := x"AA";
        tmp(1) := x"42";
        tmp(2) := x"43";
        tmp(3) := x"44";
        tmp(4) := x"45";
        tmp(5) := x"46";
        tmp(6) := x"47";
        tmp(7) := x"55";
        return tmp;
    end initMemory;

    signal memROM : blocoMemoria := initMemory;

begin
    process(clk)
    begin
    if(rising_edge(clk)) then
          Dado <= memROM (to_integer(unsigned(Endereco)));
    end if;
    end process;

end architecture;

```

<br>

### Exemplo de Memória Assíncrona

```vhdl

library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;

entity memoria IS
   generic (
          dataWidth: natural := 8;
          addrWidth: natural := 3 );
   port (
        clk : IN STD_LOGIC;
            Endereco : IN STD_LOGIC_VECTOR (addrWidth-1 DOWNTO 0);
        Dado : OUT STD_LOGIC_VECTOR (dataWidth-1 DOWNTO 0) );
end entity;

architecture assincrona OF memoria IS
  type blocoMemoria IS ARRAY(0 TO 2**addrWidth - 1) OF std_logic_vector(dataWidth-1 DOWNTO 0);

  function initMemory
        return blocoMemoria is variable tmp : blocoMemoria := (others => (others => '0'));
  begin
            -- Inicializa os endereços:
        tmp(0) := x"AA";
        tmp(1) := x"42";
        tmp(2) := x"43";
        tmp(3) := x"44";
        tmp(4) := x"45";
        tmp(5) := x"46";
        tmp(6) := x"47";
        tmp(7) := x"55";
        return tmp;
    end initMemory;

    signal memROM : blocoMemoria := initMemory;

begin
  Dado <= memROM (to_integer(unsigned(Endereco)));
end architecture;

```

<br>

---

## Inicialização de ROM com Interface Usando o Tipo _integer_

### Exemplo de Memória Síncrona

```vhd
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity romMif is

    generic
    (
        DATA_WIDTH : natural := 8;
        ADDR_WIDTH : natural := 8
    );

    port (
        clk: in std_logic;
        addr: in natural range 0 to 2**ADDR_WIDTH-1;
        q: out std_logic_vector (DATA_WIDTH-1 downto 0)
    );
end entity;

architecture inLineInitROM of romMif is

type memory_t is array (2**ADDR_WIDTH-1 downto 0) of std_logic_vector (DATA_WIDTH-1 downto 0);

    function init_rom
        return memory_t is
        variable tmp : memory_t := (others => (others => '0'));
        begin
        tmp(0) := x"49";
        tmp(1) := x"6e";
        tmp(2) := x"73";
        tmp(3) := x"70";
        tmp(4) := x"65";
        tmp(5) := x"72";
        tmp(6) := x"20";
        tmp(7) := x"21";
        return tmp;
    end init_rom;

signal content: memory_t := init_rom;

begin
    process(clk)
    begin
        if (RISING_EDGE(clk)) then
            q <= content(addr);
        end if;
    end process;
end architecture;

```

***

<br>

***

***

<!-- FIM -->
