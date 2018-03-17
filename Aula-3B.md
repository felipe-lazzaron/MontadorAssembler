<a name="inicio"></a>

## Objetivos:

1.  Rever lógica sequencial a partir do uso de Templates do Quartus.
2.  Visualização RTL.

Ir para o [fim do documento](#fimDocumento) e referências.

<a name="flip-flop"></a>

## Implementações:

<a name="registrador"></a>

### 2) Registrador em VHDL.

Queremos implementar o registrador de 8 bits mostrado abaixo:

![Imagem do Registrador](imagensComponentes/registrador8bitsPCFS.png)

Para criar um registrador, inicialmente, criaremos o esqueleto do circuito:

-   Crie um novo arquivo com o nome *`registrador`*;
-   Adicione esse arquivo ao projeto.
-   Adicione ao arquivo a biblioteca IEEE e a cláusula de uso para: *`ieee.std_logic_1164.all`*;
-   Crie uma entidade chamada *`registrador`* ;
-   Crie uma arquitetura chamada *`comportamento`*;
-   Defina a [*Top Level Entry*][topLevelEntity] para a entidade desse arquivo;

>    É importante usar o nome *`registrador`* para o arquivo e entidade, pois reutilizaremos esse arquivo no projeto hierárquico.

**Personalização do código:**

**Entidade:**

A largura de dados do registrador será definida com:

-   O tipo de dados da biblioteca **IEEE**: ***std_logic_vector***:
    -   Com o seu limite superior definido por um parâmetro.
-   A declaração *`generic`*:
    -   Onde está definido o valor padrão desse parâmetro.

No nosso caso, definiremos a largura de dados do registrador em 8 bits.

Também adicionaremos um sinal de habilitação (Enable) e outro de reinicialização (Reset).

<!--
O código da *`Entity`* será similar a [este código][entidadeRegistrador].
-->
**Arquitetura:**

O funcionamento do registrador, definido dentro da *Architecture*, será feito com:

-   O template *`Basic Positive Edge Register with Asynchronous Reset and Clock Enable`*.
-   Portanto, insira esse *template* dentro da *`architecture`*:

O funcionamento é similar ao flip flop tipo D, porém, a atualização da saída é executada para o vetor todo.

Lembre que o *reset* deve ser feito em todo o vetor. Para tanto, utilize o comando:

-   DOUT <= (OTHERS => '0');

Ele faz com que todos os bits do registrador, na quantidade definida no parâmetro *`generic`*, recebam a atribuição do nível lógico '0'.

[Compile][compilacao] o circuito e verifique, com o [RTL Viewer][rtlViewer], se o resultado da compilação foi o [desejado][rtlREG].

**Simulação:**

Para testar o registrador, precisaremos de:

-   Sinal de *clock*;
-   Sinal de entrada de dados com a largura definida no *`generic`*.

Na simulação, como foi definida a largura de 8 bits para o registrador, o vetor de teste pode ser agrupado em 8 bits e exibido em hexadecimal. Veja uma opção para fazer o [vetor de estímulos][vetorREG].

Verifique o [resultado][simulREG] da simulação.

<br><br>

**Referências:**

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

***

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!--
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[topLevelEntity]: ./quartus/_recursosQuartus.html#configurar-a-top-level-entity

[compilacao]: ./quartus/_compilarProjetoQuartus.html

[rtlViewer]: ./quartus/_rtlViewerQuartus.html

[simulREG]: ./vhdl/_simulacaoRegistrador.html

[rtlREG]: ./vhdl/_rtlRegistrador.html

[vetorREG]: ./vhdl/_simulacaoConfigRegistrador.html

[linksUteis]: ./linksUteis.html
