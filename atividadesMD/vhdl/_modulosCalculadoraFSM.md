<a name="inicio"></a>

# Código VHDL para o circuito da calculadora

O circuito é composto pelos arquivos:

-   O top level;

-   O fluxo de dados;

-   A ULA;

-   O decodificador de hexadecimal para sete segmentos;

-   O registrador genérico;

-   O divisor genérico.

E a máquina de estados (SM1.vhd), que será criada para controlar o funcionamento do circuito.

## Código do Top Level

Nome do arquivo: calculadora.vhd.

```vhdl
library IEEE;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity calculadora is
  port (
    -- Entradas (placa)
    CLOCK_50 : in STD_LOGIC;
    KEY: in STD_LOGIC_VECTOR(3 DOWNTO 0);
    SW: in STD_LOGIC_VECTOR(17 DOWNTO 0);

    -- Saidas (placa)
    LEDR  : out STD_LOGIC_VECTOR(17 DOWNTO 0) := (others => '0');
    LEDG  : out STD_LOGIC_VECTOR(8 DOWNTO 0) := (others => '0');
    HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, HEX6, HEX7 : OUT STD_LOGIC_VECTOR(6 downto 0)
  );
end entity;


architecture comportamento of calculadora is
  signal auxSaida : std_logic_vector(7 downto 0);
  signal loNibble : std_logic_vector(3 downto 0);
  signal hiNibble : std_logic_vector(7 downto 4);
  signal auxFuncaoULA : std_logic_vector(1 downto 0);
  signal auxOverFlow : std_logic := '0';
  signal auxApaga : std_logic := '1';
  signal auxNegativo : std_logic := '0';
  signal auxCarregaA : std_logic := '0';
  signal auxCarregaB : std_logic := '0';
  signal auxCarregaSaida : std_logic := '0';
  signal auxReset : std_logic := '0';
  signal auxClock : std_logic := '0';
  signal pisca : std_logic := '0';
  signal auxLeituraA : std_logic := '0';
  signal auxLeituraB : std_logic := '0';
  signal ativaPisca : std_logic := '0';
  signal controle : std_logic_vector(15 downto 0);
  --
  signal auxPasso : std_logic_vector(3 downto 0);
  signal auxReiniciaFSM : std_logic := '0';
begin

  -- Instancia o fluxo de dados mais simples:
  FD : entity work.fluxoDados (simples) --(complexo)
    Port map (
      entrada(7 downto 0) => hiNibble & loNibble, funcaoULA => auxFuncaoULA,
       clk => auxClock, rst => auxReset, overflow => auxOverFlow,
      carregaA => auxCarregaA, carregaB => auxCarregaB,
      carregaSaida => auxCarregaSaida, saida => auxSaida
    );

  -- Displays e Leds:
  freqPisca : entity work.divisorGenerico (divisaoGenerica)  generic map (divisor => 25) --(divisaoGenerica) := 2^divisor
    port map (clk =>  auxClock, saida_clk => pisca);

  -- Resultado da operacao executada:
  display0 : entity work.conversorHex7seg
    Port map (saida7seg => HEX0, dadoHex => auxSaida(3 downto 0), apaga => auxOverFlow);
  display1 : entity work.conversorHex7seg
    Port map (saida7seg => HEX1, dadoHex => auxSaida(7 downto 4), apaga => auxOverFlow);

  -- Indicador de sinal e overflow:
  display2 : entity work.conversorHex7seg
    Port map (saida7seg => HEX2, dadoHex => (others => '1'), apaga => (not(auxNegativo) or auxOverFlow), negativo => auxNegativo);
  display3 : entity work.conversorHex7seg
    Port map (saida7seg => HEX3, dadoHex => (others => '1'), apaga => not(auxOverFlow), overFlow => auxOverFlow);

  -- Mostra os valores sendo escolhidos nas chaves:
  display4 : entity work.conversorHex7seg
    Port map (saida7seg => HEX4, dadoHex => loNibble);
  display5 : entity work.conversorHex7seg
    Port map (saida7seg => HEX5, dadoHex => hiNibble);

  --Indica a operacao escolhida:
  --  0 = Soma
  --  1 = Subtrai
  --  2 = XOR
  --  3 = AND
  display6 : entity work.conversorHex7seg
    Port map (saida7seg => HEX6, dadoHex => '0' & '0' & auxFuncaoULA);

  -- Indica o estado atual da maquina de estado, em decimal:
  display7 : entity work.conversorHex7seg
    Port map (saida7seg => HEX7, dadoHex => auxPasso, apaga => '0', overFlow => '0', negativo => '0');

  -- Instacia a maquina de estados:
  sequenciador : entity work.SM1
    port map( reset => auxReset, clock => auxClock,
    leituraA => auxLeituraA, leituraB => auxLeituraB,
    controle => controle, passo => auxPasso,
    auxReset => auxReset, reiniciaFSM => auxReiniciaFSM);

  -- conexoes da placa:
  -- Os 8 primeiros LEDS VERMELHOS indicam o valor definido nas chaves.
  LEDR(7 downto 0) <= SW(7 downto 0);

  LEDR(17 downto 16) <= auxFuncaoULA;            -- indica a funçao da ULA nos dois ultimos LEDS VERMELHOS.
   LEDG(3 downto 0) <= not(KEY(3 downto 0));      -- Cada LED VERDE, de 0 a 3, indica se o botao correspondente foi pressionado.
  LEDG(7 downto 4) <= ( others => auxOverFlow);  -- Todos LEDs VERDEs, de 4 a 7, indicam se ocorreu OVERFLOW.
  LEDG(8) <= pisca and ativaPisca;               -- O LED VERDE entre os displays pisca no ESTADO 1.
  --
  auxFuncaoULA <= SW(17 downto 16);
--  00 = Soma
--  01 = Subtrai
--  10 = XOR
--  11 = AND

  loNibble <= SW(3 downto 0);
  hiNibble <= SW(7 downto 4);

  -- Indicador de valor negativo na operaçao:
  auxNegativo <=  auxSaida(7);

  -- conexoes do controleenviado para a FSM
  auxLeituraA <= not(KEY(3));
  auxLeituraB <= not(KEY(2));
  auxReiniciaFSM <= not(KEY(1));
  auxReset <= not(KEY(0));
--  Pressionando a tecla 3, carrega o valor definido nas chaves para a entrada A da ULA;
--  Pressionando a tecla 2, carrega o valor definido nas chaves para a entrada B da ULA;
--  Pressionando a tecla 1, reinicia a maquina de estados para o estado 1;
--  Pressionando a tecla 0, faz um hard reset em todos os registradores.

  -- conexoes do controle enviado pela FSM
  ativaPisca  <= controle(0);
  auxCarregaA  <= controle(2);
  auxCarregaB  <= controle(4);
-- Extras, para usar com o fluxo de dados mais complexo.
--      <= controle(5);
--      <= controle(6);
--      <= controle(7);
--      <= controle(8);
--      <= controle(9);
--      <= controle(10);
--      <= controle(11);
--      <= controle(12);
--      <= controle(13);
--      <= controle(14);
  auxCarregaSaida <= controle(15);

--Estado 1: controle(0)  = 1 (valor decimal = 1) = ativaPisca;
--Estado 2: controle(2)  = 1 (valor decimal = 4) = auxCarregaA;
--Estado 3: controle(4)  = 1 (valor decimal = 16) = auxCarregaB;
--Estado 4: controle(15) = 1 (valor decimal = 32768) = auxCarregaSaida;

   auxClock <= CLOCK_50;

end architecture;
```

