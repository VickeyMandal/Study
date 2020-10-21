set serveroutput on
DECLARE
	/*Global variables*/
	n number;
	m number;

BEGIN

	/*dbms_output.put_line('Enter first number: ');*/
	n := &number;
	/*dbms_output.put_line('Enter second number: ');*/
	m := &number;
	if(n>m) then
	dbms_output.put_line(n ||' is greater than ' || m);
	else
	dbms_output.put_line(m ||' is greater than ' || n);
	end if;
END;
/
set serveroutput off