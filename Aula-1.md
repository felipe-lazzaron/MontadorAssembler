<a name="inicio"></a>

## Objetivos:

#### Usaremos o Quartus Prime Lite para:

-   Criar diagramas esquemáticos (circuitos) das portas lógicas:

    -   AND;
    -   OR;
    -   NOT;
    -   E de circuitos combinacionais envolvendo as portas acima.

-   Simular o funcionamento desses circuitos.
-   Analisar o código VHDL criado a partir desses circuitos esquemáticos.

    [Ir para o fim do documento](#fimDocumento).

***
## Criar projeto no Quartus Prime Lite:

Crie um projeto no Quartus com o nome Aula1. Caso precise de auxílio, acesse a página:

[Criar Projeto no Quartus](./quartus/_criarProjetoQuartus.html).

***

## Criar o diagrama lógico do circuito:

Para desenhar o diagrama lógico do circuito (portas AND, OR, NOT), existe a opção:

`File` > `New` > `Block Diagram/Schematic File`

Caso precise de ajuda, acesse a página:

[Criar Esquema no Quartus][esquemaQuartus].

***

## Compilar o circuito:

Uma vez criado o circuito, deve-se testar o seu funcionamento através de simulação.
Porém, para simular é preciso compilar o circuito. Existem três formas diferentes de fazer a compilação, veja no link abaixo:

[Compilar Projeto no Quartus][compilarQuartus].

***

## Para simular o circuito, crie uma nova simulação:

[Simular Circuito no Quartus](./quartus/_simulacao.html).

***

## Faça o mesmo para as outras portas lógicas.

***

## Geração de código VHDL:

Como foi utilizado o diagrama lógico do circuito como entrada da descrição, é interessante verificar o código VHDL que foi gerado. Para tanto, veja o link abaixo:

[Criar Código VHDL](./quartus/_geraCodigoVHDL.html).

***

<!--
## Discussão sobre a sintaxe/semântica.

Veja o quiz em [socrative](https://www.socrative.com/) com "Room name": DCINSPER.

***
-->

## Circuito combinacional:

-   Crie o circuito combinacional relativo à equação abaixo:

<center>SAIDA = A D + B' D + A B' C' ;</center>

-   Compile e faça a simulação. Os vetores de teste para a simulação devem ser [parecidos com estes][simulacaoComEquacao].
-   Gere o [código VHDL][circuitoEquacaoEsquema-VHDL] e verifique quais novos comandos foram usados.

**Referências:**

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).


<!-- [//]: # (inicio dos links) -->
[esquemaQuartus]: ./quartus/_criaDiagramaLogico.html
[compilarQuartus]: ./quartus/_compilarProjetoQuartus.html
[circuitoEquacaoEsquema-VHDL]:./vhdl/_combinacionalEquacaoVHDL.html
[simulacaoComEquacao]: ./quartus/_simulacaoCombinacionalEquacao.html
[linksUteis]: ./linksUteis.html

<!--- FIM --->
