set serveroutput on

declare
	a number;
	procedure sq(x IN OUT number)
	is
	begin
		x:=x*x;
	end sq;

	begin
		a:=4;
		sq(a);
		dbms_output.put_line('Square: '||a);
	end;
	/
set serveroutput off






