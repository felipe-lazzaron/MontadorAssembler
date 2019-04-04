## Assistente de Criação de Máquinas de Estados Finitos

A criação de uma máquina de estado segue os passos:

-   Criar um novo arquivo do tipo _State Machine_
-   Vá em Menu File:
    -   Escolha: _State Machine File_.

![](../imagensQuartus/novaMaquinaEstado.png)

<br>

Deverá abrir a seguinte tela:

![](../imagensQuartus/telaCriarFSM-1.png)

***

<br>

Para criar as entradas e saídas da FSM, utilize as tabelas _Input Table_ e _Output Table_. Clique com o botão direito do mouse na região não utilizada da tabela desejada:

![](../imagensQuartus/telaCriarFSM-InputOutputTable-2A1.png)

<br>

Podem ser criadas entradas/saídas individuais ou vetores. Note que a representação de vetor utiliza a sintaxe: nome\[inicio:fim\] ou nome\[fim:inicio\].

![](../imagensQuartus/telaCriarFSM-InputOutputTable-2B.png)

<br>

Note que os nomes e tipos utilizados para os sinais de entrada e saída devem ser os mesmos utilizados na instanciação do componente.

***

<br>

Para criar os estados da FSM, utilize a ferramenta _State Tool_:

![](../imagensQuartus/telaCriarFSM-DetalhePainel-1A.png)

***

<br>

Para criar as transições entre os estados da FSM, utilize a ferramenta _State Tool_:

![](../imagensQuartus/telaCriarFSM-DetalhePainel-1B.png)

***

<br>

A edição das características da FSM é feita através do _State Machine Wizard_:

![](../imagensQuartus/telaCriarFSM-StateMachineWizard-1.png)

***

<br>

As características da FSM são configuradas através das abas do assistente e com o botão direito do mouse. As características gerais são mostradas abaixo:


![](../imagensQuartus/telaCriarFSM-StateMachineWizard-2.png)

<br>

![](../imagensQuartus/telaCriarFSM-StateMachineWizard-3.png)

<br>

![](../imagensQuartus/telaCriarFSM-StateMachineWizard-4.png)

<br>

![](../imagensQuartus/telaCriarFSM-StateMachineWizard-5.png)

<br>

Para definir as transições, temos os valores de entrada e as seguintes operações:

 Símbolo | Comparação
--------------|------------------------
 "==" | EQUAL
 "!=" | INEQUAL
 "<=" | LESSER THAN
 "<"  | LESSER
 ">=" | GREATER THAN
 ">"  | GREATER

<br>

 Símbolo | Operação Lógica
--------------|-------------------
 "&" | AND
 "\|" | OR
 "^" | XOR
 "~&" | NAND
 "~\|" | NOR
 "~^" | XNOR
 "~" | NOT

<br>

![](../imagensQuartus/telaCriarFSM-StateMachineWizard-6.png)

<br>

O valor de saída aceita números decimais inteiros.

![](../imagensQuartus/telaCriarFSM-StateMachineWizard-7.png)

***

<br>

O resultado da edição é atualizado para o grafo da máquina de estados:

![](../imagensQuartus/telaCriarFSM-grafo-1.png)

***

<br>

Para gerar o código HDL referente a essa FSM, utiliza-se o botão _Generate HDL File_:

![](../imagensQuartus/telaCriarFSM-GerarHDL-1.png)

<br>

E deve-se escolher a linguagem desejada. No nosso caso: VHDL.

![](../imagensQuartus/telaCriarFSM-GerarHDL-2.png)

<br>

Será criado um arquivo com o código VHDL referente à FSM definida anteriormente. Esse arquivo deve ser adicionado ao projeto.

![](../imagensQuartus/telaCriarFSM-GerarHDL-3.png)

<br>

***

<br>

Para verificar os detalhes da implementação, como a tabela de transição gerada ou a codificação dos estado, utilize o _State Machine Viewer_.

Ele está no menu: Tools > Net List Viewers > State Machine Viewer.

Transições:
![](../imagensQuartus/telaStateMachineViewer-1.png)

Codificação:
![](../imagensQuartus/telaStateMachineViewer-2.png)

<br>

Note que os estados são representados de duas formas:

-   Com um círculo simples: significa que eles não possuem conexão com a lógica externa;
-   Com um círculo duplo: são os estados que possuem conexão com a lógica externa à FSM.
