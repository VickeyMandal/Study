set serveroutput on
DECLARE
	/*Global variables*/
	a number := 50;
BEGIN
	if(a<42) then
		dbms_output.put_line('a is less than 42');
	else
		dbms_output.put_line('a is not less than 42');
	end if;
		dbms_output.put_line('Valu of a is : '||a);
END;
/
set serveroutput off