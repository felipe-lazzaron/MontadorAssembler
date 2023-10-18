# MontadorAssembler
Disciplina de Projeto de Computadores

```markdown
# AssemblerASM_BIN_VHDL

Este é um utilitário de linha de comando Python que converte código assembly para representação binária formatada para uso em projetos VHDL. Também inclui a funcionalidade de gerar um arquivo MIF a partir do código binário formatado.

## Como Usar

### Requisitos

- Python 3.x

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/AssemblerASM_BIN_VHDL.git
   cd AssemblerASM_BIN_VHDL
   ```

2. Execute o programa:

   ```bash
   python montador.py
   ```

3. O programa solicitará que você forneça o caminho para o arquivo de código assembly.

4. O utilitário gerará um arquivo de saída BIN.txt com a representação binária e um arquivo initROM.mif para uso em projetos VHDL.

## Exemplo de Código Assembly

Um exemplo de código assembly suportado é o seguinte:

```
; Comentário
LDA 5    ; Comentário após instrução
NOP
STA $0
```

## Arquivo de Saída

O arquivo de saída BIN.txt conterá a representação binária formatada:

```
tmp(0) := x"10";  -- LDA 5
tmp(1) := x"00";  -- NOP
tmp(2) := x"50";  -- STA $0
```

## Configuração do Arquivo MIF

O arquivo initROM.mif é gerado para uso em projetos VHDL. Ele começa com configurações de largura de dados, profundidade e representação de endereço:

```
WIDTH=8;
DEPTH=256;
ADDRESS_RADIX=DEC;
DATA_RADIX=HEX;
```

## Contribuição

Sinta-se à vontade para contribuir para o projeto. Abra uma issue ou envie um pull request.

## Licença

Este projeto é licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para detalhes.

```

