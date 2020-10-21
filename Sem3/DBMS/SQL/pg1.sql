set serveroutput on
DECLARE
	/*Global variables*/
	num1 number := 25;
	num2 number := 34;
BEGIN
	dbms_output.put_line('value of num1: '|| num1);
	dbms_output.put_line('value of num2: '|| num2);
	DECLARE
		--local variables
		num1 number := 8;
		num2 number := 10;
	BEGIN
		dbms_output.put_line('value of num1: '|| num1);
		dbms_output.put_line('value of num2: '|| num2);
	END;
END;
/
set serveroutput off