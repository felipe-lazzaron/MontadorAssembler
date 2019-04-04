# Exemplos de Componentes em VHDL

## Combinacionais

### Conversor Hexadecimal para Sete Segmentos (display)

Pode ser necessário adicionar um registrador à entrada deste circuito.

```vhdl

library IEEE;
use ieee.std_logic_1164.all;

entity conversorHex7Seg is
    port
    (
        -- Input ports
        dadoHex : in  std_logic_vector(3 downto 0);
        apaga   : in  std_logic := '0';
        negativo : in  std_logic := '0';
        overFlow : in  std_logic := '0';
        -- Output ports
        saida7seg : out std_logic_vector(6 downto 0)  -- := (others => '1')
    );
end entity;

architecture comportamento of conversorHex7Seg is
   --
   --       0
   --      ---
   --     |   |
   --    5|   |1
   --     | 6 |
   --      ---
   --     |   |
   --    4|   |2
   --     |   |
   --      ---
   --       3
   --
    signal rascSaida7seg: std_logic_vector(6 downto 0);
begin
    rascSaida7seg <=    "1000000" when dadoHex="0000" else ---0
                            "1111001" when dadoHex="0001" else ---1
                            "0100100" when dadoHex="0010" else ---2
                            "0110000" when dadoHex="0011" else ---3
                            "0011001" when dadoHex="0100" else ---4
                            "0010010" when dadoHex="0101" else ---5
                            "0000010" when dadoHex="0110" else ---6
                            "1111000" when dadoHex="0111" else ---7
                            "0000000" when dadoHex="1000" else ---8
                            "0010000" when dadoHex="1001" else ---9
                            "0001000" when dadoHex="1010" else ---A
                            "0000011" when dadoHex="1011" else ---B
                            "1000110" when dadoHex="1100" else ---C
                            "0100001" when dadoHex="1101" else ---D
                            "0000110" when dadoHex="1110" else ---E
                            "0001110" when dadoHex="1111" else ---F
                            "1111111"; -- Apaga todos segmentos.

    saida7seg <=     "1100010" when (overFlow='1') else
                            "1111111" when (apaga='1' and negativo='0') else
                            "0111111" when (apaga='0' and negativo='1') else
                            rascSaida7seg;
end architecture;

```

***

### MUX genérico

#### Exemplo de código para o MUX

Abaixo temos o código para um multiplex de duas entradas.

A largura do barramento de entrada (e saída) é definida pela declaração do _generic_.

**Nome do arquivo: muxGenerico2.vhd**

```vhdl

library ieee;
use ieee.std_logic_1164.all;

entity muxGenerico2 is
    generic (
        -- Total de bits das entradas e saidas
        larguraDados    : natural  :=   8
    );
    port (
        entradaA_MUX    : in  std_logic_vector(larguraDados-1 downto 0);
        entradaB_MUX    : in  std_logic_vector(larguraDados-1 downto 0);
        seletor_MUX   : in  std_logic;

        saida_MUX   : out std_logic_vector(larguraDados-1 downto 0)
    );
end entity;

architecture comportamento of muxGenerico2 is
begin
  -- Para sintetizar lógica combinacional usando um processo,
  --  todas as entradas do modulo devem aparecer na lista de sensibilidade.
    process(entradaA_MUX, entradaB_MUX, seletor_MUX) is
    begin
     -- If é uma instrução sequencial que não pode ser usada
     --  na seção de instruções concorrentes da arquitetura.
        if(seletor_MUX='0') then
            saida_MUX <= entradaA_MUX;
        else
            saida_MUX <= entradaB_MUX;
        end if;
    end process;
end architecture;

```

***

### Somador Genérico

```vhdl

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;           --Soma (esta biblioteca =ieee)

entity somadorGenerico is
    generic
    (
        larguraDados : natural := 32
    );
    port
    (
        entradaA, entradaB: in STD_LOGIC_VECTOR((larguraDados-1) downto 0);
        saida:  out STD_LOGIC_VECTOR((larguraDados-1) downto 0)
    );
end entity;

architecture comportamento of somadorGenerico is
    begin
        saida <= STD_LOGIC_VECTOR(unsigned(entradaA) + unsigned(entradaB));
end architecture;

```

