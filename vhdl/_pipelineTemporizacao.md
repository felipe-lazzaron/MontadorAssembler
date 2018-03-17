**Pipeline:**

```vhd

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity pipelineCircuit is

  generic (
    MAX_BIT : natural := 8
  );

  port (
    DIN : in std_logic_vector(MAX_BIT-1 downto 0);
    DOUT : out std_logic_vector(MAX_BIT-1 downto 0);
    OUTR1 : out std_logic_vector(MAX_BIT-1 downto 0);
    OUTR2 : out std_logic_vector(MAX_BIT-1 downto 0);
    ENABLE : in std_logic := '1';
    RST : in std_logic  := '0';
    CLK : in std_logic
  );

end entity;

architecture comportamento of pipelineCircuit is

    -- Declarations (optional)
    signal DOUT_R1 : std_logic_vector(MAX_BIT-1 downto 0);
    signal DOUT_R2 : std_logic_vector(MAX_BIT-1 downto 0);
    signal DIN_R2  : std_logic_vector(MAX_BIT-1 downto 0);
    signal DIN_R3  : std_logic_vector(MAX_BIT-1 downto 0);

begin

	   -- Component Instantiation Statement (optional)
    -- O mapa de portas precisa ser na mesma posicao (ordem) da definicao da entidade no arquivo dela.
    registradorR1 : entity work.registrador port map (DIN, DOUT_R1, ENABLE, CLK, RST);
    registradorR2 : entity work.registrador port map (DIN_R2, DOUT_R2, ENABLE, CLK, RST);
    registradorR3 : entity work.registrador port map (DIN_R3, DOUT, ENABLE, CLK, RST);

    OUTR2  <= DOUT_R2;
    OUTR1  <= DOUT_R1;

    DIN_R2 <= (DOUT_R1(7 downto 6) & (DOUT_R1(5) AND DOUT_R1(4)) & DOUT_R1(4 downto 0));
    DIN_R3 <= (DOUT_R2(7 downto 1) & (DOUT_R2(1) OR DOUT_R2(0)) );

end architecture;

```
