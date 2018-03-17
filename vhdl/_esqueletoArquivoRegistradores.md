

```vhdl

library ieee;
use ieee.std_logic_1164.all;

entity arqReg is
  port(
        clk, habEscrita                       : in  std_logic;
        endereco1, endereco2, enderecoEscrita : in  std_logic_vector(2 downto 0);
        dadoEscrever                          : in  std_logic_vector(7 downto 0);
        dadoLido1, dadoLido2                  : out std_logic_vector(7 downto 0)
  );
end entity;

architecture comportamento of arqReg is
-- declarações de sinais.

begin
-- código.


end architecture;
```