***

### Soma com Constante Configurável

```vhdl

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;  --Soma (esta biblioteca =ieee)

entity soma4 is
    generic
    (
        larguraDados : natural := 32;
        incremento : natural := 4
    );
    port
    (
        entrada: in  STD_LOGIC_VECTOR((larguraDados-1) downto 0);
        saida:   out STD_LOGIC_VECTOR((larguraDados-1) downto 0)
    );
end entity;

architecture comportamento of soma4 is
    begin
        saida <= std_logic_vector(unsigned(entrada) + incremento);
end architecture;

```

***

### Extensor de Sinal Genérico

```vhdl

library ieee;
use ieee.std_logic_1164.all;

entity estendeSinalGenerico is
    generic
    (
        larguraDadoEntrada : natural  :=    8;
        larguraDadoSaida   : natural  :=    8
    );
    port
    (
        -- Input ports
        estendeSinal_IN : in  std_logic_vector(larguraDadoEntrada-1 downto 0);
        -- Output ports
        estendeSinal_OUT: out std_logic_vector(larguraDadoSaida-1 downto 0)
    );
end entity;

architecture comportamento of estendeSinalGenerico is
begin
    process (estendeSinal_IN) is
    begin
            if (estendeSinal_IN(larguraDadoEntrada-1) = '1') then
                estendeSinal_OUT <= (larguraDadoSaida-1 downto larguraDadoEntrada => '1') & estendeSinal_IN;
            else
                estendeSinal_OUT <= (larguraDadoSaida-1 downto larguraDadoEntrada => '0') & estendeSinal_IN;
            end if;
    end process;
end architecture;

```

***

***

## Circuitos Sequenciais

### Detector de Borda

Nome do arquivo: edgeDetector.vhd

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity edgeDetector is
     Port ( clk     : in  STD_LOGIC;
              entrada : in  STD_LOGIC;
              saida   : out STD_LOGIC);
end entity;

architecture bordaSubida of edgeDetector is
    signal saidaQ : STD_LOGIC;
begin
  process(clk)
  begin
        if rising_edge(clk) then
            saidaQ <= entrada;
        end if;
  end process;
  saida <= entrada and (not saidaQ);
end  architecture bordaSubida;


architecture bordaDescida of edgeDetector is
    signal saidaQ : STD_LOGIC;
begin
  process(clk)
  begin
        if rising_edge(clk) then
            saidaQ <= entrada;
        end if;
  end process;
  saida <= (not entrada) and saidaQ;
end  architecture bordaDescida;
```

#### Exemplo de uso

```vhdl

detectorSub0: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(0)), saida => auxReset);
detectorSub1: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(1)), saida => auxBt1);
detectorSub2: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(2)), saida => auxBt2);
detectorSub3: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(3)), saida => auxBt3);
```

***

### Registrador Genérico

A largura dos dados (número de bits) é definida pelo _generic_.

```vhdl

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity registradorGenerico is
    generic (
        larguraDados : natural := 8
    );
    port (DIN : in std_logic_vector(larguraDados-1 downto 0);
       DOUT : out std_logic_vector(larguraDados-1 downto 0);
       ENABLE : in std_logic;
       CLK,RST : in std_logic
        );
end entity;

architecture comportamento of registradorGenerico is
begin
    -- In Altera devices, register signals have a set priority.
    -- The HDL design should reflect this priority.
    process(RST, CLK)
    begin
        -- The asynchronous reset signal has the highest priority
        if (RST = '1') then
            DOUT <= (others => '0');    -- Código reconfigurável.
        else
            -- At a clock edge, if asynchronous signals have not taken priority,
            -- respond to the appropriate synchronous signal.
            -- Check for synchronous reset, then synchronous load.
            -- If none of these takes precedence, update the register output
            -- to be the register input.
            if (rising_edge(CLK)) then
                if (ENABLE = '1') then
                        DOUT <= DIN;
                end if;
            end if;
        end if;
    end process;
end architecture;

