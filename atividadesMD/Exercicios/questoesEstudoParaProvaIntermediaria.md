# Questões

>Por Eduardo Marossi.

***

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

<br>

***

2.  Dado um vetor A, preenchido previamente com N elementos, escreva um código, em assembly para MIPS, que permita encontrar o valor máximo.
    -   O valor máximo deve ser armazenado no registrador $t4.
    -   Assuma que os dados do vetor começam na posição 0x10000004.
    -   Os dados armazenados no vetor são de 32-bits.
    -   É permitido o uso de pseudoinstruções como *li*, *move*, entre outras.

<br>

***

3.  Um engenheiro está utilizando um microprocessador, MIPS, para o controle de uma planta de produção. Com as seguintes características:

    -   O acionamento do compressor de resfriamento está mapeado em memória na posição 0x100, sendo que qualquer valor diferente de zero liga o mesmo.
    -   O acionamento do forno está mapeado em memória na posição 0x104, sendo que qualquer valor diferente de zero liga o mesmo.
    -   Um sensor contendo o valor da temperatura em Celsius (inteiro) está mapeado na posição 0x108.

Escreva, em assembly para o MIPS, uma rotina que:
-   Quando o sensor estiver acima de 100 Celsius:
    -   Acione o compressor;
-   Caso esteja abaixo:
    -   Acione o forno.

Por questões de desempenho, utilize apenas as instruções LW (load word), SW (store word), SLTI (Set Less Than Immediate) e BEQ (Branch On Equal). É permitido utilizar *labels*.

<br>

***

4.  A equipe de Design de Computadores deseja adicionar a uma ALU existente, a possibilidade de executar instruções do tipo SLT (Set Less Than).

Considerando que a ALU atual é de 32-bits, possui a capacidade de somar, subtrair, realizar lógica E e lógica OU, desenhe o circuito auxiliar e os sinais para implementar essa lógica.

Desconsidere que a ALU possui um sinal de carry-in e carry-out.

>Dica: verifique o que a lógica SLT faz com os bits dos dados. Cuidado com os valores resultantes na ALU.

<br>

***
