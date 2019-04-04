<a name="inicio"></a>

# Maquina de Estados

## Código VHDL para o circuito da máquina de estados

O circuito é composto de três módulos e quatro arquivos:

-   O top level (FSMtopLevel.vhd);

-   O fluxo de dados (fluxo.vhd);

-   O decodificador de hexadecimal para sete segmentos;

-   A máquina de estados (testeFSM.vhd), que será criada para controlar o funcionamento do circuito.

### Código do Top Level

Nome do arquivo: FSMtopLevel.vhd.

```vhd
library ieee;
use ieee.std_logic_1164.all;

entity FSMtopLevel is
    port (
        -- Entradas (nomenclatura definida no arquivo ¨.qsf¨)
        CLOCK_50 : in STD_LOGIC;
        KEY: in STD_LOGIC_VECTOR(3 DOWNTO 0);   --chaves de contato momentaneo.
--      SW: in STD_LOGIC_VECTOR(17 DOWNTO 0);    --chaves liga/desliga.

        -- Saidas da placa (nomenclatura definida no arquivo ¨.qsf¨)
        LEDR : out STD_LOGIC_VECTOR(17 DOWNTO 0) := (others => '0');
        LEDG : out STD_LOGIC_VECTOR(8 DOWNTO 0)  := (others => '0');
        HEX0 : OUT STD_LOGIC_VECTOR(6 DOWNTO 0)
    );
end entity;

architecture teste of FSMtopLevel is
    -- Declaraçao dos Componentes:
    COMPONENT testeFSM is
        PORT (
            reset       :    IN STD_LOGIC;
            clock       :    IN STD_LOGIC;
            bt1     :    IN STD_LOGIC;
            bt2     :    IN STD_LOGIC;
            bt3     :    IN STD_LOGIC;
            saida   :    OUT STD_LOGIC_VECTOR(3 DOWNTO 0)
        );
    END COMPONENT;
    --
    COMPONENT fluxoDados is
        PORT (
            entradaHex : in STD_LOGIC_VECTOR(3 DOWNTO 0);
            saida7seg : OUT STD_LOGIC_VECTOR(6 DOWNTO 0)
        );
    END COMPONENT;

    -- Fios:
    signal auxReset, auxBt1, auxBt2, auxBt3, auxBt1n : std_logic;
    signal auxHexValue : std_logic_vector (3 downto 0);
    signal aux7seg     : std_logic_vector (6 downto 0);

    constant usarDetectorBorda : boolean := FALSE;
--  constant usarDetectorBorda : boolean := TRUE;

begin
-- Instanciando os componentes:
maqEstados : testeFSM
    port map (
--  <formal_input> => <expression>,
        reset   => auxReset, clock => CLOCK_50, bt1 => auxBt1, bt2 => auxBt2, bt3 => auxBt3,
--      <formal_output> => <signal>,
        saida => auxHexValue
    );

fluxo : fluxoDados
        port map (
            entradaHex => auxHexValue, saida7seg => aux7seg
        );

comDetectorBorda:
    if (usarDetectorBorda) generate
        detectorSub0: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(0)), saida => auxReset);
        detectorSub1: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(1)), saida => auxBt1);
        detectorSub2: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(2)), saida => auxBt2);
        detectorSub3: work.edgeDetector(bordaSubida) port map (clk => CLOCK_50, entrada => (not KEY(3)), saida => auxBt3);
    end generate;

semDetectorBorda:
    if (not (usarDetectorBorda)) generate
        auxReset <= not KEY(0);
        auxBt1   <= not KEY(1);
        auxBt2   <= not KEY(2);
        auxBt3   <= not KEY(3);
    end generate;

    --Fazendo as interligacoes:
    LEDG(0)  <= not KEY(0);
    LEDG(1)  <= not KEY(1);
    LEDG(2)  <= not KEY(2);
    LEDG(3)  <= not KEY(3);

    HEX0 <= aux7seg;
end architecture;
```

***

### Código do Fluxo de Dados

Nome do arquivo: fluxo.vhd

```vhd

library ieee;
use ieee.std_logic_1164.all;

entity fluxoDados is
    port (
        entradaHex: in STD_LOGIC_VECTOR(3 DOWNTO 0);
        saida7seg : OUT STD_LOGIC_VECTOR(6 DOWNTO 0)
    );
end entity;

architecture teste of fluxoDados is

begin
-- instaciaçao sem declaracao de componente:
display : work.conversorHEX7Seg
    port map (
        dadoHex => entradaHex, apaga => '0', negativo => '0', overFlow => '0', saida7seg => saida7seg
        );
end architecture;

```

***

### Decodificador Hexadecimal para Display de Sete Segmentos

Nome do arquivo: conversorHex7Seg.vhd

```vhd

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
  saida7seg <=    "1100010" when (overFlow='1') else
                  "1111111" when (apaga='1' and negativo='0') else
                  "0111111" when (apaga='0' and negativo='1') else
                  rascSaida7seg;
end architecture;
```

***

### Detector de Borda

Nome do arquivo: edgeDetector.vhd

```vhd
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
end  architecture;


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
end  architecture;
```

***

<br>

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

***

<br>

***

***

<!-- FIM -->