```

***

### Base de tempo

Para obter a referência de tempo para o relógio, é necessário dividir o _clock_ de entrada por um valor X (inteiro) e obter a _saida_clk_.

Para tanto, pode-se utilizar o código do divisorGenerico, mostrado abaixo.

Em seguida ao código do divisor, temos um [exemplo de uso (instanciação)](#topLevel).

Para evitar problemas com o sincronismo desse _saida_clk_ gerado, deve-se tomar cuidado com a sincronização.

O resultado do divisor pode ser usado para habilitar um _flip-flop_ que **executará uma divisão por dois sincronizada** com o _clock_, como mostrado abaixo.

Em resumo, para obter uma base de tempo de um segundo:

    -   Faça a divisão do clock de entrada (CLOCK_50 do kit de desenvolvimento):

        -   Usando um contador até 25.000.000;

        -   E use a saída do contador para ativar um flip-flop que divide por 2;

        -   Assim, será obtido um sinal de 1 Hz, 50% de ciclo ativo e sincronizado com o clock do circuito.

-   O sinal **clk** do desenho deve ser conectado ao **CLOCK_50** da placa de FPGA.

![](../imagensVHDL/clockDomainSynchronizedPCFS.svg)

***

#### Exemplo de código para o divisor

Abaixo temos o código para um divisor que opera de três formas distintas:

-   Dividindo por 2;

-   Dividindo por 2^(n+1);

-   Dividindo por um inteiro 2n.

Onde "n" é o valor definido no _generic map_.

**Note que esse exemplo já possui uma divisão por 2 no fim da contagem, ou seja, ele deverá ser adaptado para funcionar como o desenho acima.**

Em seguida ao código do divisor, temos um [exemplo de uso (instanciação)](#topLevel).


**Nome do arquivo: divisorGenerico.vhd**

```vhdl

   LIBRARY ieee;
   USE ieee.std_logic_1164.ALL;
   use ieee.numeric_std.all;

   entity divisorGenerico is
    generic
    (divisor : natural := 8);
       port(
           clk      :   in std_logic;
           saida_clk :   out std_logic
           );
   end entity;

   -- Nao usa o valor do divisor. So divide por 2.

   architecture divPor2 of divisorGenerico is
       signal tick : std_logic;
   begin
       process(clk)
       begin
           if rising_edge(clk) then
               tick <= not tick;
           end if;
       end process;
       saida_clk <= tick;
   end architecture divPor2;

   -- O valor "n" do divisor, define a divisao por 2^(n+1).
   -- Ou seja, 2^n é metade do período da frequência de saída.

   architecture divPotenciaDe2 of divisorGenerico is
        signal contador : std_logic_vector(divisor downto 0);
   begin
        process(clk)
        begin
            if rising_edge(clk) then
                contador <= std_logic_vector(unsigned(contador) + 1);
            end if;
        end process;
    saida_clk <= contador(divisor);
   end architecture divPotenciaDe2;

   -- O valor "n" do divisor, define a divisao por "2n".
   -- Ou seja, n é metade do período da frequência de saída.

   architecture divInteiro of divisorGenerico is
        signal tick : std_logic := '0';
        signal contador : integer range 0 to divisor+1 := 0;
   begin
        process(clk)
        begin
            if rising_edge(clk) then
                if contador = divisor then
                    contador <= 0;
                    tick <= not tick;
                else
                    contador <= contador + 1;
                end if;
            end if;
        end process;
    saida_clk <= tick;
    end architecture divInteiro;

```

***

<a name="topLevel"></a>

#### Exemplo de uso do divisor

**Nome do arquivo: top_level.vhd**

```vhdl
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;

entity top_level is
   port(
      clk        :   in std_logic;
      saida_clk :   out std_logic
   );
end entity;

architecture teste of top_level is

begin
fazDivisaoPot2: entity work.divisorGenerico(divPotenciaDe2)
            generic map (divisor => 5)   -- divide por 2^6.
            port map (clk => clk, saida_clk => saida_clk);

