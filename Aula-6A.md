<a name="inicio"></a>

## Objetivos:

1.  Projetar máquinas de estados finitos (MEF ou FSM) para controlar circuitos digitais.
2.  Usar o assistente do Quartus para criação de FSMs.
3.  Visualização dos estados e das regras de transição (entre estados) através da opção: _State Machine Viewer_.
4.  Programar o kit de desenvolvimento com o circuito final.

## Conteúdo:

*   Implementação de contador sequencial (atividade 1);
*   Controlar uma ULA simplificada (atividade 2).

[Ir para o fim do documento](#fimDocumento).

## Implementações:

Como iremos transferir o código para o kit de FPGA, é interessante se familiarizar com o posicionamento das entradas e saídas da placa DE2-115.

Nesta [página][placaDE2-115] está o posicionamento e nome dos periféricos da placa. Utilizaremos as chaves, botões, leds e o _display_ de 7 segmentos.

## 1) Contador com máquina de estados.

### Contextualização:

Até agora, só testamos os circuitos através de simulação. E, como não foram definidas as interligações das entradas e saídas do circuito com os pinos da FPGA, o compilador ficou livre para fazer a escolha.

Para testar no kit, é necessário fazer o mapeamento do circuito com os periféricos do kit que são externos à FPGA. Isso é feito através do arquivo **".qsf"**, presente na pasta do  projeto.

No caso da placa de desenvolvimento utilizada, existe o arquivo [.qsf para a placa DE2-115][qsf-DE2-115]. Além de definir a família da FPGA utilizada e os padrões de E/S, ele faz a relação da localização dos pinos da FPGA com um nome (_signal_) para ser utilizado no programa VHDL.

Outra novidade é a programação do código binário na FPGA. Para tanto, é necessário que o programa do gravador (interno ao Quartus) esteja funcionando e reconheça a placa DE2-115.

#### Módulos fornecidos:

Esta atividade é a implementação de um contador com FSM, a sua simulação e gravação no kit de FPGA. Porém, como o foco é a máquina de estados, serão fornecidos:

-   O _top level_, que faz a interligação entre os módulos e a conexão aos pinos da FPGA;
-   O fluxo de dados (FD), que possui o circuito a ser controlado. Inicialmente será um _display_ de 7 segmentos.
-   O arquivo com o código do controlador do _display_, que é instanciado no FD;
-   O detector de borda.

A descrição desses arquivos está disponível [aqui][maqEstados].

Como o _COMPONENT_ da FSM que será criada, chamado _testeFSM_, já está criado no _top level_, é mais fácil utilizar a interface entre a máquina de estado e o circuito controlado com padrão já definido:

```vhd
COMPONENT testeFSM is
  PORT (
    reset	:	 IN STD_LOGIC;
    clock	:	 IN STD_LOGIC;
    bt1		:	 IN STD_LOGIC;
    bt2		:	 IN STD_LOGIC;
    bt3		:	 IN STD_LOGIC;
    saida	:	 OUT STD_LOGIC_VECTOR(3 DOWNTO 0)
  );
```

No módulo do fluxo de dados, os sinais estão conectados da seguinte forma:

-   reset, conectado ao bt0, que por sua vez é conectado com a chave de contato momentâneo KEY0 (está na extrema direita da placa);
-   clock, conectado ao Sinal CLOCK_50 (entrada de clock de 50MHz);
-   bt1, conectado à segunda chave de contato momentâneo: KEY1;
-   bt2, conectado a KEY2;
-   bt3, conectado a KEY3;
-   saída, conectada ao fluxo de dados e enviada ao decodificador do _display_.


#### Assistente de Criação de FSM:

O assistente de criação de máquina de estados é uma interface gráfica para a criação do diagrama de estados. Após criado o diagrama, é necessário salvar o código VHDL em um arquivo e adicionar ao projeto.

Para usar o assistente de criação de máquina de estados, visite esta [página][assistenteFSM].

### Objetivo:

Com os arquivos fornecidos, iremos implementar um contador:

-   Com a faixa de contagem de 0 a 3;
-   Podendo contar incrementando (botão KEY1);
-   Ou decrementando (botão KEY3).

O diagrama de estados está mostrado abaixo:

![Diagrama de estados](./imagensQuartus/contadorSobeDesce-1.png)

Crie esse diagrama e gere o arquivo VHDL.

Adicione esse arquivo ao projeto.

Compile o projeto para ser simulado e execute a simulação.

Se tudo estiver funcionando como esperado, compile o projeto para gerar o arquivo _assembly_ e [grave][gravarFPGA] o resultado na placa DE2-115.

Faça o teste usando os botões KEY1 (incrementa) e KEY3 (decrementa).

No _top level_, existe uma constante definindo se usará ou não o detector de borda:

```vhd
    constant usarDetectorBorda : boolean := FALSE;
--    constant usarDetectorBorda : boolean := TRUE;

```

Veja o funcionamento do código e ative o uso do detector de borda.
Compile novamente e faça o teste no kit.

***

**Qual a função do botão 2, nas duas implementações?**

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

[maqEstados]: ./vhdl/_maquinaEstados.html

[assistenteFSM]: ./quartus/_assistenteCriacaoFSM.html

[linksUteis]: ./linksUteis.html

[gravarFPGA]: ./quartus/_gravacaoFPGA.html

[qsf-DE2-115]: ./fpga/_qsfDE2_115.html

<!---   FIM  --->
