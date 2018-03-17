<a name="inicio"></a>

## Objetivos:

1.  Aplicar o tipo de dados *`array`* do VHDL.
2.  Implementar memória ROM em VHDL.

Ir para o [fim do documento](#fimDocumento) e referências.

## Lembretes:

#### ** Visite sempre os seus amigos:

-   Os [templates do Quartus][bibliotecaTemplates];
-   O guia de referência de VHDL, no site da [Renerta][renertaVHDLRefGuide];
-   O livro: [Digital McLogic Design][freeRangeTutoriais] de Mealy & Mealy;
-   O livro [VHDL Tutorial][VHDLTutorialElsevier] do Ashenden;
-   A [ajuda interna][vhdlBasico] (ainda em construção).

#### Dicas:

-   Pense qual resultado que deseja obter:
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

## 2) Memória ROM.

### Contextualização:

Caso queira rever a contextualização do item anterior, [clique aqui](Aula-4A.html).

A memória ROM possui uma topologia parecida com a memória RAM. A diferença é que a ROM não permite a escrita durante o seu uso. Por isso, ela dispensa o sinal de leitura ou escrita.

Existem vários tipos de ROM:

-   As que são gravadas durante a fabricação e não podem mais ser alteradas (ROM);
-   As que pode ser gravadas, através de um gravador específico, pelo fabricante do circuito que a está utilizando e não podem mais ser alteradas (PROM);
-   As que pode ser gravadas e regravadas, através de um gravador específico, pelo fabricante do circuito que a está utilizando (EPROM, EEPROM, etc...).




### Objetivo:

Implementar uma ROM de 8 bits e 256 posições, contendo:

-   O nome dos participantes no projeto.

***

**Referências:**

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

***

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!---
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[vhdlBasico]:  ./vhdl/_vhdlBasico.html

[bibliotecaTemplates]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[renertaVHDLRefGuide]: http://vhdl.renerta.com

[freeRangeTutoriais]: http://freerangefactory.org/books_tuts.html

[VHDLTutorialElsevier]: http://booksite.elsevier.com/9780124077263/downloads/VHDL_Tutorials/vhdl-tutorial.pdf

[linksUteis]: ./linksUteis.html