fazDivisaoInteiro: entity work.divisorGenerico(divInteiro)
            generic map (divisor => 5)   -- divide por 10.
            port map (clk => clk, saida_clk => saida_clk);

end architecture;

```

***

### Registrador de Deslocamento Genérico

```vhdl

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity registradorDeslocamento is
    generic ( estagios : natural := 8 );
    port (
        clk     : in std_logic;
        enable  : in std_logic;
        rst    : in std_logic;
        sr_out  : out std_logic_vector((estagios-1) downto 0)
    );
end entity;

architecture rtl of registradorDeslocamento is
    signal sr : std_logic_vector ((estagios-1) downto 0);
begin
    process (clk, rst)
    variable ZERO : std_logic_vector ((estagios-1) downto 0);
    begin
        ZERO := (others => '0');
        if (rst = '1') then
                sr <= (others => '0');
        elsif (rising_edge(clk)) then
            if (enable = '1') then
                if (sr = ZERO) then
                    sr(0) <= '1';
                else
                    sr <= std_logic_vector(unsigned(sr) rol 1);
                end if;
            end if;
        end if;
    end process;
    sr_out <= sr;
end architecture;

```

***

## Memórias

As memórias podem ser:

-   Somente Leitura (ROM);

-   Leitura e Escrita (RAM);

-   Síncronas:

    -   Só alteram o conteúdo armazenado na transição do _clock_;

    -   Só alteram o conteúdo sendo lido (exibido) a partir da transição do _clock_.

-   Assíncronas:

    -   A partir do aparecimento de um novo endereço, elas exibem o conteúdo da posição de memória após o tempo de propagação.

    -   A alteração do conteúdo é controlada pelo sinal de escrita (WR).

Uma característica do VHDL é o endereçamento de memória ser feito com um tipo inteiro.

Porém, para a simulação se beneficiar dos recursos multinível do tipo _std\_logic(\_vector)_ precisamos que a interface dos componentes usem esse tipo de dados.

No caso das memórias, deve-se converter o valor do endereço de _std_logic_vector_ para inteiro, conforme mostrado abaixo:

```vhdl
memoria(to_integer(unsigned(endereco))) <= dado;

dado <= memoria(to_integer(unsigned(endereco)));

```

### Banco de Registradores MIPS

Possuem a escrita síncrona e a leitura assíncrona.

Ver mais detalhes na descrição do processador.

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- Baseado no apendice C (Register Files) do COD (Patterson & Hennessy).

entity bancoRegistradores is
    generic
    (
        larguraDados        : natural := 32;
        larguraEndBancoRegs : natural := 5   --Resulta em 2^5=32 posicoes
    );
-- Leitura de 2 registradores e escrita em 1 registrador simultaneamente.
    port
    (
        clk        : in std_logic;
--
        enderecoA       : in std_logic_vector((larguraEndBancoRegs-1) downto 0);
        enderecoB       : in std_logic_vector((larguraEndBancoRegs-1) downto 0);
        enderecoC       : in std_logic_vector((larguraEndBancoRegs-1) downto 0);
--
        dadoEscritaC    : in std_logic_vector((larguraDados-1) downto 0);
--
        escreveC        : in std_logic := '0';
        saidaA          : out std_logic_vector((larguraDados -1) downto 0);
        saidaB          : out std_logic_vector((larguraDados -1) downto 0)
    );
end entity;

architecture comportamento of bancoRegistradores is

    subtype palavra_t is std_logic_vector((larguraDados-1) downto 0);
    type memoria_t is array(2**larguraEndBancoRegs-1 downto 0) of palavra_t;

    -- Declaracao dos registradores:
    shared variable registrador : memoria_t;

begin
    process(clk) is
    begin
        if (rising_edge(clk)) then
            if (escreveC = '1') then
                registrador(to_integer(unsigned(enderecoC))) := dadoEscritaC;
            end if;
        end if;
    end process;

    -- IF endereco = 0 : retorna ZERO
     process(all) is
     begin
         if (unsigned(enderecoA) = 0) then
            saidaA <= (others => '0');
         else
            saidaA <= registrador(to_integer(unsigned(enderecoA)));
         end if;
         if (unsigned(enderecoB) = 0) then
            saidaB <= (others => '0');
         else
            saidaB <= registrador(to_integer(unsigned(enderecoB)));
        end if;
     end process;
end architecture;

```

