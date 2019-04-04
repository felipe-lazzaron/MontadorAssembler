# ROM com a inicialização a partir de um arquivo ".mif"

Note que o tipo de dados dos endereços é _natural_ e o ideal é utilizar _std_logic_vector_.

Faça as alterações necessárias antes de usar.

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

architecture initFileROM of romMif is

type memory_t is array (2**ADDR_WIDTH-1 downto 0) of std_logic_vector (DATA_WIDTH-1 downto 0);
signal content: memory_t;
attribute ram_init_file : string;
attribute ram_init_file of content:
signal is "initROM.mif";

begin
    process(clk)
    begin
        if (RISING_EDGE(clk)) then
            q <= content(addr);
        end if;
    end process;
end architecture;
```

## Formato do arquivo initROM.mif

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

<br>

***

***

<!-- FIM -->
