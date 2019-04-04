<a name="inicio"></a>

# Aula 13: Revisão


### Instrução JAL

Implemente, no fluxo de dados, a instrução jal (Jump And Link) conforme o funcionamento descrito abaixo:

> R[31]=PC+4;PC=JumpAddr

**Esta é uma instrução do tipo J**

![**Fluxo de Dados do DLX**](imagensMIPS/fluxoDadosCompleto-1ciclo-Final.svg){width=800px}


<div class="bloco solucao" id="sol-ExJAL">
<div class="conteudo">
<p style="color:red">Solução:</p>

Como esse fluxo de dados já atende a instrução jump, todo o circuito de montagem do endereço destino está pronto.

> endereço=(PC+4)[31..28],imediato<25..0>,0,0);

O que falta é o armazenamento de PC+4 no registrador 31 do banco.

![**Fluxo de Dados do DLX + JAL**](imagensMIPS/fluxoDadosCompleto-1ciclo-Final+JAL.svg){width=800px}

</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>
<br>

***

### Instrução ADDI

No fluxo de dados abaixo, quais as alterações necessárias para executar a instrução addi?

> R[rt] = R[rs] + SignExtImm

Além disso, como ficaria a  palavra de controle para essa instrução?

**Esta é uma instrução do tipo I**

![**Fluxo de Dados do DLX**](imagensMIPS/fluxoDadosCompleto-1ciclo-Final.svg){width=800px}

<div class="bloco solucao" id="sol-ExADDI">
<div class="conteudo">
<p style="color:red">Solução:</p>

Não é necessário nenhuma alteração no fluxo de dados.

Porém, a unidade de controle deverá decodificar essa instrução e ativar os pontos como mostrado abaixo:

|mux([PC+4, BEQ]/Jmp)|mux(Rt/Rd)|habEscritaReg|mux(Rt/Imediato)|ULA|mux(ULA/mem)|BEQ|habLeituraMEM|habEscritaMEM|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
||||||||||
|0|0|1|1|soma|0|0|0|0|

</div>
<button onclick="exibe(this)">Ver Solução</button>
</div>

<br>

***

### Endereçamento

Para o mapa de memória abaixo, projete o decodificador de endereços para as memórias externas.

![**Mapa de Memória do i386 (parcial)**](imagensComponentes/mapaMemoria-386.svg){width=400px}

<br>

***

### VHDL

Faça a codificação em VHDL para o circuito mostrado abaixo.

Considere que o sinal de _clock_ está distribuido adequadamente e os componentes já estão implementados em seus devidos arquivos.

Faça a instanciação e o mapeamento de portas.

![**Program Counter**](imagensComponentes/implementarVHDL-1.svg){width=600px}

<br>

***

<br>

## Referências

[Página com links][linksUteis] de referências sobre VHDL, Quartus, etc ...

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).

***

<br>

***

***

<!-- FIM -->

<!---
######### (inicio dos links) ##########
#######################################
########### Links Internos ############
--->

[vhdlBasico]: ./vhdl/_vhdlBasico.html

[bibliotecaTemplates]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[renertaVHDLRefGuide]: http://vhdl.renerta.com

[freeRangeTutoriais]: http://freerangefactory.org/books_tuts.html

[VHDLTutorialElsevier]: http://booksite.elsevier.com/9780124077263/downloads/VHDL_Tutorials/vhdl-tutorial.pdf

[linksUteis]: ./linksUteis.html

[resourcesCOD4Ed]: https://booksite.elsevier.com/9780123747501/downloads/Resources.zip