***

### ROM

O seu conteúdo deve ter sido previamente gravado no dispositivo.

Possuem a leitura assíncrona.

### ROM Assíncrona com a Inicialização em VHDL

A função initMemory carrega os dados na ROM da FPGA.

```vhdl

library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;

entity memoria is
   generic (
          dataWidth: natural := 8;
          addrWidth: natural := 3
    );
   port (
          Endereco : in std_logic_vector (addrWidth-1 DOWNTO 0);
          Dado : out std_logic_vector (dataWidth-1 DOWNTO 0)
    );
end entity;

architecture assincrona of memoria is

  type blocoMemoria is array(0 TO 2**addrWidth - 1) of std_logic_vector(dataWidth-1 DOWNTO 0);

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

### ROM Assíncrona com a Inicialização a partir de um Arquivo _".mif"_:

A definição do tipo de dados da memória lê um arquivo definido com os dados e os carrega na ROM da FPGA.

```vhd

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity romMif is

    generic
    (
        dataWidth : natural := 8;
        addrWidth : natural := 8
    );

    port (
          Endereco : in std_logic_vector (addrWidth-1 DOWNTO 0);
          Dado : out std_logic_vector (dataWidth-1 DOWNTO 0)
    );
end entity;

architecture initFileROM of romMif is

type memory_t is array (2**addrWidth -1 downto 0) of std_logic_vector (dataWidth-1 downto 0);
signal content: memory_t;
attribute ram_init_file : string;
attribute ram_init_file of content:
signal is "initROM.mif";

begin
   Dado <= content(to_integer(unsigned(Endereco)));
end architecture;

```

#### Formato do arquivo initROM.mif:

```vhd

-- Copyright (C) 2017  Intel Corporation. All rights reserved.
-- Your use of Intel Corporation's design tools, logic functions
-- and other software and tools, and its AMPP partner logic
-- functions, and any output files from any of the foregoing
-- (including device programming or simulation files), and any
-- associated documentation or information are expressly subject
-- to the terms and conditions of the Intel Program License
-- Subscription Agreement, the Intel Quartus Prime License Agreement,
-- the Intel FPGA IP License Agreement, or other applicable license
-- agreement, including, without limitation, that your use is for
-- the sole purpose of programming logic devices manufactured by
-- Intel and sold by Intel or its authorized distributors.  Please
-- refer to the applicable agreement for further details.

WIDTH=8;
DEPTH=256;
ADDRESS_RADIX=DEC;
DATA_RADIX=HEX;

CONTENT BEGIN
--endereco : dado;
    0    :   44;
    1    :   41;
    2    :   4C;
    3    :   2F;
    [4..5] : 20;
    6    :   22;
    [7..8] : 00;
    9    :   01;
    10   :   6A;
    11   :   AB;
    12   :   1B;
    13   :   AC;
    14   :   09;
    15   :   00;
    16   :   AF;
    17   :   00;
    18   :   AE;
    19   :   11;
    20   :   01;
    [21..23] : 00;
    24   :   AE;
    25   :   14;
    [26..28] : 00;
    29   :   8D;
    30   :   0C;
    [31..33] : 00;
    34   :   AE;
    [35..37] : 00;
    38   :   26;
    [39..255] : 20;
END;

```

***

### Single Port RAM com Leitura Assíncrona

A escrita é síncrona e a leitura assíncrona. Ou seja, se o endereço para a leitura mudar durante qualquer parte do período de _clock_, a saída mudará após o tempo de propagação - independendo da borda do _clock_.

Modelo retirado dos _templates_ do Quartus e modificado para ter o endereço do tipo _std_logic_vector_ e leitura assíncrona.

```vhdl

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity single_port_ram is
   generic (
         dataWidth: natural := 8;
         addrWidth: natural := 8
    );
    port
    (
        addr     : in std_logic_vector(addrWidth-1 downto 0);
        we       : in std_logic := '1';
        clk      : in std_logic;
        dado_in  : in std_logic_vector(dataWidth-1 downto 0);
        dado_out : out std_logic_vector(dataWidth-1 downto 0)
    );
