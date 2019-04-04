# Solução da Questão 1

>Por Eduardo Marossi.

1.  Acrescente, em VHDL, a uma ALU existente, a funcionalidade definida abaixo:
-   Multiplicação por 2, 4, 8, 16, 32, 64, . . . , 2^N (para N inteiro).
    -   Considere o código dessa FUNCAO = “100”.
-   Por exemplo:
    -   Se A = 3 e B = 1, teremos:
        -   3 * 2^1 = 6.
    -   Se A = 3 e B = 2, teremos:
        -   3 * 2^2 = 12.

>Dica: utilize o operador & para concatenar bits

Considere que a ALU tem a seguinte entidade:

```vhd
	entity ALU_Mult is

	port
	(
		-- Input ports
		A	: in  STD_LOGIC_VECTOR(5 downto 0);
		B	: in  STD_LOGIC_VECTOR(5 downto 0);

		-- Inout ports
		FUNCAO	: in  STD_LOGIC_VECTOR(2 downto 0);

		-- Output ports
		Y	: out  STD_LOGIC_VECTOR(5 downto 0)
	);
end ALU_Mult;
```
Solução:

```vhd
architecture rtl of ALU_Mult is
	signal MULT : std_logic_vector(5 downto 0);
begin
	 Y <= MULT when FUNCAO = "100" else
	"000000";

	MULT <=
	A(4) & A(3) & A(2) & A(1) & A(0) & '0' when B = "000001" else
	A(3) & A(2) & A(1) & A(0) & "00" when B = "000010" else
	A(2) & A(1) & A(0) & "000" when B = "000100" else
	A(1) & A(0) & "0000" when B = "001000" else
	A(0) & "00000" when B = "010000" else
	"000000";
end rtl;
```
