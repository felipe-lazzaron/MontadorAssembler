def main():
    input_asm = './AssemblerASM_BIN_VHDL/ASM.txt'  # Nome do arquivo de entrada com o código assembly
    output_bin = './AssemblerASM_BIN_VHDL/BIN.txt'  # Nome do arquivo de saída com o código binário formatado para VHDL
    output_mif = './AssemblerASM_BIN_VHDL/initROM.mif'  # Nome do arquivo de saída no formato .mif

    # Abre o arquivo de entrada ASM
    with open(input_asm, "r") as asm_file:
        asm_lines = asm_file.readlines()

    # Abre o arquivo de saída BIN
    with open(output_bin, "w") as bin_file:
        cont = 0

        for asm_line in asm_lines:
            asm_line = asm_line.strip()  # Remove espaços em branco no início e no final
            if not asm_line or asm_line.startswith("#"):
                continue  # Ignora linhas em branco e comentários

            # Realize o processamento e formatação das linhas do código assembly aqui
            # Substitua a lógica a seguir pelo seu próprio processamento
            instruction, comment = asm_line.split('#', 1)
            opcode, operand = instruction.strip().split(None, 1)
            address = hex(cont)[2:].zfill(2).upper()
            formatted_line = f"tmp({cont}) := x\"{opcode}{operand}\"; -- {comment.strip()}\n"

            bin_file.write(formatted_line)
            cont += 1

    # Abre o arquivo de saída .mif
    with open(output_mif, "w") as mif_file:
        mif_file.write("DEPTH = 256;\n")
        mif_file.write("WIDTH = 8;\n")
        mif_file.write("ADDRESS_RADIX = DEC;\n")
        mif_file.write("DATA_RADIX = HEX;\n")
        mif_file.write("CONTENT\n")
        mif_file.write("BEGIN\n")

        cont = 0

        for asm_line in asm_lines:
            asm_line = asm_line.strip()
            if not asm_line or asm_line.startswith("#"):
                continue

            # Realize o processamento e formatação das linhas do código assembly aqui
            # Substitua a lógica a seguir pelo seu próprio processamento
            instruction, _ = asm_line.split('#', 1)
            opcode, operand = instruction.strip().split(None, 1)
            address = cont
            formatted_line = f"{address}: {opcode}{operand};\n"

            mif_file.write(formatted_line)
            cont += 1

        mif_file.write("END;")

if __name__ == "__main__":
    main()
