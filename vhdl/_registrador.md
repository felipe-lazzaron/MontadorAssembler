### Registrador com o total de bits configurável pelo _generic_:


```vhd
entity registrador is

generic (
    MAX_BIT : natural := 8
  );

port (
     DIN : in std_logic_vector(MAX_BIT-1 downto 0);
     DOUT : out std_logic_vector(MAX_BIT-1 downto 0);
     ENABLE : in std_logic;
     CLK, RESET : in std_logic
  );

end entity;

architecture comportamento of registrador is
 begin
     process(CLK,RESET)
     begin
         -- reset ativo em ALTO
         if RESET = '1' then
            --DOUT <= "00000000";
            DOUT <= (others => '0'); -- Assim, o codigo fica reconfiguravel.
         -- ativo na subida do CLK
         elsif CLK'event and CLK = '1' then
             if ENABLE='1' then
                 DOUT <= DIN;
             else            -- para evitar que seja implementado um latch.
                 null;  
             end if;
         end if;
     end process;
end architecture;

```
