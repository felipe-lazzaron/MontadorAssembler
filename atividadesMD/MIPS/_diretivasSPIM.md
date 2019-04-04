# Diretivas do Assembler

<br>

---

` .align n` : Align the next datum on a 2\^n byte boundary.

-   For example:
    -   ` .align 2` aligns the next value on a word boundary.
    -   ` .align 0` turns off automatic alignment of the directives:
        -   ` .half`;
        -   ` .word`;
        -   ` .float`;
        -   ` .double`
    -   Until the next ` .data` or ` .kdata` directive.

---

` .ascii str` : Store the string in memory, but do not null-terminate it.

---

` .asciiz str` : Store the string in memory and null-terminate it.

---

` .byte b1, ..., bn` : Store the *n* values in successive bytes of memory.

---

` .data ` : The following data items should be stored in the data segment.

-   If the optional argument *addr* is present, the items are stored beginning at address *addr*.

---

` .double d1, ..., dn` : Store the *n* floating point double precision numbers in successive memory locations.

---

` .extern sym size` : Declare that the datum stored at ` sym` is ` size` bytes large and is a global symbol.

-   This directive enables the assembler to store the datum in a portion of the data segment that is efficiently accessed via register `$gp`.

---

` .float f1, ..., fn` : Store the *n* floating point single precision numbers in successive
    memory locations.

---

` .globl sym` : Declare that symbol ` sym` is global and can be referenced from other files.

---

` .half h1, ..., hn` : Store the *n* 16-bit quantities in successive memory halfwords.

---

` .kdata ` : The following data items should be stored in the kernel data segment.

-   If the optional argument *addr* is present, the items are stored beginning at address *addr*.

---

` .ktext ` : The next items are put in the kernel text segment.

-   In SPIM, these items may only be instructions or words (see the ` .word` directive below).
-   If the optional argument *addr* is present, the items are stored beginning at address *addr*.

---

` .space n` : Allocate *n* bytes of space in the current segment (which must be the data segment in SPIM).

---

` .text ` : The next items are put in the user text segment.

-   In SPIM, these items may only be instructions or words (see the ` .word` directive below).
-   If the optional argument *addr* is present, the items are stored beginning at address *addr*.

---

` .word w1, ..., wn` : Store the *n* 32-bit quantities in successive memory words.

---
