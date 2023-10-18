from AssemblerASM_BIN_VHDL import defineComentario, defineInstrucao, trataMnemonico, converteArroba, converteArroba9bits, converteCifrao, converteCifrao9bits

def main():
    inputASM = './AssemblerASM_BIN_VHDL/ASM.txt'  # Arquivo de entrada que contém o assembly
    outputBIN = './AssemblerASM_BIN_VHDL/BIN.txt'  # Arquivo de saída que contém o binário formatado para VHDL
    outputMIF = './AssemblerASM_BIN_VHDL/initROM.mif'  # Arquivo de saída que contém o binário formatado para .mif

    noveBits = False

    mne = { 
        "NOP": "0",
        "LDA": "1",
        "SOMA": "2",
        "SUB": "3",
        "LDI": "4",
        "STA": "5",
        "JMP": "6",
        "JEQ": "7",
        "CEQ": "8",
        "JSR": "9",
        "RET": "A",
    }

    with open(inputASM, "r") as f:
        lines = f.readlines()

    with open(outputBIN, "w+") as f:
        cont = 0
        for line in lines:
            if line.startswith('\n') or line.startswith(' ') or line.startswith('#'):
                line = line.replace("\n", "")
                print("-- Sintaxe inválida" + ' na Linha: ' + ' --> (' + line + ')')
            else:
                comentarioLine = defineComentario(line).replace("\n", "")
                instrucaoLine = defineInstrucao(line).replace("\n", "")
                instrucaoLine = trataMnemonico(instrucaoLine)

                if '@' in instrucaoLine:
                    if not noveBits:
                        instrucaoLine = converteArroba(instrucaoLine)
                    else:
                        instrucaoLine = converteArroba9bits(instrucaoLine)
                elif '$' in instrucaoLine:
                    if not noveBits:
                        instrucaoLine = converteCifrao(instrucaoLine)
                    else:
                        instrucaoLine = converteCifrao9bits(instrucaoLine)
                else:
                    instrucaoLine = instrucaoLine.replace("\n", "")
                    if not noveBits:
                        instrucaoLine = instrucaoLine + '00'
                    else:
                        instrucaoLine = instrucaoLine + "\" & " + "\'0\' & " + "x\"00"

                line = 'tmp(' + str(cont) + ') := x"' + instrucaoLine[0] + '" & \'0\' & x"' + instrucaoLine[1:] + '";\t-- ' + comentarioLine + '\n'
                cont += 1
                f.write(line)
                print(line, end='')

    with open(outputMIF, "r") as f:
        headerMIF = f.readlines()

    with open(outputBIN, "r") as f:
        lines = f.readlines()

    with open(outputMIF, "w") as f:

        # Adicione as linhas de comentário no início do arquivo
        f.write("-- Copyright (C) 2017  Intel Corporation. All rights reserved.\n")
        f.write("-- Your use of Intel Corporation's design tools, logic functions\n")
        f.write("-- and other software and tools, and its AMPP partner logic\n")
        f.write("-- functions, and any output files from any of the foregoing\n")
        f.write("-- (including device programming or simulation files), and any\n")
        f.write("-- associated documentation or information are expressly subject\n")
        f.write("-- to the terms and conditions of the Intel Program License\n")
        f.write("-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n")
        f.write("-- the Intel FPGA IP License Agreement, or other applicable license\n")
        f.write("-- agreement, including, without limitation, that your use is for\n")
        f.write("-- the sole purpose of programming logic devices manufactured by\n")
        f.write("-- Intel and sold by Intel or its authorized distributors.  Please\n")
        f.write("-- refer to the applicable agreement for further details.\n\n")
        
        f.write("WIDTH=8;\n")
        f.write("DEPTH=256;\n")
        f.write("ADDRESS_RADIX=DEC;\n")
        f.write("DATA_RADIX=HEX;\n\n")
        f.write("CONTENT BEGIN\n")
        f.write("--endereco : dado;\n")

        for line in lines:
            replacements = [('t', ''), ('m', ''), ('p', ''), ('(', ''), (')', ''), ('=', ''), ('x', ''), ('"', '')]
            for char, replacement in replacements:
                if char in line:
                    line = line.replace(char, replacement)

            line = line.split('#')

            if "\n" in line[0]:
                line = line[0]
            else:
                line = line[0] + '\n'

            f.write(line)  # Escreve as linhas formatadas no arquivo .mif


if __name__ == "__main__":
    main()
