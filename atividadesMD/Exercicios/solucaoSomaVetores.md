# Solução da Soma de Vetores


Utilizando linguagem assembly do MIPS, escreva um programa que:

-   Dados dois vetores de 10 posições, contendo inteiros com sinal;
-   Faça a soma, posição a posição, desses dois vetores e crie um terceiro vetor com os resultados;
-   Para simplificar, considere que:
    -   O espaço dos vetores já está alocado no seguimento .data;
    -   O início do seu programa é a rotina “main”, que já está definida em .text;
    -   Nenhuma soma gera “overflow”.

### Solução:

```asm

#Soma de Vetores
.data
vetor1:   .word     1 2 3 4 5 6 7 8 9 10
vetor2:   .word     1 2 3 4 5 6 7 8 9 10
vetor3:   .word     21 22 23 24 25 26 27 28 29 30

.text
.globl main
main:

# Inicializa contador e ponteiros:
li    $t0, 10;                   # contador
la   $t1, vetor1;              # endereco vetor
la   $t2, vetor2;
la   $t3, vetor3;

inicio:
# Carrega Valores:
lw   $t4, 0($t1);
lw   $t5, 0($t2);

# Soma:
add   $t6, $t5, $t4;

# Armazena no vetor3:
sw     $t6, 0($t3);

#incrementa ponteiros:
addi   $t1, $t1, 4;
addi   $t2, $t2, 4;
addi   $t3, $t3, 4;

#decrementa contador:
addi    $t0, $t0, -1;

# desvia:
beq     $t0, $0, fim;
j        inicio;

fim:
li        $v0,10;         # Fim da execução: código 10.
syscall

```

<br>

***
