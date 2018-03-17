<a name="inicio"></a>

## Implementações:

Ir para o [fim do documento](#fimDocumento) e referências.

---

### 1) Temporização na lógica sequencial:

#### Contextualização:

Utilizaremos o _pipeline_ da atividade 3 para verificar os atrasos de temporização existentes.

![](imagensComponentes/pipeline-2.png)

---

#### Objetivo:

Comparar os resultados da simulação funcional e da simulação temporal. Para isso, utilizaremos um _pipeline_ de 8 bits e dois estágios. Dentro dos estágios teremos uma lógica combinacional simples.

**Criação do projeto:**

Crie o projeto e utilize, para o registrador e _pipeline_, os códigos dos _links_ abaixo:

-   A implementação do [_pipelilne_][codigoPipeline].

-   A implementação do [_registrador_][codigoRegistrador].

Codifique o _top-level_ para visualizar todas as entradas e saídas. Ou seja, as saídas intermediárias devem estar na entidade do _top-level_ para que sejam acessíveis na simulação.

**Compilação e Verificação:**

Compile o circuito e use o _RTL Viewer_ para confirmar a conexão feita entre os registradores.

**Simulação:**

Para a simulação utilizaremos a sequência do _Quiz_ 1. Abaixo, temos os valores na (já estáveis) entrada de R1 no momento da subida de cada _clock_:

-   _clock_ #1: _0xFF_;
-   _clock_ #2: _0x02_;
-   _clock_ #3: _0x30_;
-   _clock_ #4: _0x4F_;
-   _clock_ #5: _0x01_;
-   _clock_ #6: _0x00_;

Iremos executar duas simulações:

-   A [simulação funcional][simula];

-   E a [simulação temporal][simula].


Faça um _printscreen_ do resultado de cada simulação. Compare os resultados e  verifique a relação entre os sinais de entrada e as saídas do _pipeline_.

---

<br>

**Referências:**

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

---

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

<!--
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[codigoPipeline]: ./vhdl/_pipelineTemporizacao.html

[codigoRegistrador]: ./vhdl/_registrador.html

[simula]: ./quartus/_simulacaoTemporalFuncional.html

[linksUteis]: ./linksUteis.html
