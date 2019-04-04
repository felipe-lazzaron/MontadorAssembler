<a name="inicio"></a>

## Código VHDL para o circuito do relógio.

## Código do Divisor:

Para obter a referência de tempo para o relógio, é necessário dividir o clock de entrada por um valor X (inteiro).

Para tanto, pode-se utilizar o código do divisorGenerico, mostrado abaixo. Em seguida temos um [exemplo de uso (instanciação)](#topLevel).

Nome do arquivo: divisorGenerico.vhd

```vhd
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;

entity divisorGenerico is
	generic
	(divisor : natural := 8);
    port(
        clk 		:   in std_logic;
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
end divPor2;

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
end divPotenciaDe2;


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
end divInteiro;
```

***

<a name="topLevel"></a>
## Exemplo de uso:

```vhd
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;

entity top_level is
   port(
      clk 		 :   in std_logic;
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

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).
