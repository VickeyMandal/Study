set serveroutput on
DECLARE
	/*Global variables*/
	var varchar2(30) := 'Hello!';
BEGIN
	dbms_output.put_line(var);
END;
/
set serveroutput off