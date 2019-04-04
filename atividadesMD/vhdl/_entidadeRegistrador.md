# Entidade para o Registrador

Note que o *`generic`* é uma forma de configurar a largura do registrador.

```vhdl
entity registrador is

generic (
    MAX_BIT : natural := 8
);

port (DIN : in std_logic_vector(MAX_BIT-1 downto 0);
     DOUT : out std_logic_vector(MAX_BIT-1 downto 0);
     ENABLE : in std_logic;
     CLK, RESET : in std_logic);
end registrador;

```

***

<br>

***

***

<!-- FIM -->
