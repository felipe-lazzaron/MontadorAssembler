# Temporização DE2-115

<a name="inicio"></a>

O conteúdo abaixo deve ser salvo em um arquivo chamado de "nome projeto".sdc.

***

Conjunto mínimo de definições de temporização para projetos usando a placa DE2-115.

```asm
# Minimal constraints (altera)
create_clock -name "CLOCK_50" -period 20.000ns [get_ports {CLOCK_50}]
derive_pll_clocks
derive_clock_uncertainty

# Automatically apply a generate clock on the output of phase-locked loops (PLLs)
# This command can be safely left in the SDC even if no PLLs exist in the design
derive_pll_clocks
```

<br>

<a name="fimDocumento"></a> [Ir para o início do documento](#inicio).
