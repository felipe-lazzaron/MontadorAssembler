# Solução da Questão 2

>Por Eduardo Marossi.


2.  Dado um vetor A, preenchido previamente com N elementos, escreva um código, em assembly para MIPS, que permita encontrar o valor máximo.
    -   O valor máximo deve ser armazenado no registrador $t4.
    -   Assuma que os dados do vetor começam na posição 0x10000004.
    -   Os dados armazenados no vetor são de 32-bits.
    -   É permitido o uso de pseudoinstruções como *li*, *move*, entre outras.

Uma possível solução:

```asm
main:
## INICIALIZA
li $t0, 0x10000000 # ENDERECO
li $t1, 0 # CONTADOR
li $t4, 0 # MAX
li $t5, 5 # N

## OBTEM ENDERECO PROX DADO
prox:
addi $t0, 4

## CARREGA DADO E COMPARA

lw $t3, ($t0)
addi $t1, 1
sub $t2, $t3, $t4
blt $t2, $zero, pula_mov
move $t4, $t3
pula_mov:
bne, $t1, $t5, prox

```

Para testar (preencher a memória):

```asm

main:

li $t0, 5
sw $t0, 0x10000000
li $t0, 3
sw $t0, 0x10000004
li $t0, 7
sw $t0, 0x10000008
li $t0, 2
sw $t0, 0x1000000c
li $t0, 8
sw $t0, 0x10000010
li $t0, 1
sw $t0, 0x10000014

```

***