***

## Código do Fluxo de Dados

Nome do arquivo: fluxoDados.vhd

```vhd
library IEEE;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity fluxoDados is
    Port ( entrada : in std_logic_vector(7 downto 0);
        funcaoULA: in std_logic_vector(1 downto 0);
        clk, rst:  in std_logic;
        carregaA:  in std_logic;
        carregaB:  in std_logic;
        carregaSaida: in std_logic;

        entradaA_ULA: out std_logic_vector(7 downto 0);
        entradaB_ULA: out std_logic_vector(7 downto 0);
        saida : out std_logic_vector(7 downto 0);
        overflow: out std_logic
   );
end entity;

architecture simples of fluxoDados is
  signal ULA_IN_A, ULA_IN_B, ULA_OUT, REG_ULA  : std_logic_vector(7 downto 0);
  signal overflowLocal : std_logic;
begin
    ULA         : entity work.ULA Port map (A => ULA_IN_A, B => ULA_IN_B, C => ULA_OUT, Sel => funcaoULA, overflow => overflowLocal);
    regEntradaA : entity work.registradorGenerico port map (DIN => entrada, DOUT => ULA_IN_A, CLK => clk, RST => rst, ENABLE => carregaA);
    regEntradaB : entity work.registradorGenerico port map (DIN => entrada, DOUT => ULA_IN_B, CLK => clk, RST => rst, ENABLE => carregaB);
    regSaida    : entity work.registradorGenerico generic map (larguraDados => 9) port map (DIN => overflowLocal & ULA_OUT, DOUT(7 downto 0) => saida, DOUT(8) => overflow, CLK => clk, RST => rst, ENABLE => carregaSaida);
    entradaA_ULA <= ULA_IN_A;
    entradaB_ULA <= ULA_IN_B;
end architecture;
```

