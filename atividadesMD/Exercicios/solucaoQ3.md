# Solução da Questão 3

>Por Eduardo Marossi.

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

Uma possível solução:

```asm
main:
lw $t0, 0x10000008 ## temp
loop:
slti $t3, $t0, 100
sw $t3, 0x10000000 ## liga forno se slti for menos de 100c
slti $t4, $t3, 1
sw $t4, 0x10000004
beq $zero, $zero, loop
```

Para testar (preencher a memória):

```asm
main:
li $t0, 90
sw $t0, 0x10000008
```
***
