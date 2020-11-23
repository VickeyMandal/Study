set serveroutput on

prompt Enter customer id
accept cno

declare
	fg number;
begin
	totalsale(&cno,fg);
	dbms_output.put_line('Customer No: '||&cno||' Total: '||fg);
end;
/
set serveroutput off