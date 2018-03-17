## Assistente de Criação de Máquinas de Estados Finitos

A criação de uma máquina de estado segue os passos:
-   Criar um novo arquivo do tipo _State Machine_
-   Vá em Menu File:
    -   Escolha: _State Machine File_.

![Imagem da Tela](imagensQuartus/novaMaquinaEstado.png)

Deverá abrir a seguinte tela:

![Imagem da Tela](imagensQuartus/telaCriarFSM-1.png)

***

Para criar as entradas e saídas da FSM, utilize as tabelas _Input Table_ e _Output Table_. Clique com o botão direito do mouse na região não utilizada da tabela desejada:

![Imagem da Tela](imagensQuartus/telaCriarFSM-InputOutputTable-2A1.png)

Podem ser criadas entradas/saídas individuais ou vetores. Note que a representação de vetor utiliza a sintaxe: nome[inicio:fim] ou nome[fim:inicio].

![Imagem da Tela](imagensQuartus/telaCriarFSM-InputOutputTable-2B.png)

Note que os nomes e tipos utilizados para os sinais de entrada e saída devem ser os mesmos utilizados na instanciação do componente.

***
Para criar os estados da FSM, utilize a ferramenta _State Tool_:

![Imagem da Tela](imagensQuartus/telaCriarFSM-DetalhePainel-1A.png)

***

Para criar as transições entre os estados da FSM, utilize a ferramenta _State Tool_:

![Imagem da Tela](imagensQuartus/telaCriarFSM-DetalhePainel-1B.png)

***

A edição das características da FSM é feita através do _State Machine Wizard_:

![Imagem da Tela](imagensQuartus/telaCriarFSM-StateMachineWizard-1.png)

***

As características da FSM são configuradas através das abas do assistente e com o botão direito do mouse. As características gerais são mostradas abaixo:

![Imagem da Tela](imagensQuartus/telaCriarFSM-StateMachineWizard-2.png)


![Imagem da Tela](imagensQuartus/telaCriarFSM-StateMachineWizard-3.png)

![Imagem da Tela](imagensQuartus/telaCriarFSM-StateMachineWizard-4.png)

![Imagem da Tela](imagensQuartus/telaCriarFSM-StateMachineWizard-5.png)

Para definir as transições, temos os valores de entrada e as seguintes operações:

Símbolo | Comparação    |  | Símbolo | Operação Lógica
--------|---------------|--|---------|----
"=="    | EQUAL         |  |  "&"    | AND
"!="    | INEQUAL       |  |  "\|"   | OR
"<="    | LESSER THAN   |  |  "^"    | XOR
"<"     | LESSER        |  |  "~&"   | NAND
">="    | GREATER THAN  |  |  "~\|"  | NOR
">"     | GREATER       |  |  "~^"   | XNOR
  ---   | ---           |  |  "~"    | NOT

![Imagem da Tela](imagensQuartus/telaCriarFSM-StateMachineWizard-6.png)

O valor de saída aceita números decimais inteiros.

![Imagem da Tela](imagensQuartus/telaCriarFSM-StateMachineWizard-7.png)

***

O resultado da edição é atualizado para o grafo da máquina de estados:

![Imagem da Tela](imagensQuartus/telaCriarFSM-grafo-1.png)

***

Para gerar o código HDL referente a essa FSM, utiliza-se o botão _Generate HDL File_:

![Imagem da Tela](imagensQuartus/telaCriarFSM-GerarHDL-1.png)

E deve-se escolher a linguagem desejada. No nosso caso: VHDL.

![Imagem da Tela](imagensQuartus/telaCriarFSM-GerarHDL-2.png)


Será criado um arquivo com o código VHDL referente à FSM definida anteriormente. Esse arquivo deve ser adicionado ao projeto.

![Imagem da Tela](imagensQuartus/telaCriarFSM-GerarHDL-3.png)

<br>

***

Para verificar os detalhes da implementação, como a tabela de transição gerada ou a codificação dos estado, utilize o _State Machine Viewer_.

Ele está no menu: Tools > Net List Viewers > State Machine Viewer.

Transições:
![Imagem da Tela](imagensQuartus/telaStateMachineViewer-1.png)

Codificação:
![Imagem da Tela](imagensQuartus/telaStateMachineViewer-2.png)

Note que os estados são representados de duas formas:
-   Com um cículo simples: significa que eles não possuem conexão com a lógica externa;
-   Com um cículo duplo: são os estados que possuem conexão com a lógica externa à FSM.
