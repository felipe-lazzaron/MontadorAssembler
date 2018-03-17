<a name="inicio"></a>

## Objetivos:

1.  Aplicar o tipo de dados *`array`* do VHDL.
2.  Implementar memória RAM em VHDL.
3.  Implementar memória ROM em VHDL..


## Conteúdo:
*   [Memória RAM](#memRAM);
*   [Memória RAM](#memRAM);
*   [Arquivo de Registradores](#arqREG).


<!--
4.  Usar projeto hierárquico (Instanciar) em VHDL.
*   [Projeto hierárquico](#projHierarquico).
*   [Codificadores](#???)
*   [Decodificadores](#???);  -->

Ir para o [fim do documento](#fimDocumento) e referências.

## Lembretes:
#### ** Visite sempre os seus amigos:
-   Os [templates do Quartus][bibliotecaTemplates];
-   O guia de referência de VHDL, no site da [Renerta][renertaVHDLRefGuide];
-   O livro: [Digital McLogic Design][freeRangeTutoriais] de Mealy & Mealy;
-   O livro [VHDL Tutorial][VHDLTutorialElsevier] do Ashenden;
-   A [ajuda interna][vhdlBasico] (ainda em construção).

#### Dicas:

-   Pense qual resultado que deseja obter;
    -   Esboce no papel um diagrama representando esse objetivo;
    -   Ou uma tabela da verdade. Ou o que for mais adequado.
-   Monte a estrutura básica do VHDL no seu arquivo de trabalho:
    -   Utilize um componente por arquivo;
    -   O nome do arquivo deve ser o nome da entidade desse componente;
    -   Assim é mais fácil de reutilizá-lo no futuro.
-   Para alguns casos, o uso da configuração com *generics* permite:
    -   Criar componentes mais versáteis, com largura de entrada/saída parametrizáveis.
    -   Aumentando a possibilidade de reutilização desse código.
-   Verifique se o esquema RTL é funcionalmente similar ao seu objetivo de implementação.
-   Simule o funcionamento do seu circuito. Se houver uma tabela da verdade:
    -   Ela já indica os vetores de entrada e os resultados na saída.
    -   Caso não exista ou a quantidade de possibilidades é muito grande:
        -   Fique atento para os casos nos extremos da sua faixa de valores de entrada.
***

## Implementações:
<a name="memRAM"></a>
## 1) Memória RAM.
### Contextualização:

#### Lógica sequencial e memórias.



#### Arrays em VHDL.




### Objetivo:


A lógica combinacional permite criar uma variedade de circuitos. Porém, em termos de


***




##### Para um chute inicial:

> No Quartus, existe um exemplo de somador/subtrator dentro de: *templates, VHDL, full designs*.

Usando esse *template* como base, ainda falta adicionar as outras funções e implementar o seletor.

<br>

***
#### Se sobrar tempo:


<!--
### Exemplo de um somador completo para um bit:

![Somador](imagensComponentes/somadorCompleto.png)

--->

<!--- TODO colocar avaliações do aprendizado, talvez pelo blackboard  -->

***
<br><br>

**Referências:**

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

***

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!---
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[vhdlBasico]:  ./__vhdlBasico

[bibliotecaTemplates]: ./_recursosQuartus#acessar-a-biblioteca-de-modelos-templates

[simulacaoVWF]: ./_simulacao

[compilacao]: ./_compilarProjetoQuartus

[rtlViewer]: ./_rtlViewerQuartus

[renertaVHDLRefGuide]: http://vhdl.renerta.com

[freeRangeTutoriais]: http://freerangefactory.org/books_tuts.html

[VHDLTutorialElsevier]: http://booksite.elsevier.com/9780124077263/downloads/VHDL_Tutorials/vhdl-tutorial.pdf

<!--
[novoProjeto]: ./_criarProjetoQuartus

[recursosQuartus]: _recursosQuartus

[adicionarArqProjeto]:./_recursosQuartus#adicionar-um-arquivo-ao-projeto

[clausulaBiblioteca]: ./_recursosQuartus#acessar-a-biblioteca-de-modelos-templates

[clausulaUse]: ./_recursosQuartus#escolher-os-templates-de-interesse

[entidade]: ./_recursosQuartus#escolher-os-templates-de-interesse

[arquitetura]: ./_recursosQuartus#escolher-os-templates-de-interesse

[topLevelEntity]: ./_recursosQuartus#configurar-a-top-level-entity

[concurrentStatements]: ./_recursosQuartus#concurrentStatements
<!--
[inserirTemplateEscolhido]: ./_recursosQuartus#inserir-o-template-escolhido

[instanciacao]: ./_recursosQuartus#instanciacao

[declaracao]: ./_recursosQuartus#declaracao

[entidade]: ./_recursosQuartus#escolher-os-templates-de-interesse

[arquitetura]: ./_recursosQuartus#escolher-os-templates-de-interesse

[entidadeRegistrador]: ./_entidadeRegistrador

[codigoPipeline]: ./_pipeline

[rtlFFD]: ./_flipFlopTipoD#esquema-rtl-do-flip-flop-do-c%C3%B3digo-acima

[simulFFD]: ./_simulacaoFFD

[simulREG]: ./_simulacaoRegistrador

[rtlREG]: ./_rtlRegistrador

[vetorREG]: ./_simulacaoConfigRegistrador

[vetoresPipeline]: ./_simulacaoConfigPipeline
-->
<!---
#######################################
###########Links Externos##############
####################################### --->

[linksUteis]: ./Links-Úteis

<!--
[IntelHierarchicalDesign]: https://www.altera.com/support/support-resources/design-examples/design-software/vhdl/v_hier.html
-->
<!---
fim
--->