end entity;

architecture rtl of single_port_ram is
    -- Build a 2-D array type for the RAM
    subtype word_t is std_logic_vector(dataWidth-1 downto 0);
    type memory_t is array((2**addrWidth-1) downto 0) of word_t;

    -- Declare the RAM signal.
    signal ram : memory_t;
begin
    process(clk)
    begin
        if(rising_edge(clk)) then
            if(we = '1') then
                ram(to_integer(unsigned(addr))) <= dado_in;
            end if;
        end if;
    end process;
    dado_out <= ram(to_integer(unsigned(addr)));
end architecture;

```

***

### Single Port RAM com Leitura e Escrita Síncronos

A escrita e leitura são síncronas.

Modelo retirado dos _templates_ do Quartus e modificado para ter o endereço do tipo _std_logic_vector_.

```vhdl

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity single_port_ram is
   generic (
         dataWidth: natural := 8;
         addrWidth: natural := 8
    );
    port
    (
        addr     : in std_logic_vector(addrWidth-1 downto 0);
        we       : in std_logic := '1';
        clk      : in std_logic;
        dado_in  : in std_logic_vector(dataWidth-1 downto 0);
        dado_out : out std_logic_vector(dataWidth-1 downto 0)
    );
end entity;

architecture rtl of single_port_ram is
    -- Build a 2-D array type for the RAM
    subtype word_t is std_logic_vector(dataWidth-1 downto 0);
    type memory_t is array((2**addrWidth-1) downto 0) of word_t;

    -- Declare the RAM signal.
    signal ram : memory_t;

    -- Register to hold the address during one clock cycle.
    signal addr_reg : std_logic_vector(addrWidth-1 downto 0);

begin
    process(clk)
    begin
        if(rising_edge(clk)) then
            if(we = '1') then
                ram(to_integer(unsigned(addr))) <= dado_in;
            end if;
            -- Register the address for reading during one clock cycle.
            addr_reg <= addr;
        end if;
    end process;
    dado_out <= ram(to_integer(unsigned(addr_reg)));
end architecture;

```

***

***

## Biblioteca

### Biblioteca de Componentes

Este arquivo é <i>somente um exemplo</i>, antes de usar faça os ajustes necessários para a sua implementação.

```vhdl

library IEEE;
use IEEE.STD_LOGIC_1164.all;
use ieee.numeric_std.all;

package bibliotecaComponentes is


    component conversorHex7Seg is
        port
        (
            -- Input ports
            dadoHex : in  std_logic_vector(3 downto 0);
            apaga   : in  std_logic;
            negativo : in  std_logic;
            overFlow : in  std_logic;
            -- Output ports
            saida7seg : out std_logic_vector(6 downto 0)
        );
    end component conversorHex7Seg;

-----------------------------------------------------------------------------------

    component bancoRegistradores is
        generic
        (
            larguraDados        : natural := 8;
            larguraEndBancoRegs : natural := 5
        );
    -- Leitura de 2 registradores e escrita em 1 registrador simultaneamente.
        port
        (
            clk        : in std_logic;
    --
            enderecoA       : in std_logic_vector((larguraEndBancoRegs-1) downto 0);
            enderecoB       : in std_logic_vector((larguraEndBancoRegs-1) downto 0);
            enderecoC       : in std_logic_vector((larguraEndBancoRegs-1) downto 0);
    --
            dadoEscritaC    : in std_logic_vector((larguraDados-1) downto 0);
    --
            escreveC          : in std_logic;
            saidaA          : out std_logic_vector((larguraDados -1) downto 0);
            saidaB          : out std_logic_vector((larguraDados -1) downto 0)
        );
    end component bancoRegistradores;

-----------------------------------------------------------------------------------

    component divisorGenerico is
        generic
        (divisor : natural := 8);
        port(
            clk         :   in std_logic;
            saida_clk :   out std_logic
            );
    end component divisorGenerico;

