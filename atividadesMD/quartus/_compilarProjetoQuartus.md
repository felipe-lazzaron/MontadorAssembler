<a name="inicio"></a>

## Compilação:

O processo de compilação é dividido em algumas etapas:

-   **Análise**:

    -   Verifica cada unidade de projeto separadamente:
        -   declaração da entidade, arquitetura, etc..
        -   facilita se utilizar um arquivo por unidade de projeto.
    -   Verifica se há erros de sintaxe (gramática) ou semântica (significado);
    -   As unidades analisadas são colocadas em uma biblioteca:
        -   usando um formato interno a dependente da implementação;
        -   essa biblioteca é chamada de *work*.

-   **Elaboração**:

    -   Transforma o projeto hierárquico em um projeto plano:
        -   cria as portas (*`ports`*);
        -   cria os sinais (*`signal`*) e processos (*`process`*) dentro do corpo de cada arquitetura;
        -   para cada componente instanciado, copia a entidade e corpo de arquitetura do componente para o módulo que o utiliza;
        -   repete esse procedimento recursivamente nos corpos de arquitetura.
    -   Resultado da elaboração:
        -   conjunto de processos (*`process`*) interligados por uma rede de sinais (*`signal`*), chamado de *netlist*.
    -   É o suficiente para que a simulação possa ser executada.

<!-- **Simulação** -->

-   **Síntese**:

    -   Com o auxílio da biblioteca da tecnologia usada, traduz o projeto RTL em uma lista de conexões de portas lógicas (*gate-level netlist*):
    -   Existem restrições ao uso de algumas declarações no modelo RTL;
    -   Essas restrições dependem da ferramenta de síntese utilizada.

-   **Alocação e Roteamento**:

    -   Analisa a lista de conexões gerada na síntese e aloca os blocos funcionais (primitivas) no dispositivo alvo (modelo da FPGA ou ASIC);
    -   Faz o roteamento dos sinais que interconectam esses blocos funcionais;
    -   Verifica se foram satisfeitas as restrições (*constraints*) de área, temporização e potência.
    -   Gera um arquivo contendo todas as conexões necessárias para que a FPGA implemente a funcionalidade desejada.


***
<br>

**No Quartus, a compilação pode ser feita de três formas:**

<br>

*`Start Compilation`*: Faz a compilação completa. Isso inclui: análise sintática, criação da netlist, roteamento para a tecnologia escolhida (*fitter*), verificação das restrições de temporização do projeto, alocação dos pinos da FPGA, geração do arquivo *assembly* para gravar a FPGA, etc ...

*`Start Analysis & Elaboration`*: Analisa o projeto procurando por erros de sintaxe e semântica. Também executa a elaboração, que é a identificação da hierarquia criada. Após a execução, é possível utilizar o *RTL Viewer* e navegar pelos arquivos no *Project Navigator*.

*`Start Analysis & Synthesis`*: Analisa o projeto procurando por erros de sintaxe e semântica. Faz a extração da *netlist* e cria um banco de dados com todos arquivos do projeto. Também faz o mapeamento do projeto para a arquitetura alvo (síntese). Após a execução, é possível fazer a simulação do circuito criado.

-   Clique no ícone escolhido:
    -   Aguarde a finalização do processo;
    -   Verifique se ocorreu algum erro.

![Tela de Compilação](../imagensQuartus/telaCompilacao-1.png)

<!--- [[imagens/Aula1/TelaAnalysisElaboration.png|Imagem da Tela]]  -->
<br><br>

**Para verificar o circuito resultante da compilação, use:**

-   `Tools` > `Net List Viewers` > `RTL Viewer`

![Menu](../imagensQuartus/rtlViewerMenu.png)

<br><br><br>

**Fluxo da compilação (compilation flow) do Quartus Prime**

![Fluxo do Projeto](../imagensQuartus/designFlowQuartus-1_svg.png)

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!--- (inicio dos links)  -->
