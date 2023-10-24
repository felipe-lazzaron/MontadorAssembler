inputASM = "ASM.txt"  # Arquivo de entrada de contém o assembly
outputBIN = "BIN.txt"  # Arquivo de saída que contém o binário formatado para VHDL
outputMIF = "initROM.mif"  # Arquivo de saída que contém o binário formatado para .mif


registradores = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "R7": "111",
}

simbolos = {
    "HEX0": 288,  # em binario é 100100000
    "HEX1": 289,  # em binario é 100100001
    "HEX2": 290,  # em binario é 100100010
    "HEX3": 291,  # em binario é 100100011
    "HEX4": 292,  # em binario é 100100100
    "HEX5": 293,  # em binario é 100100101
    "KEY0": 352,  # em binario é 101100000
    "KEY1": 353,  # em binario é 101100001
    "KEY2": 354,  # em binario é 101100010
    "KEY3": 355,  # em binario é 101100011
}

mnemonicos_possiveis = [
    "NOP",
    "LDA",
    "SOMA",
    "SUB",
    "LDI",
    "STA",
    "JMP",
    "JEQ",
    "CEQ",
    "JSR",
    "RET",
    "OP_AND",
]

minhas_subrotinas = {}

def converteDecimalParaBinario(numero, bits=9):
    return "{0:b}".format(numero).rjust(bits, "0")


def identificaMnemonico(line):
    # Divide a linha por espaços em branco
    parts = line.split()

    for part in parts:
        if part in mnemonicos_possiveis:
            return part

    # Se nenhum mnemônico for encontrado na linha, retorne None
    return None

def converteRegistradores(line):
    # Divide a linha por espaços em branco
    parts = line.split()

    for part in parts:
        if part in registradores:
            return registradores[part]

    # Se nenhum registrador foi encontrado, retorne None ou outra indicação de erro, se desejado
    return None

def converteSimbolos(line):
    # Divide a linha por espaços em branco
    parts = line.split()

    for part in parts:
        if part.startswith("."):
            symbol_name = part[1:]  # Remove o ponto no início
            if symbol_name in simbolos:
                decimal_value = simbolos[symbol_name]
                binary_value = converteDecimalParaBinario(decimal_value)
                return binary_value

    # Se nenhum símbolo for encontrado na linha, retorne None
    return None

def converteCifrao(line):
    # Divide a linha por espaços em branco
    parts = line.split()

    for part in parts:
        if part.startswith("$"):
            decimal_value = int(part[1:])
            binary_value = converteDecimalParaBinario(decimal_value)
            return binary_value

    # Se nenhum valor após o cifrão for encontrado, retorne None ou outra indicação de erro
    return None

def converteArroba(line):
    # Divide a linha por espaços em branco
    parts = line.split()

    for part in parts:
        if part.startswith("@"):
            decimal_value = int(part[1:])
            binary_value = converteDecimalParaBinario(decimal_value)
            return binary_value

    # Se nenhum valor após o cifrão for encontrado, retorne None ou outra indicação de erro
    return None

def defineComentario(line):
    if "#" in line:
        line = line.split("#")
        line = line[0] + "\t#" + line[1]
        return line
    else:
        return line

def defineInstrucao(line):
    line = line.split("#")
    line = line[0]
    return line

def identificaInicioSubrotina(line):
    parts = line.split(":")
    if len(parts) > 1 and parts[0].strip():
        return parts[0].strip()
    return None

def identificaChamadaDeSubrotina(line):
    parts = line.split()
    for part in parts:
        if part.startswith("."):
            return part[1:]  # Remove o ponto no início
    return None

def retornaNumeroLinhaSubrotinaBinario(nome_subrotina):
    return converteDecimalParaBinario(minhas_subrotinas[nome_subrotina])
