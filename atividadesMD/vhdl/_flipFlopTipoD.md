# Flip flop tipo D

Observe a influência da posição da atribuição da saída Qbarra.

A primeira forma, implementa dois _flip-flops_. Já a segunda forma, implementa um _flip-flop_.

<br>

## Código VHDL que Implementa **Dois** _Flip-Flops_

```vhdl
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
            Qbarra <= NOT(dado);       -- A atribuição do Qbarra dentro do processo força a implementação de outro flip-flop
        end if;
    end process;

end comportamento;
```
### Esquema RTL do Flip-Flop do código acima

<img src="../imagensQuartus/flipFlopRTL.png" alt="Esquema RTL do Flip-Flop tipo D" style="width:600px;"/>

***

## Código VHDL que Implementa **Um** _Flip-Flop_

```vhdl
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
        end if;
    end process;
    Qbarra <= NOT(Q);                  -- A atribuição do Qbarra fora do processo impede a implementação de outro flip-flop

end comportamento;

```
### Esquema RTL do Flip-Flop do código acima

<img src="../imagensQuartus/flipFlopRTL2.png" alt="Esquema RTL do Flip-Flop tipo D" style="width:600px;"/>


***


<br>

***

***

<!-- FIM -->
