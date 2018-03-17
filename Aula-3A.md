<a name="inicio"></a>

## Objetivos:

1.  Rever lógica sequencial a partir do uso de Templates do Quartus.
2.  Visualização RTL.
3.  Usar projeto hierárquico (Instanciar) em VHDL.

## Implementações:

### 1) Flip-Flop em VHDL.

Iremos implementar um flip-flop tipo D como mostrado na figura abaixo:

![Imagem do Flip-Flop](imagensComponentes/FF_D.png)

**Antes de iniciar a descrição do flip-flop:**

-   Crie um novo projeto no Quartus e monte o esqueleto do código:
    -   Bibliotecas;
    -   Entidade;
    -   Arquitetura.
-   Remova a declaração **generic**.
-   Adicione o template de registrador na arquitetura:
    -   Insert Template > VHDL > Logic > Registers > Basic Positive Edge Register.

>    Neste ponto, temos a [estrutura][flipflopD] do programa montada. Inspecione o código, e leia os comentários, para reconhecer os blocos construtivos.

**Personalização do código:**

Entidade:

-   Crie nomes para os sinais de entrada e saída;
-   Para ambos, utilizaremos o tipo **STD_LOGIC**.

Arquitetura:

*   Acertar os nomes das entradas e saídas de acordo com o definido na entidade.
*   Como é um circuito sequencial, a lista de sensibilidade do **process()** não deve possuir todos os sinais de entrada:
    *   Neste caso, essa lista usa somente o sinal **clock**:
        *   Ou seja, quando houver uma transição do **clock**, o processo será ativado.
*   O **process()** será ativado tanto na transição de subida como na de descida do clock:
    -   Ele executará, sequencialmente, o código dentro do bloco **begin / end process**:
        -   Que contém o comando **if**.
    -   Esse comando **if**, seleciona qual a borda do **clock** que queremos utilizar:

```vhd
		if (rising_edge(<clock_signal>))   -- borda de subida.

		if (falling_edge(<clock_signal>))  -- borda de descida.
```

Neste caso, na ocorrência da borda de subida, serão executados os comandos dentro do **if**:

-   Que devem atribuir às saídas o valor da entrada naquele momento (ou seu inverso).

<!---
O código final deverá ser parecido com [este][codigoFFD].
-->

**Compilação:**

[Compile][compilacao] o circuito e verifique o circuito resultante com o  [RTL Viewer][rtlViewer]. Ele deve ser parecido com [este][rtlFFD].

**Simulação:**

Para testar o flip-flop, precisaremos de:

-   Sinal de *`clock`*;
-   Sinal de entrada de dados.

Inicie uma [simulação][simulacaoVWF] e crie esses vetores de teste. Faça com que o sinal de entrada mude aleatoriamente em relação à mudança do *`clock`*.

Verifique o resultado da sua simulação. Como referência, veja os resultados desta [simulação][simulFFD].

***

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

[flipflopD]:  ./vhdl/_esqueletoFlipFlopTipoD.html

[simulacaoVWF]: ./quartus/_simulacao.html

[compilacao]: ./quartus/_compilarProjetoQuartus.html

[rtlViewer]: ./quartus/_rtlViewerQuartus.html

[rtlFFD]: ./vhdl/_flipFlopTipoD.html#esquema-rtl-do-flip-flop-do-c%C3%B3digo-acima

[simulFFD]: ./vhdl/_simulacaoFFD.html

[linksUteis]: ./linksUteis.html

<!---
#######################################
###########Links Externos##############
####################################### --->

<!---
[novoProjeto]: ./_criarProjetoQuartus
[clausulaBiblioteca]: ./_recursosQuartus#acessar-a-biblioteca-de-modelos-templates
[clausulaUse]: ./_recursosQuartus#escolher-os-templates-de-interesse
[entidadeRegistrador]: ./_entidadeRegistrador
[inserirTemplateEscolhido]: ./_recursosQuartus#inserir-o-template-escolhido
[entidade]: ./_recursosQuartus#escolher-os-templates-de-interesse
[arquitetura]: ./_recursosQuartus#escolher-os-templates-de-interesse
[concurrentStatements]: ./_recursosQuartus#concurrentStatements
[recursosQuartus]: _recursosQuartus
[adicionarArqProjeto]:./_recursosQuartus#adicionar-um-arquivo-ao-projeto
[bibliotecaTemplates]: ./_recursosQuartus#acessar-a-biblioteca-de-modelos-templates
[declaracao]: ./_recursosQuartus#declaracao
[instanciacao]: ./_recursosQuartus#instanciacao



fim
--->
