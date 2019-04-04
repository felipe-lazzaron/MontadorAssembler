## Geração de código VHDL:

No caso da utilização de descrição do circuito através do diagrama lógico, pode-se verificar, ou mesmo exportar, o código equivalente ao diagrama. Para isso, use a opção *Create HDL Design File from Curret File*: 

-   Menu File:
    -   Create / Update:
        -   Create HDL Design File from Curret File...
            -   Selecione VHDL;
            -   OK.
-   Vá no diretório do projeto e abra o arquivo “.VHD” no editor de texto.

Para uma porta AND, o programa será similar ao seguinte:

```vhd
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
LIBRARY work;

ENTITY portaAND IS
PORT (
    entrada1 : IN STD_LOGIC;
    entrada2 : IN STD_LOGIC;
    saida : OUT STD_LOGIC
);
END portaAND;

ARCHITECTURE bdf_type OF portaAND IS
BEGIN
	saida  <=  entrada1  AND  entrada2;
END bdf_type;
```
