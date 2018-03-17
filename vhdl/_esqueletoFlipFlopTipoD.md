## Esqueleto VHDL de um Flip Flop tipo D:

```vhd
-- A library clause declares a name as a library.  It
-- does not create the library; it simply forward declares
-- it.
library <library_name>;
use <library_name>.<package_name>.all;

entity <entity_name> is
	port
	(
		-- Input ports
		<name>	: in  <type>;
		<name>	: in  <type> := <default_value>;

		-- Inout ports
		<name>	: inout <type>;

		-- Output ports
		<name>	: out <type>;
		<name>	: out <type> := <default_value>
	);
end <entity_name>;


architecture <arch_name> of <entity_name> is

	-- Declarations (optional)

begin

	-- Process Statement (optional)

	-- Concurrent Procedure Call (optional)

	-- Concurrent Signal Assignment (optional)

	-- Conditional Signal Assignment (optional)

	-- Selected Signal Assignment (optional)

	-- Component Instantiation Statement (optional)

	-- Generate Statement (optional)

-- Update the register output on the clock's rising edge
	process (<clock_signal>)
	begin
		if (rising_edge(<clock_signal>)) then
			<register_variable> <= <data>;
		end if;
	end process;

end <arch_name>;
```