-----------------------------------------------------------------------------------

    component edgeDetector is
         Port ( clk     : in  std_logic;
                  entrada : in  std_logic;
                  saida   : out std_logic);
    end component edgeDetector;

-----------------------------------------------------------------------------------

    component estendeSinalGenerico is
        generic
        (
            larguraDadoEntrada : natural  :=    8;
            larguraDadoSaida   : natural  :=    8
        );
        port
        (
            -- Input ports
            estendeSinal_IN : in  std_logic_vector(larguraDadoEntrada-1 downto 0);
            -- Output ports
            estendeSinal_OUT: out std_logic_vector(larguraDadoSaida-1 downto 0)
        );
    end component estendeSinalGenerico;

-----------------------------------------------------------------------------------

    component muxGenerico2 is
        generic (
            -- Total de bits das entradas e saidas
            larguraDados    : natural  :=   8
        );
        port (
    --      -- Input ports
            entradaA_MUX    : in  std_logic_vector(larguraDados-1 downto 0);
            entradaB_MUX    : in  std_logic_vector(larguraDados-1 downto 0);
            seletorMUX  : in  std_logic;
    --
    --      -- Output ports
            saidaMUX   : out std_logic_vector(larguraDados-1 downto 0)
        );
    end component muxGenerico2;

-----------------------------------------------------------------------------------

    component registradorGenerico is
    generic (
        larguraDados : natural := 8
    );
    port (DIN : in std_logic_vector(larguraDados-1 downto 0);
           DOUT : out std_logic_vector(larguraDados-1 downto 0);
           ENABLE : in std_logic;
           CLK,RST : in std_logic);
    end component registradorGenerico;

-----------------------------------------------------------------------------------

    component somaConstanteGenerico is
         generic (
              larguraDados : natural := 32;
              incremento : natural := 4
         );
         port (
              entrada: in  STD_LOGIC_VECTOR((larguraDados-1) downto 0);
              saida:   out STD_LOGIC_VECTOR((larguraDados-1) downto 0)
         );
         end component somaConstanteGenerico;

-----------------------------------------------------------------------------------

     component somadorGenerico is
            generic ( larguraDados : natural := 32 );
        port (
            entradaA, entradaB: in STD_LOGIC_VECTOR((larguraDados-1) downto 0);
            saida:  out STD_LOGIC_VECTOR((larguraDados-1) downto 0) );
     end component somadorGenerico;

-----------------------------------------------------------------------------------

    component deslocadorGenerico is
    generic (
        larguraDadoEntrada : natural  :=    8;
        larguraDadoSaida   : natural  :=    8;
        deslocamento : natural := 2  );
    port (
        -- Input ports
        sinalIN : in  std_logic_vector(larguraDadoEntrada-1 downto 0);
        -- Output ports
        sinalOUT: out std_logic_vector(larguraDadoSaida-1 downto 0) );
     end component deslocadorGenerico;

end package bibliotecaComponentes;

```

***

### Biblioteca de Constantes

Este arquivo é <i>somente um exemplo</i>, antes de usar faça os ajustes necessários para a sua implementação.

```vhdl

library IEEE;
use IEEE.STD_LOGIC_1164.all;
use ieee.numeric_std.all;

package constantesMIPS is

--  Exemplos:
--  signal Instruction : Bit_Vector(15 downto 0);
--  alias OpCode : Bit_Vector(3 downto 0) is Instruction(15 downto 12);
--  subtype TypeWord is unsigned( 31 downto 0 );
--  type    TypeArrayWord is array (natural range <>) of unsigned( 31 downto 0 );
--  constant FUNCT_WIDTH : natural := 6;

    constant FUNCT_WIDTH    : natural := 6;
    constant OPCODE_WIDTH   : natural := 6;
    constant DATA_WIDTH     : natural := 32;
    constant ADDR_WIDTH     : natural := 32;
    constant REGBANK_ADDR_WIDTH : natural := 5;
    constant ALU_OP_WIDTH   : natural := 2;
    constant CTRL_ALU_WIDTH : natural := 3;
    constant CONTROLWORD_WIDTH : natural := 10;

