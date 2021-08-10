Windows 10
==========

Por: Marco Antonio Soares de Mello Alves (Laboratório de Arquitetura de
Computadores)

Dúvidas:

> **Email: marcoasma@insper.edu.br**

> **Teams: marco.alves@al.insper.edu.br**

Quartus 20.1 e ModelSim 20.1
============================

Instalando
----------

1.  Faça o download dos arquivos a seguir (salve na mesma pasta, todos
    os arquivos):

-   Quartus Lite 20.01:
    https://download.altera.com/akdlm/software/acdsinst/20.1std/711/ib_installers/QuartusLiteSetup-20.1.0.711-windows.exe

-   ModelSim:
    https://download.altera.com/akdlm/software/acdsinst/20.1std/711/ib_installers/ModelSimSetup-20.1.0.711-windows.exe

-   Cyclone V (Chip usado no curso) :
    https://download.altera.com/akdlm/software/acdsinst/20.1std/711/ib_installers/cyclonev-20.1.0.711.qdz

2.  Execute o arquivo **QuartusLiteSetup-20.1.0.711-windows.exe** e
    clique **Next** até a instalação iniciar:
    
![installQuartus](imgs/installQuartus.png)

<p align="center">
  <img src="imgs/installQuartus.png">
</p>
    

3.  Após a instalação, finalize-a com as seguintes opções:

![finish](imgs/finish.png)



4.  A instalação do USB Blaster deverá iniciar em seguida:

![UBSblaster](imgs/UBSblaster.png)



Atualizando o USB Blaster
-------------------------

Mesmo instalando o driver é necessário atualiza-lo.

1.  Pressione Windows + R no teclado e insira o comando **devmgmt.msc**:

![devmgmt](imgs/devmgmt.png)



2.  O gerenciador de dispositivo deverá abrir:

![gerenciadorDISP](imgs/gerenciadorDISP.png)



3.  Conecte a placa e o driver USB-Blaster será reconhecido da seguinte
    maneira:

![blasterNreconhecido](imgs/blasterNreconhecido.png)



4.  O símbolo de atenção em amarelo indica que o driver está
    desatualizado, selecione a opção **Atualizar driver** clicando com o
    botão direito do mouse em cima do USB-Blaster, a janela a baixo
    deverá abrir:

![atualizarBlaster](imgs/atualizarBlaster.png)



5.  Selecione a opção **Procurar software de driver no computador** e
    defina o caminho da pasta intelFPGA\_lite (caso tenha sido alterado
    o caminho de instalação do quartus o padrão é "\*\*C:\_lite\*\*"),
    selecione incluir subpastas e clique em avançar:

![incluirSub](imgs/incluirSub.png)



6.  Aguarde a instalação do drive e o USB-Blaster agora deverá aparecer
    como **Altera USB-Blaster**, conforme a imagem abaixo:

![AlteraUSB](imgs/AlteraUSB.png)



Validando
=========

1.  Execute o Quartus (**Quartus (Quartus Prime 20.1) Lite Edition**),
    esse ícone deverá estar na sua área de trabalho:

![IconeQuartus](imgs/IconeQuartus.png)



2.  Selecione a segunda opção **Run the Quartus Prime Software**

3.  Por fim, o programa deverá abrir:

![quartusAberto](imgs/quartusAberto.png)

quartusAberto
