set serveroutput on
DECLARE
	/*Global variables*/
	n number;
BEGIN
	n := &number;
	if mod(n,2)=0 then
		dbms_output.put_line('number is even');
	else
		dbms_output.put_line('number is odd');
	end if;
END;
/
set serveroutput off