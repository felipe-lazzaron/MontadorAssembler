<a name="inicio"></a>

## Objetivos:

1.  Aplicar o tipo de dados *`array`* do VHDL.
2.  Implementar arquivo de registradores em VHDL.

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

<a name="arqREG"></a>

## 3) Arquivo de Registradores.

### Contextualização:

Caso queira rever a contextualização do primeiro item, [clique aqui](Aula-4A.html).

O arquivo de registradores é o armazenamento temporário existente dentro da CPU. Nele estão os registradores de propósito geral do processador, que são acessíveis ao programador. A velocidade desse conjunto é um fator importante na velocidade final da CPU.

Eles são utilizados para armazenar os dados que estão sendo manipulados. Por exemplo, durante a soma de dois valores:

A = B + C;

Os valores de B e C são lidos de dois registradores e o valor resultante (A) é armazenado em outro registrador. Para aumentar a velocidade, seria interessante ler os dois registradores ao mesmo tempo. Para tanto, o arquivo de registradores deve possuir duas portas de leitura. Se quiser escrever o resultado durante o mesmo ciclo, será necessária uma porta de escrita adicional.

### Objetivo:

Como o processador MIPS DLX possui duas portas de leitura e uma de escrita, iremos implementar algo semelhante:

![](./imagensComponentes/arquivoRegistradores-1.svg)

-   8 Registradores de 8 bits;
-   2 portas de leitura;
-   1 porta de escrita;
-   1 sinal de ativar escrita.

Para que exista uniformidade entre as implementações, use a interface abaixo:

```vhd
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- Baseado no apendice C (Register Files) do COD (Patterson & Hennessy).
entity bancoRegistradores is
	generic
	(
		larguraDados        : natural := 8;
		larguraEndBancoRegs : natural := 3
	);
-- Leitura de 2 registradores e escrita em 1 registrador simultaneamente.
	port
	(
		clk		   : in std_logic;
--
		enderecoA		: in std_logic_vector((larguraEndBancoRegs-1) downto 0);
		enderecoB		: in std_logic_vector((larguraEndBancoRegs-1) downto 0);
		enderecoC  	: in std_logic_vector((larguraEndBancoRegs-1) downto 0);
--
		dadoEscritaC  	: in std_logic_vector((larguraDados-1) downto 0);
--		
		escreveC	  : in std_logic := '1';
--
		saidaA			: out std_logic_vector((larguraDados -1) downto 0);
		saidaB			: out std_logic_vector((larguraDados -1) downto 0)
	);
end entity;
```

Lembre-se que a escrita é síncrona e a leitura não.

Codifique e simule. Verifique que o dado escrito pode ser lido no mesmo ciclo de clock.

#### Para um chute inicial:

> Veja o [apêndice C][resourcesCOD4Ed] do livro texto: "Organização e Projeto de Computadores - a interface Hardware/Software".

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

[vhdlBasico]: ./vhdl/_vhdlBasico.html

[bibliotecaTemplates]: ./quartus/_recursosQuartus.html#acessar-a-biblioteca-de-modelos-templates

[renertaVHDLRefGuide]: http://vhdl.renerta.com

[freeRangeTutoriais]: http://freerangefactory.org/books_tuts.html

[VHDLTutorialElsevier]: http://booksite.elsevier.com/9780124077263/downloads/VHDL_Tutorials/vhdl-tutorial.pdf

[linksUteis]: ./linksUteis.html

[resourcesCOD4Ed]: https://booksite.elsevier.com/9780123747501/downloads/Resources.zip
