# Solução da Questão 4

>Por Eduardo Marossi.


4.  A equipe de Design de Computadores deseja adicionar a uma ALU existente, a possibilidade de executar instruções do tipo SLT (Set Less Than).

Considerando que a ALU atual é de 32-bits, possui a capacidade de somar, subtrair, realizar lógica E e lógica OU, desenhe o circuito auxiliar e os sinais para implementar essa lógica.

Desconsidere que a ALU possui um sinal de carry-in e carry-out.

>Dica: verifique o que a lógica SLT faz com os bits dos dados. Cuidado com os valores resultantes na ALU.


Solução:

-   Meio caminho: realizar SUB, pegar bit mais significativo e expandir com 31-bits zero.
-   Resposta correta: levar em conta o Overflow.

```
V (overflow) = not ( (/A(31) AND /B(31) AND R) OR (A(31) AND B(31) AND /R) )
SLT = Y(31) xor V
```

<br>

***
