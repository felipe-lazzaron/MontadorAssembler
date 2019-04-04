# Pipeline

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity pipelineCircuit is
    generic (
        MAX_BIT : natural := 8
    );
    port (DIN : in std_logic_vector(MAX_BIT-1 downto 0);
          DOUT : out std_logic_vector(MAX_BIT-1 downto 0);
          ENABLE : in std_logic := '1';
          CLK,RST : in std_logic);
end entity;


architecture comportamento of pipelineCircuit is

  -- Declare os sinais (fios) que irá utilizar, por exemplo:
  signal DOUT_REG1 : std_logic_vector(MAX_BIT-1 downto 0);
  signal DIN_REG2 : std_logic_vector(MAX_BIT-1 downto 0);

begin

  -- Instanciação por posição:
        -- O mapa de portas precisa ser na mesma ordem da definição da entidade no arquivo dela (esta não é a solução da atividade, somente um exemplo de outro circuito).
    R1 : entity work.registrador port map (DIN, DOUT_REG1, ENABLE, CLK, RST);

        -- Ou utilizar o mapeamento completo (esta não é a solução da atividade, somente um exemplo de outro circuito).
        -- O VHDL permite, no port map, a concatenação de sinais e/ou a utilização de equações lógicas.
        -- Por exemplo:
    R2 : entity work.registrador port map (DIN => DIN, DOUT_REG1 (3 downto 0) & DOUT_REG1 (7 downto 4) => DIN_REG2, ENABLE => ENABLE, CLK => CLK, RESET => RST);

  -- Adicione aqui a lógica necessária:


end architecture;
```


***

<br>

***

***

<!-- FIM -->
