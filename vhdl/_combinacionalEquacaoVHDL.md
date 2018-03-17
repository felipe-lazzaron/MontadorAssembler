### Código VHDL referente à equação booleana:

SAIDA = AD + B'D + AB'C'

```vhd
LIBRARY ieee;
USE ieee.std_logic_1164.all;
LIBRARY work;

ENTITY circuitoCombinacionalEquacao IS
	PORT
	(
		A :  IN  STD_LOGIC;
		B :  IN  STD_LOGIC;
		C :  IN  STD_LOGIC;
		D :  IN  STD_LOGIC;
		SAIDA :  OUT  STD_LOGIC
	);
END circuitoCombinacionalEquacao;

ARCHITECTURE bdf_type OF circuitoCombinacionalEquacao IS
	SIGNAL	SYNTHESIZED_WIRE_6 :  STD_LOGIC;
	SIGNAL	SYNTHESIZED_WIRE_1 :  STD_LOGIC;
	SIGNAL	SYNTHESIZED_WIRE_2 :  STD_LOGIC;
	SIGNAL	SYNTHESIZED_WIRE_3 :  STD_LOGIC;
	SIGNAL	SYNTHESIZED_WIRE_4 :  STD_LOGIC;
BEGIN
	SYNTHESIZED_WIRE_1 <= SYNTHESIZED_WIRE_6 AND D;
	SYNTHESIZED_WIRE_2 <= D AND A;
	SAIDA <= SYNTHESIZED_WIRE_1 OR SYNTHESIZED_WIRE_2 OR SYNTHESIZED_WIRE_3;
	SYNTHESIZED_WIRE_4 <= NOT(C);
	SYNTHESIZED_WIRE_3 <= SYNTHESIZED_WIRE_4 AND SYNTHESIZED_WIRE_6 AND A;
	SYNTHESIZED_WIRE_6 <= NOT(B);
END bdf_type;
```
---

### Diagrama do circuito digital referente à equação booleana:

![](../imagensQuartus/circuitoCombinacionalEquacao-Esquema.png)
