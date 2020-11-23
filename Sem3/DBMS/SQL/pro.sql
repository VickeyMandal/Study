set serveroutput on

declare
	a number;
	b number;
	c number;
procedure min(x IN number, y IN number, z OUT number)
is
	begin 
		if x<y then
			z:=x;
		else
			z:=y;
		end if;
	end;
	begin
		a:= 45;
		b:=23;
		min(a,b,c);
		dbms_output.put_line('Minimum value: '||c);
	end;
	/
set serveroutput off






