### Flip flop tipo D:

```vhd
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity flip_flop is
port
(
    -- Input ports
    dado: in STD_LOGIC;
    clock: in STD_LOGIC; -- := <default_value>;
    -- Output ports
    Q: out STD_LOGIC;
    Qbarra : out STD_LOGIC);
end flip_flop;

architecture comportamento of flip_flop is
-- Declarations (optional)
begin
    -- Update the variable only when updates are enabled
    process(clock)
    begin
        if (rising_edge(clock)) then
            Q <= dado;
            Qbarra <= NOT(dado);
        end if;
    end process;
end comportamento;
```
### Esquema RTL do Flip-Flop do código acima.

![Esquema RTL do Flip-Flop tipo D](../imagensQuartus/flipFlopRTL.png)
