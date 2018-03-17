<a name="inicio"></a>

## Projeto 1: Relógio Digital

Ir para o [fim do documento](#fimDocumento) e referências.

## Descrição:

Este projeto será a criação de um relógio digital, em VHDL, com as seguintes características:

-   Indica horas e minutos (segundos é opcional);

-   Possui algum sistema para acertar o horário;

-   Possui seleção da base de tempo:

    -   Para mostrar a passagem das 24 horas em tempo reduzido:

        -   Utilizado para verificar se o projeto funciona corretamente.

Opcionais que adicionam valor ao projeto:

-   Sistema de despertador;

-   Temporizador com contagem regressiva;

-   Implementação microprogramada;

-   Caso tenha ideia para algum opcional, confira antes se ele adiciona valor ao projeto.

Existem poucos critérios que limitam a liberdade de criação neste projeto:

-   Deve utilizar um fluxo de dados contendo uma ULA:

    -   Responsável pelos cálculos envolvidos na contagem de tempo;

-   O controle desse fluxo de dados pode ser através de:

    -   Máquina de estados finitos;

    -   Microprogramado.

-   O horário deverá ser mostrado através do display de sete segmentos.

### Entrega:

A data de entrega, que está no plano de aula, é: 26/09.

A avaliação do projeto segue o descrito no plano de aula. Ela será feita através dos seguintes itens:

-   Apresentação do projeto, no kit de desenvolvimento:

    -   Com arguição do(s) professor(es).

-   Entrega de um resumo explicativo do funcionamento do circuito, contendo:

    -   Diagrama de blocos do projeto;

    -   Diagrama de estados (se for o caso);

    -   Com comentários (opcional) sobre os problemas encontrados.   

-   Entrega do projeto do Quartus, com:

    -   Código VHDL, devidamente documentado e com o nome dos participantes;

    -   Arquivo com conteúdo da microprogramação (se for o caso).

#### Execução:

Em grupo, com até 3 alunos.

***

#### Um rascunho de metodologia:

1.  Liste as funções que o projeto terá, incluindo as entradas e saídas do circuito.

2.  Liste os macro elementos de hardware necessários para executar essas funções:

    -   ULA, registradores, decodificadores, etc...

3.  Esboce um fluxo de dados (FD) que implemente a função básica:

    -   Esse esboço deve possuir a interligação dos componentes e a definição dos pontos de controle (crie um nome significativo para cada ponto de controle);

    -   Defina um vetor de bits que reúne todos os pontos de controle. Essa é a sua palavra de controle.

    -   Se preferir pensar em termos de algoritmo, lembre que:

        -   O comando _if_  e o _case_ são equivalentes ao multliplex (com ponto(s) de controle);

        -   As variáveis são equivalentes a registradores ou banco de registradores (com ponto(s) de controle);

        -   Uma comparação é o resultado XNOR dos dois valores;

        -   Para detectar um resultado igual a zero, use uma porta OR

        -   As operações lógicas e aritméticas são feitas pela ULA (com ponto(s) de controle);

<br>

Exemplo de fluxo de dados:

<br>

![](./imagensComponentes/FluxoDados_aula6_pqn.svg)

<br>

4.  Simule, com papel e lápis, o funcionamento do FD:

    -   Levante a sequência de ativação dos pontos de controle (palavras de controle), para cada função que deseja executar;

    -   Uma função pode ativar vários pontos de controle ao mesmo tempo e/ou em sequência (essas são as microoperações).

5.  Quando o FD básico estiver pronto, codifique em VHDL e simule no Quartus:

    -   Na simulação, verifique se as palavras de controle estão corretas, tanto no conteúdo quanto na sequência, e anote qualquer alteração necessária.

6.  Repita o processo para criar novas funcionalidades:

    -   Pode ser feito partindo-se do FD atual;

    -   Ou com um FD novo, que depois terá de ser integrado ao existente com a remoção dos elementos que são comuns.

7.  Com o FD completo e testado, utilize as anotações das palavras de controle para fazer o sequenciador da unidade de controle.

Uma forma de definir as operações do fluxo de dados é utilizando RTL (Register Transfer Language):

-   Que possui uma notação (RTN) para exprimir as operações que ocorrem em um ciclo de _clock_. Ou seja, cada passo elementar do processo ou instrução.

-   A explicação mais resumida, que encontrei, sobre essa notação está em:

    -   [allcomputertopics : RTL](http://allcomputertopics.blogspot.com/2012/12/register-transfer-language.html)

    -   [allcomputertopics : microoperações](http://allcomputertopics.blogspot.com/2012/12/micro-operations.html)

***

### Leituras:

Livro texto (Organização e Projeto de Computadores: A Interface Hardware/Software):

-   Capítulo 4, item 3 (construindo um fluxo de dados);

-   Apêndice D, completo;

Caso queira ler mais, veja o livro do Stallings (Arquitetura e Organização de Computadores):

-   Capítulos 14 e 15.

***

### Ferramentas:

Acredito que o Logic Friday pode ser de alguma valia. Veja nos links úteis.

<br>

**Referências:**

[Página com links][links] de referências sobre VHDL, Quartus, etc ...

***

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!---
######### (inicio dos links) ##########
--->

[links]: ./linksUteis.html