***

## Código da ULA

Nome do arquivo: ULA.vhd

```vhdl
library IEEE;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ULA is
    Port ( A :  in std_logic_vector(7 downto 0);
           B :  in std_logic_vector(7 downto 0);
        Sel: in std_logic_vector(1 downto 0);
           C : out std_logic_vector(7 downto 0);
        overflow: out std_logic
   );
end entity;

architecture comportamento of ULA is

begin
  process (A, B, Sel) is
    variable tempOF : std_logic_vector(2 downto 0);
    variable C9     : std_logic_vector(8 downto 0);
  begin
    C9 := (others => '0');
    case Sel is
      when "00" => C9 := std_logic_vector(resize(signed(std_logic_vector(signed(A) + signed(B))), C9'length));
      when "01" => C9 := std_logic_vector(resize(signed(std_logic_vector(signed(A) - signed(B))), C9'length));
      when "10" => C9(8 downto 0) := '0' & std_logic_vector(A XOR B);
      when "11" => C9(8 downto 0) := '0' & std_logic_vector(A AND B);
      when others => C9 := (others => '0');
    end case;
    C(7 downto 0) <= C9(7 downto 0);
    case Sel is
      -- overflow = "b001" (entrada POSITIVA e saida NEGATIVA)  OU "b110" (entrada NEGATIVA e saida POSITIVA)
      when "00" => tempOF := A(A'high) & B(B'high) & C9(C9'high-1);
      when "01" => tempOF := A(A'high) & not(B(B'high)) & C9(C9'high-1);
      when others => tempOF := (others => '0');
    end case;
    case tempOF is
      when "001"  => overflow <= '1';
      when "110"  => overflow <= '1';
      when others => overflow <= '0';
    end case;
  end process;
end architecture;
```

***

## Decodificador Hexadecimal para Display de Sete Segmentos

Nome do arquivo: conversorHex7Seg.vhd

```vhdl

library IEEE;
use ieee.std_logic_1164.all;

entity conversorHex7Seg is
  port
  (
    -- Input ports
    dadoHex  : in  std_logic_vector(3 downto 0);
    apaga  : in  std_logic := '0';
    negativo : in  std_logic := '0';
    overFlow : in  std_logic := '0';
    -- Output ports
    saida7seg : out std_logic_vector(6 downto 0)
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
  rascSaida7seg <= "1000000" when dadoHex="0000" else ---0
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
  --
  saida7seg <=    "0100011" when (overFlow='1') else
                  "1111111" when (apaga='1' and negativo='0') else
                  "0111111" when (apaga='0' and negativo='1') else
                  rascSaida7seg;
end architecture;
```

***

## Registrador

Nome do arquivo: registradorGenerico.vhd

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

 entity registradorGenerico is
    generic (
        larguraDados : natural := 8
    );
      port (DIN : in    std_logic_vector(larguraDados-1 downto 0);
           DOUT : out   std_logic_vector(larguraDados-1 downto 0);
           ENABLE : in  std_logic;
           CLK,RST : in std_logic);
 end entity;

 architecture comportamento of registradorGenerico is
 begin
    -- In Altera devices, register signals have a set priority.
    -- The HDL design should reflect this priority.
    process(RST, CLK)
    begin
        -- The asynchronous reset signal has the highest priority
        if (RST = '1') then
            DOUT <= (others => '0');
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

## Divisor

Nome do arquivo: divisorGenerico.vhd

```vhd
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;

entity divisorGenerico is
    generic
    (divisor : natural := 8);
    port(
        clk         :   in std_logic;
        saida_clk :   out std_logic
        );
end entity;

architecture divisaoPor2 of divisorGenerico is
    signal tick : std_logic;
begin
    process(clk)
    begin
        if rising_edge(clk) then
            tick <= not tick;
        end if;
    end process;
    saida_clk <= tick;
end architecture;


architecture divisaoGenerica of divisorGenerico is
    signal cnt : std_logic_vector(divisor downto 0);
    begin
        process(clk)
        begin
            if rising_edge(clk) then
                cnt <= std_logic_vector(unsigned(cnt) + 1);
            end if;
        end process;
        saida_clk <= cnt(divisor);
end architecture;
```

***

<br>

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

***

<br>

***

***

<!-- FIM -->