def montaLinhaVHDL(line,numero_linha):
    # Remove comentários
    line = defineComentario(line)

    # Remove espaços em branco
    line = line.strip()
    # Identifica o comentário
    comentario = defineComentario(line)
    # Identifica o mnemônico
    mnemonico = identificaMnemonico(line)
    # Identifica o registrador
    registrador = converteRegistradores(line)
    # Identifica o cifrão
    cifrao = converteCifrao(line)
    # Identifica o arroba
    arroba = converteArroba(line)
    # Identifica o símbolo
    simbolo = converteSimbolos(line)
    # Identifica o início de uma subrotina
    inicio_subrotina = identificaInicioSubrotina(line)
    # Identifica a chamada de uma subrotina
    chamada_subrotina = identificaChamadaDeSubrotina(line)
    # print("------------------")
    # print("linha: ", numero_linha)
    # print("comentario: ", comentario)
    # print("mnemonico: ", mnemonico)
    # print("registrador: ", registrador)
    # print("cifrao: ", cifrao)
    # print("simbolo: ", simbolo)
    # print("inicio_subrotina: ", inicio_subrotina)
    # print("chamada_subrotina: ", chamada_subrotina)
    # print("------------------")
    if mnemonico == "LDI":
        linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador, cifrao)
    elif mnemonico == "STA":
        if (simbolo):
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador,simbolo)
        elif (arroba):
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador, arroba)
        else:
            linha_traduzida = "ERROR: STA"
            print("ERROR: STA")
            print("linha: ", numero_linha)
            print("comentario: ", comentario)
            print("mnemonico: ", mnemonico)
            print("registrador: ", registrador)
            print("cifrao: ", cifrao)
            print("simbolo: ", simbolo)
            print("inicio_subrotina: ", inicio_subrotina)
            print("chamada_subrotina: ", chamada_subrotina)
            print("------------------")
    elif mnemonico == "LDA":
        if (simbolo):
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador,simbolo)
        else:
            linha_traduzida = "ERROR: LDA"
            print("ERROR: LDA")
            print("linha: ", numero_linha)
            print("comentario: ", comentario)
            print("mnemonico: ", mnemonico)
            print("registrador: ", registrador)
            print("cifrao: ", cifrao)
            print("simbolo: ", simbolo)
            print("inicio_subrotina: ", inicio_subrotina)
            print("chamada_subrotina: ", chamada_subrotina)
            print("------------------")
    elif mnemonico == "OP_AND":
        if (arroba):
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador, arroba)
        else:
            linha_traduzida = "Erro: OP_AND"
    elif mnemonico == "SOMA":
        if (cifrao):
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador, cifrao)
        else:
            linha_traduzida = "Erro: SOMA"
    elif mnemonico == "SUB":
        if (cifrao):
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador, cifrao)
        else:
            linha_traduzida = "Erro: SUB"
    elif mnemonico == "NOP":
        linha_traduzida = "tmp({}) := \"000000000\";".format(numero_linha)
    elif mnemonico == "CEQ":
        if (arroba):
            registrador = "000"
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador, arroba)
    elif mnemonico == "JEQ":
        if (chamada_subrotina):
            registrador = "000"
            endereco = retornaNumeroLinhaSubrotinaBinario(chamada_subrotina)
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador,endereco )
        else:
            linha_traduzida = "Erro: JEQ"
    elif mnemonico == "JMP":
        if (chamada_subrotina):
            registrador = "000"
            endereco = retornaNumeroLinhaSubrotinaBinario(chamada_subrotina)
            linha_traduzida = "tmp({}) := {} & \"{}\" & \"{}\";".format(numero_linha, mnemonico, registrador,endereco )
        else:
            linha_traduzida = "Erro: JMP"
    elif mnemonico == "RET":
        linha_traduzida = "tmp({}) := \"000000000\";".format(numero_linha)
    else:
        linha_traduzida = "Erro: mnemônico ainda não implementado"
        print("linha: ", numero_linha)
        print("comentario: ", comentario)
        print("mnemonico: ", mnemonico)
        print("registrador: ", registrador)
        print("cifrao: ", cifrao)
        print("simbolo: ", simbolo)
        print("inicio_subrotina: ", inicio_subrotina)
        print("chamada_subrotina: ", chamada_subrotina)
        print("------------------")

    print(linha_traduzida)


with open("ASM.txt", "r") as arquivo_asm:
    for numero_linha, linha in enumerate(arquivo_asm, 0):
        if (identificaInicioSubrotina(linha)):
            nome_rotina = identificaInicioSubrotina(linha)
            minhas_subrotinas[nome_rotina] = int(numero_linha) + 1

with open("ASM.txt", "r") as arquivo_asm:
    for numero_linha, linha in enumerate(arquivo_asm, 0):
        montaLinhaVHDL(linha,numero_linha)