-- codigos das instrucoes do DLX:
    subtype opCode_t       is std_logic_vector(OPCODE_WIDTH-1 downto 0);
    subtype funct_t        is std_logic_vector(FUNCT_WIDTH-1 downto 0);
    subtype ctrlWorld_t    is std_logic_vector(CONTROLWORD_WIDTH-1 downto 0);
    subtype aluOp_t        is std_logic_vector(ALU_OP_WIDTH-1 downto 0);
    subtype ctrlALU_t      is std_logic_vector(CTRL_ALU_WIDTH-1 downto 0);

    subtype dado_t         is std_logic_vector(DATA_WIDTH-1 downto 0);
    subtype addr_t         is std_logic_vector(ADDR_WIDTH-1 downto 0);
--
    constant functADD   : funct_t := "100000";
    constant functSUB   : funct_t := "100010";
    constant functAND   : funct_t := "100100";
    constant functOR    : funct_t := "100101";
    constant functSLT   : funct_t := "101010";

    constant opCodeTipoR  : opCode_t := "000000";
--
    constant opCodeLW     : opCode_t := "100011";
    constant opCodeSW     : opCode_t := "101011";
    constant opCodeBEQ    : opCode_t := "000100";
--
    constant opCodeTipoJ  : opCode_t := "000010";

--
-- Codigos da palavra de controle:
--  alias memWRsignal: std_logic is controlWord(0);
--  alias memRDsignal: std_logic is controlWord(1);
--  alias beqSignal:   std_logic is controlWord(2);
--  alias muxUlaMem:   std_logic is controlWord(3);
--  alias ulaOPvalue:  std_logic_vector(1 downto 0) is controlWord(5 downto 4);
--  alias muxRtImed:   std_logic is controlWord(6);
--  alias regcWRsignal:std_logic is controlWord(7);
--  alias muxRtRd:     std_logic is controlWord(8);
--  alias muxPcBeqJ:   std_logic is controlWord(9);
--
-- ControlWorld Bit:    9   8       7           6     5,4    3     2      1       0
--Instrução  Opcode    Mux1 Mux2 HabEscritaReg Mux3  ULAOp  Mux4  BEQ HabLeMEM HabEscME
--Tipo R    |00.0000  | 0 |  1 |     1        |  0  |  10  |  0  | 0 |    0   |    0    |
--LW        |10.0011  | 0 |  0 |     1        |  1  |  00  |  1  | 0 |    1   |    0    |
--SW        |10.1011  | 0 |  0 |     0        |  1  |  00  |  0  | 0 |    0   |    1    |
--BEQ       |00.0100  | 0 |  0 |     0        |  0  |  01  |  0  | 1 |    0   |    0    |
--J         |00.0010  | 1 |  X |     0        |  X  |  XX  |  X  | X |    0   |    0    |

--  Mux1: mux([PC+4, BEQ]/J);  Mux2: mux(Rt/Rd); Mux3: mux(Rt/imediato);  Mux4: mux(ULA/mem).

    constant ctrlTipoR:       ctrlWorld_t := "0110100000";
    constant ctrlTipoJ:       ctrlWorld_t := "1X0XXXXX00";
    constant ctrlTipoLW:      ctrlWorld_t := "0011001010";
    constant ctrlTipoSW:      ctrlWorld_t := "0001000001";
    constant ctrlTipoBEQ:     ctrlWorld_t := "0000010100";
    constant ctrlZERO:        ctrlWorld_t := "0000000000";

--  -- ULA ---
    subtype operacaoULA_t is std_logic_vector(2 downto 0);

    constant execAndULA : operacaoULA_t := "000";
    constant execOrULA  : operacaoULA_t := "001";
    constant execAddULA : operacaoULA_t := "010";
    constant execSubULA : operacaoULA_t := "110";
    constant execSltULA : operacaoULA_t := "111";
end package constantesMIPS;

```

***

<br>

***

***

<!-- FIM -->

<!---

## Inicialização de ROM com interface usando endereçamento _integer_ e leitura síncrona.

```vhdl
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
---->
