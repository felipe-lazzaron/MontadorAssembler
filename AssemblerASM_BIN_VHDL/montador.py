from funcoes_auxiliares import *

inputASM = "ASM.txt"  # Arquivo de entrada de contém o assembly
outputBIN = "BIN.txt"  # Arquivo de saída que contém o binário formatado para VHDL
outputMIF = "initROM.mif"  # Arquivo de saída que contém o binário formatado para .mif

# Ler o arquivo de entrada ASM.txt e escrever o resultado em BIN.txt
with open("ASM.txt", "r") as arquivo_asm, open("BIN.txt", "w") as arquivo_bin:
    for linha in arquivo_asm:
        linha_traduzida = traduzASMparaVHDL(linha)
        arquivo_bin.write(linha_traduzida + "\n")

print("Tradução concluída. O resultado foi salvo em BIN.txt.")