# Register Transfer Language : RTL

É uma linguagem que exprime a transferência de dados entre registradores.
Também descreve a sequência de micro-operações necessária para executar a função desejada.

But the description of micro-operation is too lengthy and difficult so we used symbolic notations.

This symbol of notation describe by R.T.L.


| Simbolo | | Descrição | | Exemplo |
|:------------------------------------|------|:------------------------------------|------|:-------------|
|Letras e Números |  | Nome do Registrador  |   | R1, R2, R3 ... |
| Parenteses |  | Faixa dentro do Registrador |   | R1(0-7)  Dr(11-5) |
| Setas   | | Transferência de dados |   | R1<--Ac |
| Vírgula (,) |  | Separa 2 micro operações  |   |   |
| Sinal de Controle |  | Uma letra seguida de dois pontos |   | P:R1<--R2  |

Um exemplo:

Show conditional statement by 2 register transfer statement with control function.

```asm

if(P==1) then

    (R1<--R2)

else

if(Q==1) then

    (R1<--R3)

```

<br>

```asm
Sol.  P: R1<--R2

      P'Q: R1<--R3
```

<br>

**Retirado de: Computer Architecture Tutorials - RTL: http://allcomputertopics.blogspot.com/2012/12/register-transfer-language.html**

***

<br>

***

***

<!-- FIM -->

