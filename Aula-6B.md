<a name="inicio"></a>

## Objetivos:

1.  Projetar máquinas de estados finitos (MEF ou FSM) para controlar circuitos digitais.
2.  Usar o assistente do Quartus para criação de FSMs.
3.  Visualização dos estados e das regras de transição (entre estados) através da opção: _State Machine Viewer_.
4.  Programar o kit de desenvolvimento com o circuito final.

## Conteúdo:

*   Controlar uma ULA simplificada.

[Ir para o fim do documento](#fimDocumento).

## Implementações:

Para se familiarizar com o posicionamento das entradas e saídas da placa DE2-115, acesse esta [página][placaDE2-115].

## 2) Controlar uma ULA simples.

***

### Contextualização:

Para controlar o fluxo de dados, é necessário ativar cada elemento na ordem correta para obter o resultado desejado.

Como pode ser visto na figura abaixo, os controles existentes são:

-   Carrega A: quando em nível alto, ativa o sinal de _ENABLE_ do registrador que alimenta a entrada A da ULA. Durante a primeira (próxima) transição de subida do _clock_, o registrador transferirá o valor de entrada (SW(7 downto 0)) para as suas saídas (entrada A da ULA);
-   Carrega B: o mesmo para a entrada B da ULA;
-   Função: dois bits que definem a função a ser executada usando os valores A e B.
-   Carrega Saída: quando em nível alto, ativa o sinal de _ENABLE_ do registrador que recebe o resultado da ULA, para transferí-lo para a saída na próxima borda de subida do _clock_.

Os registradores A e B existem para que possa ser compartilhada a entrada de dados.

Note que o registrador de saída possui 9 bits. Os bits (7 downto 0) são o resultado da operação e o bit 8 é a indicação de _overflow_.

O sinal de _clock_ está distribuído pelo fluxo de dados e só foi indicado pelo nome.

![](./imagensComponentes/FluxoDados_aula6.svg)

***

#### Módulos fornecidos:

O foco está na implementação da FSM para a calculadora. Os módulos utilizados estão [disponíveis aqui][modulosAula6B]. Eles são:

-   O _top level_, onde deverá ser acoplada a máquina de estados;
-   O fluxo de dados;
-   A ULA;
-   O conversor hexadecimal para 7 segmentos;
-   O registrador com o total de bits configurável;
-   O divisor genérico.

#### Objetivo:

Construir a máquina de estados para controlar uma calculadora hexadecimal (com sinal).

Utilizando os módulos fornecidos, faremos o controle de uma ULA com as funções:

-   Somar considerando o sinal (código de seleção: 00);
-   Subtrair considerando o sinal (código de seleção: 01);
-   XOR lógico ((código de seleção: 10);
-   AND lógico (código de seleção: 11).

>Os valores de entrada e resultado aparecerão em hexadecimal, portanto, cuidado ao avaliar os resultados.

As características gerais são:

-   Os valores de entrada são definidos pelas chaves SW0 a SW7;
-   A função da ULA é definida pelas chaves SW16 e SW17;
-   O botão Key3 é o sinal de carregamento do valor para a entrada A da ULA;
-   O botão Key2 é o sinal de carregamento do valor para a entrada B da ULA;
-   O botão Key1 é o _reset_ da máquina de estados (não limpa os registradores);
-   O botão Key0 é o _reset_ dos registradores.

Faz parte da atividade:

-   Analisar o código entregue, para entender os detalhes de funcionamento;
-   Criar a máquina de estados;
-   Fazer a integração da máquina de estados;
-   Compilação, testes e gravação no kit;
-   Demonstração para o professor.

A entrega do código e deve ser feita pelo Blackboard.

<br><br>

***

**Referências:**

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!---
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->
[placaDE2-115]:  ./fpga/_layoutDE2_115.html

[linksUteis]: ./linksUteis.html

[modulosAula6B]: ./vhdl/_modulosCalculadoraFSM.html

<!---   FIM  --->
